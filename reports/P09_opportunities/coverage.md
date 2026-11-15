# P09 — Coverage, source map and decisions

**as_of_date: 2026-11-15; client timezone: America/Los_Angeles.** Verification instant used for deadlines: **2026-11-15T23:09:45Z**. Source access dates are in [sources.csv](sources.csv). A source's publication date, the opportunity's cycle/award period and the web tool's crawl date are separate fields or notes; none substitutes for another.

## Corpus and counts

This is a **focused prospective funding directory**, not a worldwide census and not P03's historical ledger. The intended applicants are CHEP-associated Master's students, early and advanced doctoral students, postdoctoral researchers and other affiliates. Sciences Po enrolment/employment, nationality, citizenship, residence, society membership and available leave are never presumed. Historical rounds are included only when useful for a clearly labelled monitoring decision or exclusion.

- **24 distinct scheme records** in [opportunities.csv](opportunities.csv): 12 open; four upcoming with an officially announced date; four recurring but next round unannounced; three closed; one unverified. The 12 open records include a standing Erasmus administrative route and an EHS conditional attendance-bursary route with no published bursary deadline. They are not 12 universally accessible competitions.
- **86 unique URL records** in [sources.csv](sources.csv), including unsuccessful retrievals and discovery/exclusion evidence. This is a count of URLs checked or attempted, not 86 independently confirmed live calls.
- Evidence labels on opportunities: **19 verified**, **five conflicting**. “Verified” means the cited scheme terms were inspected, not that every applicant-specific fact is settled or every field is published. The five conflicting records are CIERA student mobility O005–O007, EHS/IHR O021 and EHA O024.
- **20 conditional shortlist rows** cover all five profiles. Ranking is an analytic inference from documented gates, relevance, cost purpose, preparation burden and deadline readiness; it is not an acceptance forecast.
- Coverage spans research travel, archive access/reproduction and other research expenses; conference attendance; language learning within CHEP; subsidised methods training; residential fellowships; and small collaborative meetings. Pure living-cost/admission scholarships and retrospective prizes are outside the main directory.

Variants with materially different stages or funding bases remain separate: CIERA Master's/complete doctoral/partial doctoral/young doctors; Newberry short/long term; Hagley exploratory/extended research. Named endowments inside a single general competition were not multiplied into extra entries. No known repeated opportunity is counted twice. Repeated source URLs were consolidated; [id_crosswalk.csv](id_crosswalk.csv) maps the component research IDs and source aliases to the final tables.

## Task-specific source tree

Statuses below describe retrieval in this run, not a general website-health verdict. All listed sources were accessed or attempted on 15 November 2026. Full titles, owners, dates and supports are in the register.

### CHEP / Sciences Po context and local funding

