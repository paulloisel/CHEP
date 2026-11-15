# P08 corpus, coverage and research decisions

as_of_date: **2026-11-15**. All web accesses in this package occurred on 15 November 2026. Browser retrieval often returned indexed/cached representations, with crawl ages noted in [sources.csv](sources.csv). Those ages are not source publication dates or proof of a live-site defect.

## Corpus and boundaries

Read the complete Shared research brief and P08 in `prompts_proposal.md`, plus nonempty `Summary.md` (the four starting URLs, no further research notes). Executed P08 only, independently of P01–P12 reports. No other report was required or used. All new files are inside `reports/P08_symposium/`; prompts, Summary and other workstreams were not edited.

The research covers a purposeful Paris-centred set of official profiles, research descriptions, publication abstracts/introduction material, and recent calendars. Calendar focus: 2025–2026 and announced 2026–27 activities. Earlier material is included for a specific research/format connection: Archives Notariales (May 2021), the notarial article (2022), capital-mobility article (online 2021/issue 2022), and historical programme context. Institutional dates 2019 and 2022 are separately retained. No claim of a comprehensive event, membership, publication or funding census is made.

Counts in the final package:

- **61 unique URLs in sources.csv**: 41 returned underlying-page content (including stale/partial content), one supplied indexed event text only (P08-PS20), and 19 failed/unsupported retrieval routes (P08-X01–19).
- Nine calendar evidence records (P08-CAL-S01–09), plus the Virely programme and Balguy indexed-event lead in participant research. Sources are not counted as unique events.
- **Three concepts**, **one detailed half-day pilot**, one smaller fallback, and cost comparisons for local one-day and four-European-visitor versions.
- **15 participant/role/partner records**: ten named people, one unnamed student role, four prospective institutions/programmes. Ancillary evidence on Giosuè and Virely informs alternative fit and overlap checks; they are not additional invitations.
- Four repeated participant-note source IDs are mapped to canonical records in [source_id_aliases.csv](source_id_aliases.csv). Duplicate URL evidence is not treated as independent corroboration.

No overall coverage percentage is given: the full population of relevant internal events and researchers is unknown.

## Task-specific source tree

Status key: **R** underlying content returned; **P** partial/indexed only; **F** failed retrieval; **O** observed branch, outside this purposeful corpus. Every R/P/F source below has a direct URL in the register or linked supporting notes. Access date for this tree: 2026-11-15.

