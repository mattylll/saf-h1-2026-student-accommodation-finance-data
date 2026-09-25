#!/usr/bin/env python3
"""Check the frozen public aggregates; does not audit private transaction ledgers."""
import csv
import hashlib
import json
from pathlib import Path
import sys


def validate(root):
    checks = []

    def check(name, condition):
        checks.append({"check": name, "passed": bool(condition)})

    manifest = json.loads((root / "source-manifest.json").read_text())
    expected_files = {"chart-data.csv", "database-evidence.json", "methodology.md"}
    check("three expected source files", len(manifest) == 3 and
          {item["file"] for item in manifest} == expected_files)
    for item in manifest:
        if item["file"] not in expected_files:
            continue
        blob = (root / item["file"]).read_bytes()
        check(item["file"] + " byte length", len(blob) == item["bytes"])
        check(item["file"] + " SHA-256",
              hashlib.sha256(blob).hexdigest() == item["sha256"])

    with (root / "chart-data.csv").open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        check("six expected CSV fields", reader.fieldnames ==
              ["exhibit", "title", "row", "measure", "value", "scope_note"])
        rows = list(reader)
    check("64 chart observations", len(rows) == 64)
    check("CSV cells populated and row widths valid", all(
        None not in row and all(value is not None and value.strip()
                               for value in row.values()) for row in rows))
    evidence = json.loads((root / "database-evidence.json").read_text())
    check("H1 2026 coverage", evidence["reportPeriod"] ==
          {"from": "2026-01-01", "to": "2026-06-30"})
    check("12 September evidence cutoff", evidence["compilationDate"] == "2026-09-12")
    charges = evidence["companiesHouse"]
    check("monthly charges reconcile", sum(x["charge_instruments"] for x in
          charges["monthly"]) == charges["screenedChargeInstruments"] == 124)
    check("quarterly charges reconcile", sum(x["chargeInstruments"] for x in
          charges["quarterly"]) == charges["screenedChargeInstruments"])
    check("57 screened companies", charges["screenedCompanies"] == 57)
    planning = evidence["planning"]
    check("planning classifications reconcile", sum(planning["classification"].values())
          == planning["h1KeywordRecords"] == 116)
    sold = evidence["sold"]
    check("eight distinct postal towns", len(sold["cities"]) == 8 and
          len({x["town"] for x in sold["cities"]}) == 8)
    check("town sales reconcile", sum(x["observed_sales_h1"] for x in sold["cities"])
          == sold["observedRecordCount"] == 19871)
    months = ["2026-0" + str(i) for i in range(1, 7)]
    for town in sold["cities"]:
        monthly = town["monthly_observed_sales"]
        check(town["town"] + " six H1 months", [x["month"] for x in monthly] == months)
        check(town["town"] + " monthly sales reconcile", sum(x["sales"] for x in monthly)
              == town["observed_sales_h1"])
    return {"study": "SAF-H1-2026", "scope": "Public-file integrity and aggregate consistency only",
            "passed": all(x["passed"] for x in checks), "checks": checks}


if __name__ == "__main__":
    try:
        result = validate(Path(__file__).resolve().parent)
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"passed": False, "error": str(error)}, indent=2))
        sys.exit(1)
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["passed"] else 1)
