# H1 2026 Student Accommodation Finance Report: methodology

Published by Student Accommodation Finance, 12 September 2026.

Activity window: 1 January to 30 June 2026 inclusive. Evidence cut-off: 12 September 2026. Later publications that report H1 are retrospective evidence. Later observations and forecasts are labelled as outlook material.

## Evidence architecture

The report combines four evidence classes: (1) public investment reports, lender announcements and interim accounts; (2) Companies House security records; (3) Construction Capital V2 planning exports; and (4) the Construction Capital V2 raw Land Registry file. A common city or similar name does not constitute an asset match. No financing-to-planning conversion rate is estimated.

Public market sources, dates and observation periods accompany the report. The principal agency investment series and independent agency checks have different coverage and preliminary status; their totals are not combined or averaged. Investment consideration, gross development value, debt commitments, drawn debt and outstanding balances are different measures. Transaction-level source records and counterparty mappings are retained privately; the public release contains aggregate findings.

## Companies House

The local database contains 3,464,115 charge records, with charge dates through 31 July 2026 and a company snapshot dated 1 August 2026. Backfill includes incomplete/error cases; it is not a verified census of student accommodation borrowing.

The query selects charge creation dates from 2026-01-01 inclusive to 2026-07-01 exclusive, joining legal company numbers. It screens for `student` in company names, or `student` / `pbsa` in collateral particulars, case-insensitively. Unique charge IDs are counted. It returns 128 instruments and 61 companies. Four evident non-property matches are excluded following review of business activity. The exclusion ledger is retained privately.

The retained exploratory cohort is 124 instruments across 57 companies. Monthly creation counts are 31, 15, 27, 16, 12 and 23. Only 10 have student wording in collateral particulars; even those words can refer to a tenant company rather than verified occupation. The screen can both omit student-property SPVs and retain entities whose secured assets are not student occupied. It is not a PBSA lender league table.

Four H1-created instruments were delivered in July. Security may be filed after creation, several instruments may secure one facility, and several SPVs may participate in one transaction. An entitled party can be a security agent, trustee or servicer. Neither loan value nor amount drawn is inferred from charge metadata. Snapshot status does not establish the debt balance or status at 30 June.

Two asset-level checks corroborate financing disclosures against registered security. The identities, legal entities, title references and source links are retained privately. These checks are separate from the keyword cohort and are not treated as exact announcement-date lending. Disclosed facility values come from the transaction source, not charge metadata.

## Planning

Source: the Construction Capital V2 `data/generated/planning` exports, containing 301 town files when examined. We use 288 files whose observation windows cover all of H1, corresponding to 188 authority labels. This window test is not proof of complete authority capture. The files are predominantly retrieved in September; dates and current status can reflect later updates.

A case-insensitive full-proposal `student` / `pbsa` search is deduplicated by authority and application reference. It produces 338 records across all rolling windows and 116 with H1 receipt dates. A separate H1 decision-date screen returns 100 records, including procedural decisions; it is not the same cohort or an approval count for new schemes.

The 116 received-date records are manually classified:

| Class | Records |
|---|---:|
| Primary capacity-related applications | 25 |
| Flexibility / alternative use / exit | 10 |
| Refurbishment, amenity and operating works | 8 |
| Planning administration | 61 |
| Neighbouring-authority consultation | 7 |
| Retrospective capacity | 2 |
| Companion listed-building consent | 1 |
| Proposed lawful-development conversion | 1 |
| Unrelated educational work | 1 |
| Total | 116 |

The core exhibit plots the first three classes; the other 73 records are identified separately. Capacity-related applications include new build, conversions, extensions, revised schemes and broad mixed-use outline applications. They are not necessarily distinct new schemes, net additional beds, funded projects or H1 consents. Flexibility records include a pre-application and a lawful-use record. Permission for another use does not establish implementation or actual loss of student beds.

The exports contain approved and pending records, but not a complete refused/withdrawn population. Some descriptions truncate and some dates are missing. No national approval rate, completion rate, net bed total or gross development value is derived. Generic residential `units` and `estimatedGdv` fields are excluded from PBSA calculations. Individual authority references, addresses and source links are retained privately; the public evidence file contains aggregate classifications.