- Paris overview: [EN](https://histecon.fr/en/) **R**, [FR](https://histecon.fr/fr/) **R**, [FR index alias](https://histecon.fr/fr/index.html) **R, old state**, [supplied EN index](https://histecon.fr/en/index.html) **F**.
  - [Organisation](https://histecon.fr/en/organisation.html) **R**: Coordinator and support-function terminology.
  - [People](https://histecon.fr/en/people.html) **R**: navigation inspected.
    - [Fellows](https://histecon.fr/en/research_fellows.html), [Associates](https://histecon.fr/en/research_associates.html), [Students 2026](https://histecon.fr/en/research_students.html), [Visitors](https://histecon.fr/en/research_visitors.html) **R**.
    - Student profiles → [Giosuè](https://histecon.fr/en/Francesco_Giosue.html) **R**; Mathiot/Piumelli CHEP routes **F**, newer CHSP profiles **R**. A Virely CHEP route also failed during supporting research; the verified CHSP profile was used.
    - Executive committee/former fellows/previous students **O**; not necessary for the ten selected candidates. No claim that these categories were exhaustively inventoried.
  - [Publications](https://histecon.fr/en/publications.html) **R**: selective work discovery only.
    - Lemercier/Trivellato and Cordelli/Levy publisher records **R**, abstract/introduction or abstract inspected; article dates preserved separately.
    - Rude DOI endpoint **F**; official author metadata supports topic only, not a full-text interpretation.
  - [EN Projects](https://histecon.fr/en/projects.html) **F**; [FR Projets](https://histecon.fr/fr/projets.html) **R, old state**.
    - [Archives Notariales](https://www.histecon.fr/archivesnotariales/) and [Colonies et Consulats](https://www.histecon.fr/archivesnotariales/colonies.html) **R**; resources subpage **F**. Navigation includes acts, repertories, control and registration; no full archival holdings crawl or reproduction-rights determination.
    - Joint [environment programme](https://histecon.fas.harvard.edu/ehc/) **R**; selective people/work links inspected, not all programme outputs attributed to Paris.
  - CHEP events/seminars index routes EN and FR **F**; [Recent Centre Events](https://histecon.fr/en/events_recent.html) **R**.
    - Linked JCHE/CHEP workshop, New Paths and Climate/Capitalism detailed pages **F**. No full programme or linked PDF could be verified through these routes.
    - [Regional agenda](https://histecon.fr/fr/agenda.html) **R**, entries through spring 2025 in retrieved state.
  - [robots.txt](https://histecon.fr/robots.txt) and [sitemap.xml](https://histecon.fr/sitemap.xml) **F** via browser tool. No automated bulk crawl was undertaken; source requests were targeted.
- Sciences Po [CHEP overview](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) and [alternate route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) **R**.
  - CHSP/CSO newer directory profiles and School of Research award notice **R**; public research interests and affiliation categories only.
  - [Events index](https://www.sciencespo.fr/histoire/en/events/) **P**: navigation/three-page pagination present, no event cards in extraction. Full pagination content was not verified.
  - Targeted searches → Histoires de la vie économique, La matière du politique, Mondes soviétiques programmes **R**; LIEPP planning workshop **R**; Balguy source seminar **P**, direct open failed.
  - Regional agenda → [PSE economic-history seminar](https://www.parisschoolofeconomics.eu/fr/recherche-academique/vie-academique/seminaires/histoire-economique/) **R, stale 2024 state**.
- Harvard [home](https://histecon.fas.harvard.edu/) **R**; events navigation → [upcoming index](https://histecon.fas.harvard.edu/events.htm) and [graduate workshop](https://histecon.fas.harvard.edu/graduate_workshop.html) **R**. Sparse index is not evidence of inactivity.
- Cambridge [home](https://www.histecon.magd.cam.ac.uk/) **F, 403** and [historical Paris project](https://www.histecon.magd.cam.ac.uk/chep/) **F, cache miss**. Other official Paris/Harvard pages support the limited network claims used here.

Searches were used to locate official material rather than as independent evidence: CHEP projects, fellows, students, events; CHSP/CHEP workshops; planning; named-candidate profiles and source seminars. Detailed search findings and locator notes are preserved in [calendar_research.md](calendar_research.md) and [participant_research.md](participant_research.md).

## Reconciliation and evidence statuses

1. **Verified in inspected official representations:** Coordinator is the supported title for Jonathan Levy. Earlier Lemercier co-coordination is historical (2019–2021), not a current role. Students are explicitly the 2026 cohort. Recheck all affiliations before any future event.
2. **Conflicting retrieval states:** home aliases and search results show different announcements. A French index retrieval displayed April 2024; other representations showed a July 2026 State and Capital banner or no banner. These are possible cache/version differences. The July banner remains a lead, not a current-calendar finding or proof an event occurred.
3. **Differences in roster coverage:** the Sciences Po overview includes Joan Chaker, whereas the retrieved CHEP fellows page foregrounds Balguy. This does not establish that Chaker left. He is not assigned a candidate role requiring reconciliation here.
4. **Calendar date conventions:** a year inferred from a 2026–27 academic heading is labelled inferred; future programme entries are announcements. Retrospective descriptions do not establish attendance or impact. The environment programme contains “12–13 November 2006” next to a current infrastructure announcement; that date is not used or silently corrected.
5. **Inferred:** candidate fit, comparative connections, expected community benefit, planning costs/hours and the choice of C1. **Unverified:** demand, willingness, present local availability, shareable dossiers, actual access needs, venue charges and fee policy. Emelyn Rude’s old profile is explicitly insufficient for a current appointment claim; Parrinello has a newer profile cross-check.
6. **Metadata decisions:** preserve the capital-mobility article’s September 2021 online date and May 2022 issue date. Publication inclusion is not proof of CHEP funding. No grant amount is used to finance the proposal.

## Exclusions, remaining queue and internal questions

The funding ledger, current opportunity directory, full governance census, public-communication audit and anniversary project are other workstreams and were not executed. No newsletter subscription, registration, invitation, publication, application or external message occurred. No personal contact details were collected. Broader partner memberships, demographic attributes and willingness were not inferred.

The practical stopping point was sufficient verified fit for three differentiated concepts and an auditable conditional pilot. Remaining retrieval work is explicit: re-open CHEP seminar/event routes and linked programmes; locate a current PSE calendar; recover Cambridge pages through permissible official routes or dated archives if history becomes relevant; verify Balguy’s January 2026 announcement directly; check for any relevant public PDF programme surfaced in those branches. No unavailable PDF is treated as read. Archive snapshots were not needed for the limited historical claims used and were not retrieved.

Internal questions determine implementation: Is the comparison useful and distinct from existing sessions? Do the proposed presenters want it and have permission to share appropriate extracts? Can an academic convenor and administrative/access functions contribute the stated hours? Does the student genuinely have this allocation? What are venue, purchasing and fee rules? Would an existing seminar prefer the smaller session? Public pages cannot answer these questions.

## File status and estimate precedence

[report.md](report.md), [concepts.md](concepts.md), [pilot_programme.md](pilot_programme.md), [participants.csv](participants.csv), [budget_and_workplan.csv](budget_and_workplan.csv), this coverage note and [sources.csv](sources.csv) are the final P08 deliverables. Supporting research notes retain their original local IDs; use the alias CSV to reconcile them.

[feasibility_review.md](feasibility_review.md) records the independent audit. Final cost arithmetic follows that audit. Final expanded labour uses explicit points within its indicative ranges: local day 45 student/55 other hours; European extension 65/95, with 35 experienced-organiser hours included in the latter's other total. They are alternatives, not amounts to add to the pilot. Optional catering rows are incremental to the lean pilot. Unknown cash rows are always excluded from modelled subtotals. Source/proposal validation checked CSV structure and references, arithmetic, weekly capacity, internal file links and absence of confirmed-participation claims; it does not establish external feasibility.
