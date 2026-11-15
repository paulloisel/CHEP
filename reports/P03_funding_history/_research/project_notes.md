# P03 institutional and project funding research

as_of_date: 2026-11-15. Subtask only; shared brief, P03 and Summary.md read. No other prompt executed. All files are working inputs for consolidation.

## Strongest findings and proposed treatment

- **P03-F301:** [Conseil de l’Institut, 13 December 2022](https://www.sciencespo.fr/sites/default/files/cd_cp/ci2022/PVCI20221213.pdf), p. 3, explicitly reports a Harvard payment for CHEP received in 2022. Record the receipt as verified, but the amount, contract period, underlying donor, legal contracting parties and Paris expenditure remain unknown. Sciences Po is the institution discussing its receipts; do not silently turn its brand name into a verified legal recipient.
- **P03-F302 is an accounting observation, not an additional award.** [FNSP board minutes, 19 October 2022](https://www.sciencespo.fr/sites/default/files/cd_cp/ca/2022/PVCA20221019.pdf), p. 22, identify a rounded €0.9 million CHEP effect within the budget-execution discussion of *charges de fonds dédiés*. [6 December minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/ci2022/PVCI20221206.pdf), pp. 3–4, explain corresponding charges against CHEP-related receipts. Neither establishes €900,000 spent on research or the contractual grant value. F301 and F302 must not be summed; their exact transaction mapping requires internal records, so no fabricated parent ID is asserted. Retain F302 as explicitly excluded accounting context, or move it to the leads table.
- **P03-F304:** [Scientific council minutes, 10 March 2020, validated 2 June](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2020/2020_03_10_CSFR.pdf), §10, pp. 14–15, describe approximately six month-long doctoral bursaries already awarded. This is an aggregate announcement, not six verified payments. The [French host page](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/) identifies four 2020 selections and scheme-level cofinancing by the Direction scientifique through *la soufflerie*. Four named selections cannot be added to the approximate aggregate; match recipient and award registers first. The same minutes describe two three-year Harvard-funded postdocs awaiting selection in April, which are a plan, not named awards.
- **P03-F305:** [Emotions, climate, and the environment](https://histecon.fr/emotions_climate_environment/index.html) explicitly acknowledges CHEP funding. The [events archive](https://histecon.fr/en/events_recent.html) dates the workshop to 24 May 2024. Purpose: scholarly workshop. Amount and recipient entity remain unknown.
- **P03-F306:** [Invisible Actors in the Making of International Law programme](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2025-11-27ET28-INVISIBLE-ACTORS-VERSION5.pdf) expressly acknowledges cofunding by CHEP and the Sciences Po School of Research. The programme gives 27–28 November 2025; the [junior-colloquium index](https://www.sciencespo.fr/histoire/fr/les-formations/les-etudes-doctorales/le-colloque-junior/) gives 26–27 November. Prefer the specific programme for the ledger and flag the disagreement; neither date changes the support conclusion. Cofunding acknowledgment does not establish expenditure.

All links accessed 2026-11-15; source titles, document/event dates and indexed retrieval status are in project_sources.csv.

## Rows to move to calls_and_unverified_leads.csv

**F303 and F307–F313 are not verified cash awards.** F303 preserves the [EHC programme](https://histecon.fas.harvard.edu/ehc/) acknowledgment of continuing support by Carol Richards, the late David K Richards and the Richards family. The programme names Cambridge, Paris and Harvard as bases, but the text does not establish a discrete gift, legal recipient, amount or Paris allocation. Do not imply a proven Richards → Harvard → CHEP chain.

F307–F312 preserve hosting/support acknowledgments for Archives Notariales, the 2020–2022 slavery discussion group, Valuing Empires (2022), La vie matérielle des déplacés (2023), Imperial and Colonial Currencies (2024), and Belonging. Without a cash-specific statement, these are evidence of support, not proof of financial transfers. F313 preserves CHEP’s inclusion within the supported *Soufflerie* in the [2023 research annual report](https://www.sciencespo.fr/recherche/sites/sciencespo.fr.recherche/files/SciencesPo_RA2023-2_0.pdf), p. 42; no distinct allocation is specified.

The historical 2025 postdoctoral call at /fr/fellowships.html was a search lead only and timed out on opening. The main agent is handling calls. The search excerpt’s €45,000 gross annual salary cannot establish the salary paid to a subsequently named fellow.

## Attribution and chronology decisions

[The 2019 spatial workshop report](https://histecon.fr/en/spatial.html) explicitly calls 5 June 2019 a Paris launch event. This is compatible with the current home page distinguishing collaboration in 2019 from establishment in 2022. The March 2020 council minutes’ approximate reference to expansion to Paris a little over two years earlier is an unresolved earlier-prehistory lead; do not turn it into an exact 2017/2018 funding date.

The opened French Sciences Po page identifies current scholarship holders specifically as **2026**: Francesco Giosuè, Rébecca Mathiot, Giulio Piumelli and Aesa Virely. Its English equivalent omits the year. Search results exposed an older version naming David Todd and a different doctoral cohort; opened body text now identifies Jonathan Levy. Prefer the opened page, retain the cached discrepancy in coverage, and do not infer award amounts from the 2027 ceiling.

Excluded examples: the [History Project](https://histproj.org/) acknowledges INET support, but its Paris navigation link does not establish a Paris funding allocation; [SEATIDE, agreement 320221](https://cordis.europa.eu/project/id/320221/reporting), was a 2012–2016 Cambridge-linked consortium, not a CHEP Paris grant. Its total must not enter this ledger. The Belonging event’s ERC Lubartworld co-support likewise does not make the whole ERC award CHEP income.

## Source tree and retrieval limits

```text
Paris home (retrieved indexed)
├── EN projects (406; www alias cache miss)
├── FR /fr/projets.html (retrieved; indexed crawl 2.6 years old)
│   ├── EHC / Harvard (retrieved)
│   ├── Archives Notariales (retrieved; page dated May 2021)
│   └── Slavery / Cambridge (403)
├── recent events 2019–2026 (all displayed entries read)
│   ├── Emotions/climate (retrieved; explicit funding)
│   ├── Belonging (retrieved; support only)
│   ├── Ottoman world (retrieved; no funding statement)
│   └── Spatial launch (retrieved; no funding amount)
└── robots.txt / sitemap.xml (retrieval unavailable)
Sciences Po
├── CHEP EN and FR (retrieved; variant differences preserved)
├── 2020 scientific council minutes §10 (text retrieved)
├── 2022 FNSP board minutes + two Institute minutes (text retrieved)
├── 2022 research annual report (search lead only; target unavailable)
├── 2023 research annual report (CHEP sections retrieved)
└── Junior colloquium + 2024 currency conference + 2025 programme (retrieved)
Cambridge historical CHEP root/index (cache miss/inaccessible)
Harvard research/news/EHC (retrieved; network boundaries preserved)
External targeted databases: CORDIS/ANR searches (no Paris institutional award found)
```

No automated bulk crawl was performed: robots/sitemap retrieval failed, shell DNS was unavailable, and browser search/open was used at ordinary rates. Several retrieved pages explicitly exposed indexed crawl ages; these are not site publication dates or independently live-tested states. PDF screenshots for the 2020 and three 2022 minutes failed with cache misses; readable full relevant page text was inspected. The PDF skill was read and applied to read-only inspection; no PDF output was created. Raw documentary wording about finance is retained in notes only to the minimum necessary.

This is a bounded public-source survey, not a complete financial history. Funding coverage records distinguish findings from support-only leads. Pending: Cambridge historical project and slavery pages; original 2019/2020 agreements; full 2022 and other annual reports; every event’s full programme rather than the checked funding-bearing subset; exact funder award agreements; and a transaction-level reconciliation of the 2022 receipt and restricted-fund accounting. Internal finance records, selection decisions and disbursement reports are necessary to establish amounts, exact cohorts, spending and restrictions.

## Safe annual-report material and next records

A short narrative can document doctoral mobility selections, a 2022 Harvard contribution, and two later funded scholarly meetings without a financial total. Student work can reconcile those concrete records before attempting a budget history. Request (as a draft, not sent): the Harvard agreement and receipt date/amount; the 2022 restricted-funds accounting note; the 2020 doctoral selection and payment list; funding decisions and final accounts for the two funded events; and any earmarking linking upstream receipts to downstream awards. Unknown is not zero.
