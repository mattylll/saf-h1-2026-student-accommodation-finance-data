# H1 2026 Student Accommodation Finance: supporting data

Study identifier: **SAF-H1-2026**. Published 12 September 2026. Activity window: 1 January–30 June 2026; evidence cutoff: 12 September 2026.

These are supporting files for the [H1 report](https://studentaccommodationfinance.co.uk/insights/h1-2026-student-accommodation-finance-report/), also archived at [Zenodo DOI 10.5281/zenodo.22733171](https://doi.org/10.5281/zenodo.22733171). This package represents the same study. Cite the original report and relevant underlying sources when using its evidence.

## Files and reading order

1. `methodology.md`: read first for population definitions, screening, dates, source attribution and exclusions.
2. `chart-data.csv`: 64 chart observations. UTF-8 with a byte-order mark; values retain their original units, currency symbols and rounding labels.
3. `database-evidence.json`: aggregate Companies House, planning and residential sold-price evidence, source vintages and verification hashes.

The three source files are copied byte-for-byte from the published release. This repository guide was adapted on 25 September 2026. The release is fixed; later evidence should be published as a separately identified update.

## Chart CSV dictionary

| Field | Meaning |
| --- | --- |
| `exhibit` | Exhibit identifier within the report. |
| `title` | Report exhibit title. |
| `row` | Category, period or scenario label. |
| `measure` | Metric or series label; interpret alongside the row. |
| `value` | Published display value, stored as text with units and rounding where applicable. |
| `scope_note` | Coverage and interpretation limitations that must accompany the observation. |

Do not sum mixed units or silently convert rounded investment values into precise amounts. A missing record or an unpublished counterparty is not a zero.

## JSON sections

`reportPeriod` and `compilationDate` define time coverage. `companiesHouse` describes screened charge instruments and their monthly/quarterly counts. `planning` records the observed application cohort and classifications. `sold` provides postal-town aggregates and the source vintage. `verification` contains hashes from the original publication workflow. `publicationScope` explains the aggregate-only release. These hashes are provenance information; their presence does not mean an independent reviewer accessed the private ledgers.

## Interpretation limits

- Residential sold evidence: 19,871 observed general residential transactions across eight exact postal towns. No student-property flag or PBSA valuation inference.
- Financing evidence: six selected announcements totalling £142.7m. Announcement amounts do not establish drawn lending, national market coverage or lender market shares.
- Charge evidence: 124 instruments across 57 screened companies. Instruments, companies and financing facilities are different units.
- Planning evidence: 116 observed H1-received records. Applications do not establish approvals, starts or net new beds.
- Private deal identities, record-level references and matching ledgers are not part of this public package. No synthetic transaction rows have been added.

## Reproduce the public-file checks

Run `python3 validate.py` with Python 3.9 or later. No packages or network access are needed. The script checks the source-file hashes, CSV structure and row count, H1 date coverage, charge totals, planning classification totals and postal-town sales totals. It prints a JSON result and exits with an error if a check fails.

These are checks of the published aggregates, not a recreation or independent audit of the private transaction extraction. Source hashes in `source-manifest.json` identify the frozen public release. `validate.py` was added for this repository; it is not the original extraction code.

For citation, use the associated report identified in `CITATION.cff`. Its Zenodo DOI identifies that report, not a new GitHub dataset DOI.

## Follow the evidence into a worked example

For a narrow, checked import that preserves display values and scope notes, use the [GitBook data reference](https://construction-capital.gitbook.io/student-accommodation-finance-data-reference). For the difference between activity dates and evidence publication, read the [date explainer](https://telegra.ph/Why-an-H1-finance-report-can-use-evidence-published-after-June-10-30).

The [Posit June-exclusion diagnostic](https://01a19b9d-0dff-28f1-f6ef-52427eb0117d.share.connect.posit.cloud/) uses these unchanged aggregates to examine town counts and shares. It is not a registration-lag correction or a recalculation of sale-price medians. The separate [refinance explorer](https://saf-h1-2026-refinance-explorer.streamlit.app/) illustrates valuation assumptions; it adds no observed lending data.

Use the [H1 research navigation guide](https://sites.google.com/view/saf-h1-2026-research-guide/home) to choose a reading copy, presentation or analytical resource. These companions share authorship and source evidence with SAF-H1-2026; they do not provide independent corroboration or new reuse rights.

Use the [Colab median aggregation notebook](https://colab.research.google.com/github/mattylll/saf-h1-2026-student-accommodation-finance-data/blob/main/notebooks/median-aggregation.ipynb) to see why count-weighting town medians cannot recover a pooled median. It preserves the real town summaries and separates two unitless teaching examples from the source records. The [notebook source](notebooks/median-aggregation.ipynb) includes tested, saved outputs.

The [H1 student accommodation refinancing analysis](https://studentaccommodationfinance.wordpress.com/) explains the investment slowdown, selected financing activity and the effect of lower income and valuation on refinancing proceeds, with a worked repayment-gap example.

## Rights

The original publication reserves copyright. Third-party source material remains subject to its original publishers' terms. This reader guide grants no new licence over the source files. All rights reserved. No open reuse licence is granted over the original source package; contact the publisher for permission where required. Third-party rights and applicable statutory rights remain unaffected.