- [CHEP English home](https://www.histecon.fr/en/) — retrieved, indexed crawl reported five months earlier; host context corroborated by Sciences Po (SR03).
  - [French home](https://histecon.fr/fr/index.html) — retrieved older cached/indexed rendition, crawl reported 2.6 years earlier; used for navigation only (SR05).
  - [Supplied English index route](https://histecon.fr/en/index.html) — 406 retrieval failure (SR06).
  - [Organisation](https://histecon.fr/en/organisation.html) — retrieved; Jonathan Levy labelled Coordinator (SR02).
  - [Grants, English](https://histecon.fr/en/research_grants.html) — inspected 2027 call and application/reference dates (SR01).
    - [French grants](https://histecon.fr/fr/bourses.html) — failed retrieval; [www alias](https://www.histecon.fr/fr/bourses.html) search index exposed closed 2026 text, direct open failed (SR08, SR18).
    - [English www alias](https://www.histecon.fr/en/research_grants.html) — failed retrieval (SR10).
    - [Linked application portal](https://histecon.fr/fr/bourses_portail.html) — 406; [www alias](https://www.histecon.fr/fr/bourses_portail.html) also failed; functionality unverified (SR09, SR19).
  - [Announcements archive](https://histecon.fr/en/announcements_archive.html) — retrieved; awards/recipient announcements not treated as open calls (SR11).
  - [Sitemap attempt](https://histecon.fr/sitemap.xml) — not accessible through tool; existence unverified (SR07).
- [Sciences Po CHEP host page](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) and [alternate route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) — both retrieved; agree on role/host context (SR04, SR20).
  - [Funding directory](https://www.sciencespo.fr/ecole-recherche/fr/carrieres/financements-appels-en-cours/) — retrieved; [linked public table](https://docs.google.com/spreadsheets/d/e/2PACX-1vTCLCGdBOSV-RNY3_OsJ0HShwqSNAUQtBdTb7d-ugN_Vf15gFLoRM4Gr6VlztSPbBeluEGrK-vbH_-k/pubhtml?gid=0&single=true) yielded title only (SR14–15).
  - [Doctoral funding](https://www.sciencespo.fr/ecole-recherche/fr/admissions/doctorat/doctorat-droits-scolarite-aides-financieres/) — retrieved; standing exceptional fund, exact next round absent (SR16).
  - [2025–26 CHSP doctoral guide PDF](https://www.sciencespo.fr/histoire/files/Guidedoctorant2025-2026-15sept.pdf) — text retrieved, nine pages; historical contextual lead, not current amount authority (SR17).
  - [Erasmus+](https://www.sciencespo.fr/students/fr/financer/bourses-aides-financieres/programme-erasmus-plus/) → [2026–27 rate PDF](https://www.sciencespo.fr/students/sites/sciencespo.fr.students/files/sciencespo-decision-fixation-taux-financement-erasmus-plus-en.pdf) — both retrieved (SF01–02).
  - [Doctoral mobility](https://www.sciencespo.fr/ecole-recherche/fr/formations/doctorats/programmes-echanges/) — retrieved, Erasmus spring-2027 call and CamPo branch checked (SF03).
  - [International mobility](https://www.sciencespo.fr/students/fr/financer/bourses-aides-financieres/aides-mobilite/) and [MENA fieldwork call](https://www.sciencespo.fr/mena/fr/actualites/appel-a-candidature-pour-le-soutien-a-la-mobilite-des-etudiant-e-s-realisant-un-memoire-de-master-sur-la-region-afrique-du-nord-moyen-orient-mena/) — retrieved; dated student rounds closed (SF19–20).
  - [Eiffel English](https://www.sciencespo.fr/students/en/fees-funding/bursaries-financial-aid/eiffel-scholarship/) / [French](https://www.sciencespo.fr/students/fr/financer/bourses-aides-financieres/bourse-eiffel/) — retrieved, consistent 2027 institutional non-participation (SR12–13).

### French/European external routes

- [CIERA home](https://www.ciera.fr/fr) → [mobility programme](https://www.ciera.fr/fr/programme-mobilite) — retrieved (SF14–15).
  - Current French calls: [Master's](https://www.ciera.fr/fr/manifestation/12189), [complete doctoral](https://www.ciera.fr/fr/manifestation/12187), [partial doctoral](https://www.ciera.fr/fr/manifestation/12188), [young doctors](https://www.ciera.fr/fr/manifestation/12975) — retrieved; spring 2027 sections checked (SF04–07).
  - [Eligibility FAQ](https://www.ciera.fr/fr/node/12977), [dossier guidance](https://www.ciera.fr/fr/node/12978) — retrieved; differences preserved (SF08–09).
  - [Master's English-route version](https://www.ciera.fr/en/node/12189) — older rendition with deadlines through autumn 2026; current French call used for future date (SF16).
  - [Methods workshop](https://www.ciera.fr/fr/manifestation/24827), [junior call](https://www.ciera.fr/fr/manifestation/24218), [junior programme](https://www.ciera.fr/fr/colloques-juniors), [member network](https://www.ciera.fr/en/reseau-partenariats) — retrieved (SF10–13).
  - [Réseaux et terrains](https://www.ciera.fr/fr/reseaux-terrains) — retrieved, no exact next deadline verified; excluded lead (SF17).
- [Alliance doctoral mobility](https://alliance.columbia.edu/alliance-call-doctoral-mobility) — retrieved; conflicting cycle wording against Sciences Po, excluded pending resolution (SF18).

### Archives and libraries

- Newberry: [short-term](https://www.newberry.org/research/fellowships/short-term-fellowships) → [long-term](https://www.newberry.org/research/fellowships/long-term-fellowships) → [instructions](https://www.newberry.org/research/fellowships/how-to-apply) → [FAQ](https://www.newberry.org/research/fellowships/faq): all retrieved; 2027–28 cycle, separate referee dates and degree thresholds checked (SA01–04).
- Hagley: [overview](https://www.hagley.org/research/grants-fellowships?language=en) → [exploratory](https://www.hagley.org/exploratory-research-grants) / [du Pont](https://www.hagley.org/henry-belin-du-pont-research-grants): retrieved; no dated next round, so standing annual dates remain off the live calendar (SA05–07).
- Huntington: [programme](https://www.huntington.org/research-and-fellowships/fellowships-program) → [awards](https://www.huntington.org/research-and-fellowships/available-fellowships) → [FAQ](https://www.huntington.org/research-and-fellowships/fellowship-faqs) → [public portal](https://fellowships.huntington.org/): retrieved; no login; short-term 2027–28 route checked (SA08–11).
- EUI HAEU: [Sørensen programme](https://www.eui.eu/en/academic-units/historical-archives-of-the-european-union/research-support/postgraduate-vibeke-soerensen-grant) → [dated 2026 call](https://www.eui.eu/news-hub?id=call-for-applications-the-vibeke-soerensen-grant-programme-2026&lang=en-GB): retrieved; next early-2027 announcement has no exact date (SA12–13).
- BnF: [2026–27 SciencesCall portal](https://bnfaac2026.sciencescall.org/) → [Hyman](https://bnfaac2026.sciencescall.org/page/bourse_hyman), [instructions](https://bnfaac2026.sciencescall.org/page/comment_deposer), [13-page regulation](https://bnfaac2026.sciencescall.org/data/pages/Reglement_de_l_appel_a_chercheurs_et_chercheuses_2026_2027.pdf): retrieved; regulation articles 6, 14, 22 and 23 checked; some pages labelled rewritten summaries by tool (SA14–17). [Research blog lead](https://bnf.hypotheses.org/54271) stopped at bot check, not bypassed (SA18).

### Societies and Harvard/Cambridge branches

- RHS: [postgraduate](https://royalhistsoc.org/research_funding/postgraduate-research-funding/pgr-research-support-grants/), [membership](https://royalhistsoc.org/membership/membership-postgraduate/), [international rules](https://royalhistsoc.org/research_funding/international-research-support-grants/), [ECR](https://royalhistsoc.org/research_funding/early-career-research-funding/early-career-research-support-grants/), [workshops](https://royalhistsoc.org/research_funding/workshop-grants/rhs-workshop-grants/): retrieved (SS01–05).
- EHS: [fellowship call](https://ehs.org.uk/award/economic-history-society-fellowships/) → [IHR portal](https://universityoflondon.smapply.io/prog/ihr_economic_history_society_fellowship_2027/); [posters](https://ehs.org.uk/conference/new-researcher-posters/); [UK-restricted graduate fund](https://ehs.org.uk/award/research-fund-for-graduate-students/): retrieved (SS06–08, SS12).
- EHA: [early-stage call](https://eh.net/early-stage-dissertation-grant/) / [form](https://eh.net/early-stage-dissertation-grants/), [graduate fellowship call](https://eh.net/graduate-dissertation-fellowships/) / [form](https://eh.net/graduate-dissertation-fellowship-application/), [Cole call](https://eh.net/arthur-h-cole-grants/) / [form](https://eh.net/cole-grant-application/): retrieved; future dates coexist with closed form text (SS10–11, SS21–24).
- Harvard CHE [home](https://histecon.fas.harvard.edu/) / [news](https://histecon.fas.harvard.edu/news.html) → [EHP home](https://histecon.fas.harvard.edu/ehppf/index.html), [programme](https://histecon.fas.harvard.edu/ehppf/about.html), [historical CHEP cohort](https://histecon.fas.harvard.edu/ehppf/chep_fellows.html), [Exchanges form](https://histecon.fas.harvard.edu/exel/exchanges_research_grant_application_2019.pdf): retrieved; no new Paris-eligible EHP call established (SS13, SS15–18, SS25).
  - [IRIS recruitment](https://academicpositions.harvard.edu/postings/16700) — retrieved independent external call (SS09).
  - [WIGH funding](https://wigh.wcfia.harvard.edu/funding) → [old job link](https://academicpositions.harvard.edu/postings/14102): mixed cycles; old link redirects to generic index (SS19–20).
- Cambridge [www home](https://www.histecon.magd.cam.ac.uk/) / [news](https://www.histecon.magd.cam.ac.uk/news.html) — 403; [non-www home](https://histecon.magd.cam.ac.uk/) — 502; [historical Paris branch](https://www.histecon.magd.cam.ac.uk/chep/) — cache miss (SS14, SS26–28). Retrieval failure does not establish the centre lacks opportunities.

## Consequential decisions and unresolved conflicts

1. **CHEP current cycle:** inspected English text explicitly announces 2027; search snippets and failed French retrieval expose older 2026 wording. The current dated English call controls this record. French parity and portal operation remain unverified. No claim that the live French website is broken or necessarily stale.
2. **CIERA:** French call body announces spring 2027 despite old page creation dates and autumn header. Calls require French enrolment plus six-month residence; FAQ adds one-year university enrolment. Preserve both, request clarification for an actual applicant, and mark student entries conflicting. Topic rules allow justified research-team integration as an alternative in the German-speaking-country route; the DAAD-centre route remains German-area-specific. Renewal is not an automatic consecutive extension.
3. **EHS/IHR:** both sources agree on 31 January 2027, but disagree between 11:00 and 11:59 GMT. The earlier time is a proposed conservative submission target, not a claimed resolution.
4. **EHA and WIGH:** future headings/dates do not override closed or mismatched application pages. EHA O024 remains unverified; other similarly conflicted leads are excluded from the main 24.
5. **Eligibility mappings:** Huntington says graduate students, not specifically French Master's degrees; the mapping remains explicit. Newberry ABD equivalence likewise requires applicant-level confirmation. RHS workshops do not explicitly confirm a Paris venue or postgraduate membership category. Published international recruitment at Harvard establishes an external route, not CHEP preference.
6. **Sørensen:** written rules exclude current EUI scholars, although a recipient listing includes an EUI affiliation. The rule governs prospective advice; no exception inferred. Huntington's differing approximate award counts were not used to estimate acceptance chances.

## Exclusions, remaining queue and internal-information needs

Excluded: Eiffel via Sciences Po in 2027; EHS UK-enrolment-only research support; CamPo as cash funding (its page explicitly says no dedicated funding); North-America-restricted Huntington travel awards; Newberry consortium-only variants without verified institutional access; unfunded BnF affiliation presented as a grant; historical prizes, recipient announcements and 2015–2021 joint-centre Exchanges funding; general admissions scholarships for students already enrolled. Closed MENA and international-mobility rounds were checked but not added merely to increase the inventory.

The focused search reached the 15–25 target with supported opportunities and all five profiles. It did **not** exhaust every visible BnF award, every archive or every European programme. Remaining queue, in order of practical benefit: obtain the public school table rows through an ordinary readable view; confirm CHEP portal and French parity; resolve CIERA/EHS/EHA conflicts; inspect Centre Jacques Berque's current Master's mobility call if a relevant applicant exists; follow IISH thematic fellowship leads; revisit Cambridge access and new EHP/WIGH calls; expand other BnF/European foundation branches only for demonstrated topic demand. No claimed coverage percentage is possible because the worldwide denominator is unknown.

Internal confirmation is needed for unpublished Master's support, current quasi-forfait doctoral allowances, reimbursement/advance rules, permissible cofunding, credited mobility approvals, real staff capacity and service demand. Nationality/residence/contract facts belong to individual applicants and were not collected. Suggested responsible functions are proposals, not documented assignments.

No bulk crawler was used: research used bounded targeted searches and individual official-page opens, so no automated site crawl required a robots-rule implementation. Public navigation, language variants, relevant linked PDFs and the available source branches above were checked; login-only pages, bot checks and failed fetches were not bypassed. Search snippets were discovery leads only, except the explicitly labelled old French snippet used to document a retrieval discrepancy. Raw component notes are retained for audit; the final CSVs, guides and this reconciliation note control the service prototype.
