from pathlib import Path
import json,csv,collections
p=Path(__file__).resolve().parent.parent
v=json.loads((p/'validation.json').read_text())
sources=list(csv.DictReader((p/'sources.csv').open()));ledger=list(csv.DictReader((p/'funding_ledger.csv').open()));cohort=list(csv.DictReader((p/'cohort.csv').open()))
counts=collections.Counter(r['relationship_category'] for r in ledger)
fails=[r for r in sources if any(w in r['retrieval_status'].lower() for w in ['failed','unavailable','403','406','503','cache miss','cache_miss','timeout','lead_only','indexed_only'])]
s=f'''# P03 — Coverage, source tree and reconciliation

**as_of_date: 2026-11-15.** Research cutoff and access date use the client date. `Summary.md` was nonempty and supplied the four expected Paris, Sciences Po, Harvard and Cambridge starting URLs. The shared brief and P03 were applied. Other reports were not dependencies. This file describes the checked corpus, not the universe of CHEP finances.

## Counts and boundaries

- **{v['cohort_records']} distinct people** in `cohort.csv`, including two administrative/web support functions retained for boundary clarity. Categories overlap; these are not {v['cohort_records']} current members.
- **{v['ledger_records']} ledger rows**, including **{v['component_records']} beneficiary components** of one project. A row is not necessarily a separate grant: records include an institutional receipt, an approximate cohort aggregate, appointments, prizes and explicit funding acknowledgements.
- Relationship rows: {counts['incoming_institutional_project_funding']} incoming institutional receipt; {counts['CHEP_administered_or_distributed_support']} CHEP-administered/distributed support; {counts['independent_awards_to_CHEP_connected_researchers']} independent connected-researcher records (including linked components).
- **10 named CHEP doctoral award records**: Hugo Carlier (2022), Leonard le Roux (2022–23), four recipients in 2025 and four in 2026. This is not an all-time recipient count. Four named 2020 exchange selections remain distinct from the approximate six-bursary aggregate and are not added to it.
- **{v['lead_records']} call/lead/accounting rows**, **{v['source_records']} exact-URL source records**, and **{v['coverage_records']} coverage rows**. Identical URLs were deduplicated from {v['original_source_ids']} original source IDs; `source_id_crosswalk.csv` preserves the mapping. Different aliases/language routes remain separate retrievals, not independent corroboration.

The core period is 2019–2026-11-15. Earlier member awards are labelled `earlier_independent_award`; approximate pre-2019 Paris activity in 2020 minutes is retained as unresolved prehistory. The 2027 studentship call is documented as a future-cycle call only. No all-time coverage percentage or monetary aggregate is calculated because the relevant population and accounting denominator are unknown.

## Task-specific source tree

`R` means an underlying source was opened, normally as indexed/cached text. `F` means retrieval failed. `I` means indexed evidence only, insufficient for a verified ledger claim where marked. None of these labels independently proves the live site's state.

- **Paris starting point and chronology**
  - [English home](https://www.histecon.fr/en/) — R; [Summary route](https://histecon.fr/en/index.html) — F, 406.
  - [French home](https://histecon.fr/fr/index.html) — R, old cached rendition; 2019/2022 chronology agrees with English.
  - [5 June 2019 launch workshop](https://histecon.fr/en/spatial.html) — R; launch event, no funding figure.
  - [robots.txt](https://histecon.fr/robots.txt) and [sitemap.xml](https://histecon.fr/sitemap.xml) — F; no automated crawl undertaken.
- **Paris people branches: independent funding cohort**
  - [People](https://histecon.fr/en/people.html) → [Organisation](https://histecon.fr/en/organisation.html) — R.
  - [Associates EN](https://histecon.fr/en/research_associates.html) / [FR](https://histecon.fr/fr/chercheurs_associes.html) — R; same 20 names.
  - [Fellows](https://histecon.fr/en/research_fellows.html) / [past fellows](https://histecon.fr/en/research_fellows_past.html) — R; one displayed current fellow and three past fellows. Host roster supplements this, without inventing employment terms.
  - [Research students 2026](https://histecon.fr/en/research_students.html) — R; [previous students](https://histecon.fr/en/research_students_previous.html) — F including alias.
  - [Visitors](https://histecon.fr/en/research_visitors.html) / [graduate visitors](https://histecon.fr/en/visiting_graduate_students.html) — R; individual periods retained.
  - [Executive committee](https://histecon.fr/en/executive_committee.html) — F including alias; 2020 council minutes recover historical names only.
  - Linked official profiles, selected public CVs and funder notices — per-person searches and gaps in `funding_coverage.csv`; no automatic import of whole partner rosters.
- **Paris funding, projects and acknowledgements**
  - [Research grants](https://histecon.fr/en/research_grants.html) — R, 2027 call. [French Bourses](https://histecon.fr/fr/bourses.html) and www alias — F.
  - [2025 postdoctoral call](https://histecon.fr/en/fellowships2025/fellowships.html) / [2026 call](https://histecon.fr/en/fellowships2026/fellowships.html) — R, closed cycles; [French fellowship page](https://histecon.fr/fr/fellowships.html) — I/F timeout. [2023 republication](https://hdoisto.gr/en/news/922/) — R secondary, original still needed.
  - [Announcements archive](https://histecon.fr/en/announcements_archive.html) — R; prizes and Lviv support followed to responsible institutions.
  - [English projects](https://histecon.fr/en/projects.html) — F; [French projects](https://histecon.fr/fr/projets.html) — R, historical cached content.
  - [Archives Notariales](https://www.histecon.fr/archivesnotariales/) — R, hosting; [Slavery and French Economic Life](https://www.histecon.magd.cam.ac.uk/slavery/index.html) — F; group support verified through French projects.
  - [Recent events](https://histecon.fr/en/events_recent.html) — R, displayed 2019–2026 entries read; funding-relevant programme subset followed, not every event PDF.
  - [Emotions/climate workshop](https://histecon.fr/emotions_climate_environment/index.html) and [Invisible Actors programme](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2025-11-27ET28-INVISIBLE-ACTORS-VERSION5.pdf) — R, explicit funding. Other generic support mentions retained as leads.
- **Host institution and public financial evidence**
  - [CHEP EN](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) / [FR](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/) — R; alternate EN route checked; opened contents take precedence over older search snippets.
  - [2025 awards](https://www.sciencespo.fr/ecole-recherche/fr/actualites/quatre-doctorants-du-centre-d-histoire-laureats-de-la-bourse-d-excellence-du-chep/) / [2026 awards](https://www.sciencespo.fr/ecole-recherche/en/news/four-young-history-researchers-chep-2026-grant/) — R, dated recipient announcements. [Newsletter index](https://www.sciencespo.fr/ecole-recherche/fr/newsletter/) checked for award discovery; all historic issues were not audited.
  - [10 March 2020 council minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2020/2020_03_10_CSFR.pdf) — R text; validated 2 June 2020; governance and approximate bursary cohort.
  - [19 October 2022 FNSP minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/ca/2022/PVCA20221019.pdf), [6 December](https://www.sciencespo.fr/sites/default/files/cd_cp/ci2022/PVCI20221206.pdf), [13 December](https://www.sciencespo.fr/sites/default/files/cd_cp/ci2022/PVCI20221213.pdf) — R text; screenshot cache misses recorded.
  - [2023 research report](https://www.sciencespo.fr/recherche/sites/sciencespo.fr.recherche/files/SciencesPo_RA2023-2_0.pdf) — R relevant CHEP passages; 2022 full-report target failed. Other annual reports remain a retrieval queue.
- **Connected programmes and external verification**
  - [Harvard research](https://histecon.fas.harvard.edu/research_main.html) / [news](https://histecon.fas.harvard.edu/news.html) — R; only demonstrable Paris connections followed.
  - [Economic History, Climate, and the Environment](https://histecon.fas.harvard.edu/ehc/) — R; Richards support is acknowledged, but financial nature and Paris allocation unverified.
  - [Historical Cambridge Paris project](https://www.histecon.magd.cam.ac.uk/chep/) — F plus alternate route; Harvard EHP programme lists and Paris-linked individual profiles retrieved (exact URLs in sources).
  - [CORDIS 819353](https://cordis.europa.eu/project/id/819353), [CORDIS 295817](https://cordis.europa.eu/project/id/295817), [ANR TOFLIT18](https://anr.fr/Projet-ANR-13-BSH1-0005), [ANR SOSELF](https://anr.fr/Projet-ANR-21-CE26-0022) and institutional award notices — R; awards attributed to legal recipients and connected researchers, not CHEP automatically.
  - Lviv annual report and fellowship pages; EHA, AHA, ECPR and other responsible prize institutions — inspected as recorded in sources. Project acknowledgements and personal CVs are identified as such.
  - Wayback CDX discovery for the grant page — F; **no authenticated historical snapshot retrieved**. Crawl ages are not snapshot dates.

## Years checked and substantive gaps

| Period | Public evidence checked | Limit |
|---|---|---|
| Earlier member awards | Explicit dated entries in selected CVs, ERC/funder and host records | Illustrative historical expansion, not lifetime census; does not establish CHEP involvement at award time |
| 2019 | Launch page, host chronology, partner news and targeted funding searches | No 2019 institutional award amount recovered |
| 2020 | Council minutes; four selected exchanges; cofinancing; planned postdocs | Approximately six awards cannot be reconciled with four named selections; completed travel/payments unknown |
| 2021 | Paris-linked CHEP-EHP fellows; graduate visitors; project support | Fellowship titles do not establish payer or individual amounts |
| 2022 | Harvard receipt/accounting; Lviv; Carlier; Le Roux multi-year record | Grant agreement and disbursements absent |
| 2023 | Appointments, Le Roux period, annual-report context; postdoctoral call republication | No complete annual doctoral cohort or centre budget |
| 2024 | Explicitly funded workshop; fellowship call; research/prize records | No year-specific CHEP doctoral award cohort recovered; no inference of zero |
| 2025 | Four doctoral awards; conference cofunding; fellowship/visitor evidence | Amounts and actual appointment terms unknown |
| 2026 to 15 November | Four doctoral awards; current rosters; project notices; closed postdoctoral call | No completed-year finance statement; later dates not assumed |
| 2027 | Official studentship call only | Future support is not historical award or expenditure |

Queries included grant/bourse/studentship terms on `histecon.fr` and `sciencespo.fr`, exact centre-name fellowship searches, annual-cycle checks and name-plus-grant/fellowship/ANR/ERC searches. The core associate roster was searched person by person. Support staff were checked for their public functions, not their personal awards. Coverage is explicit about shorter searches, failed profiles and remaining CV extraction.

## Conflicts and consequential decisions

1. **Current versus indexed roster:** an older search result for the host page names Todd and the 2025 cohort; opened content names Levy and the 2026 cohort. This is not sufficient evidence of a live French/English contradiction. Historical Todd evidence is separately dated.
2. **Appointment periods:** Le Bras and Hewitt have three-year position announcements in 2023 that do not align with abbreviated past-fellow roster years. Retain appointment evidence; leave contractual start/end unresolved. Skoglund's programme cohort, thesis and Paris-stay dates likewise do not justify invented payment periods.
3. **SLAVEVOICES:** retain CORDIS end 2027-08-31 provisionally; Sciences Po ERC register says August 2028. Mark all three linked ledger rows conflicting for period, while amounts remain verified. Earlier 2019–23 publicity is an original plan, not a current end date.
4. **SHIFTING SHORES:** 2018 award/original funding through 2022 versus retrospective 2019–24 activity. Do not collapse these into a single verified funding interval.
5. **2020 aggregate:** keep approximately six bursaries distinct from four named selections. No automatic parent link or total of ten.
6. **€0.9m accounting:** retained in leads as a verified accounting observation, not an award; exact association to the Harvard receipt is unproven. Richards support remains non-quantified and financially unverified.
7. **Recognition versus funding:** *Femmes en tête* has conflicting descriptions as a prize versus portrait selection. Keep outside the monetary award ledger. Other prizes are not cash receipts without evidence.
8. **TRADEDEPRESSION:** project/amount and an O’Rourke ERC award are separately documented; exact attribution uses a primary indexed notice whose underlying page failed. Retain `inferred`, with no verified-attribution total.
9. **Event dates:** *Invisible Actors* archive gives 26–27 November 2025; final linked programme gives 27–28. Use the programme dates and record the conflict. No attendance or event expenditure inferred.

## Exclusions, practical stopping boundary and next steps

Excluded: unrelated CHEP acronyms; other Sciences Po awards without a Paris connection; entire Harvard/Cambridge populations; general salaries; honorary or declined fellowships; future unannounced calls; and INET/History Project or SEATIDE funding with no demonstrated Paris allocation. Hosting and collaboration alone are not cash support.

This run reached the core source-map branches and per-person first-pass searches, then followed identified high-value financial records and dated recipient leads. It stops at the documented access and evidence boundary: historical committee/student pages, several award databases/profiles, remaining deep CV entries and unreviewed annual reports. The lead table is the explicit remaining queue, not a claim that those awards did not occur.

Next public retrieval priorities: the previous-student archive; Joseph la Hausse de Lalouvière’s British Academy notice; Lucile Truffy’s 2026 archival award; Giosuè’s IdEx profile; Iyamu’s scholarships; LOGE beneficiary attribution; Delalande/Lazarus project dates; dated original 2023 fellowship call; remaining annual financial reports. Amount-only leads (e.g. Yates's reported prize amount) must remain separate from already verified award existence. Internal records are required to establish legal CHEP funding arrangements, donor restrictions, paid amounts, beneficiary reimbursements, grant-to-distribution links and publication clearance. See `administrator_questions.md`.

## Retrieval failures and partial evidence

The following {len(fails)} source-register rows include failures, inaccessible targets or indexed-only qualifications. Some also have readable text or another successfully retrieved rendition; status strings preserve that distinction. Repeated failures were not treated as website defects.

| Source ID | Source | Retrieval qualification |
|---|---|---|
'''
for r in fails:
 s+=f"| {r['source_id']} | [{r['title']}]({r['url']}) | {r['retrieval_status'].replace('|',';')} |\n"
s+='\n## File verification\n\nCSV encoding/structure, unique IDs, source references, parent references and person references were checked. The two SLAVEVOICES components sum to the parent exactly. All monetary aggregation beyond that within-project reconciliation is intentionally absent. `validation.json` records the final counts and check results. Intermediate evidence and reproducible assembly scripts remain in `_research/`; the files in this directory root are the authoritative deliverables.\n'
(p/'coverage.md').write_text(s)