## Sold-price analysis

Source: Construction Capital V2 `data/land-registry/pp-2026.csv`. File timestamp: 6 August 2026. Latest transaction date: 30 June 2026. Source SHA-256:

`29222c20e87e0782559ff06546c232c975d5956015fe23d24106dd3e098979cb`

Select H1-dated detached, semi-detached, terraced and flat transactions (D/S/T/F) in eight exact postal-town fields: BRISTOL, EXETER, LEEDS, MANCHESTER, NOTTINGHAM, OXFORD, SHEFFIELD and SOUTHAMPTON. Deleted records are excluded. Unique transaction GUIDs are retained; identical address/date/price rows with different GUIDs remain separate transactions. The selected file records all have addition status. No student-use label is available.

This gives 19,871 unique observed transaction GUIDs. Town counts are Bristol 4,064; Exeter 712; Leeds 2,854; Manchester 4,053; Nottingham 3,358; Oxford 559; Sheffield 2,343; Southampton 1,928. Medians are computed over observed prices, with terraced-house prices shown as additional context. These are cross-sectional property-mix medians, not a constant-quality index. Postal towns differ from local-authority boundaries and immediate university catchments.

Registration lag materially reduces observations close to the file's cut-off. Low June observations cannot establish declining liquidity; no growth rate is computed against a matured prior-year series. No uplift is applied for unregistered sales. These are general residential transactions, not verified student HMO or PBSA investment sales. They are never used as PBSA values per bed.

The lake's rolling sold aggregates and the Companies House database's replica table were audited but not used for these published statistics. The raw lake preserves transaction GUIDs and update fields. Heuristic postcode matches between charged properties and previous sale prices are not used.

## Financing sample

The six facilities are grouped into development/refurbishment (£73.65m, three facilities) and investment/term refinance (£69.05m, three facilities). Multi-purpose facilities are assigned once according to their primary disclosed use. The public breakdown avoids one-facility categories and does not allocate facility proceeds to individual uses.

Six selected facility announcements in H1 total £142.7m. This is a purposive public-disclosure sample, not a market total, representative panel or measure of cash advanced. The public release omits individual facility amounts, transaction dates, property identifiers and source links that could identify financing counterparties. Announcement dates are not necessarily legal completion or drawdown dates. Only announcements within the stated period are included, and repeated reporting is not counted as additional financing. The underlying amounts and deduplication ledger are retained privately.

The principal investment figures were checked against the original quarterly agency reports. The reported £2.1bn Q1 value is rounded; £164m Q2 implies roughly a 92% quarterly value reduction, not a precise unrounded growth rate. Q1 included five deals above £150m, with corporate acquisitions and forward-development structures contributing to the comparison base. The chart presents investment value and deal count on separate scales. We do not construct an adjusted series by selectively subtracting large deals.

Transaction count change: (13 / 20) - 1 = -35%. Lender balances and new-business flows have different scopes and must be evaluated against their own comparable period. Operator metrics are company-specific, and acquisitions can change comparability. Identifying lender and counterparty details are retained in the private research record.

Illustrative valuation: value = annual net operating income / yield. LTV = debt / value. With £1m income, 5% yield and £12m debt, value is £20m and LTV 60%. With £0.9m income and 5.5% yield, value is £16.36m and LTV 73.3%. At an assumed 60% refinance cap, proceeds are £9.82m and the repayment gap £2.18m before fees. Interest coverage = annual net operating income / annual interest; this assumes interest-only debt and excludes amortisation and reserve requirements. None of these assumptions is a lender quote or market forecast.

## Demand, outlook and reproducibility

Academic-year enrolments, UCAS deadline applicants, rolling-year visa grants and applications, and operator booking guidance are separately labelled. They cannot be summed or equated to occupied beds. England-specific regulatory evidence is not generalised to the whole UK. Market scenarios are original analysis, with no probability weights or unsupported numerical rent, investment or lending forecast.

The private publication project retains query code, reviewed classifications, source hashes, transaction evidence and counterparty mappings. Public chart tables are downloadable as CSV. The public database-evidence JSON contains aggregate findings, without company identifiers, charge codes, title references, property-level source links, machine-local paths or working database dumps.
