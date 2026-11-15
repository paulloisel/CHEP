# P09 focused research: French and European routes

as_of_date: 2026-11-15 (America/Los_Angeles). Time-sensitive status cutoff: 2026-11-15T23:09:45Z, already 16 November 00:09:45 in Paris. Research only; no messages, registrations or applications sent. The shared brief, P09 and Summary.md were read. Other prompts were not executed.

The machine-readable contribution is [research_french_european.json](research_french_european.json). It contains eight opportunity records and 22 source records. All substantive source pages were opened, not merely copied from search snippets. Pages retrieved through the web tool frequently identify crawled/indexed versions; this is a limitation on claims of live portal availability. Current-cycle dates are explicit in the retrieved content. No page footer or crawl date was used to infer a call year.

## Findings and consequential choices

- **P09-OF01, Master's Erasmus:** the official [Sciences Po programme](https://www.sciencespo.fr/students/fr/financer/bourses-aides-financieres/programme-erasmus-plus/) provides an active administrative route for approved, compulsory, credited Master's mobility of at least two months. This is neither a general travel competition nor permission to fund an independent archive visit. The status `open` means that the published 2026–27 administrative procedure is active; individual processing deadlines and approved mobility remain applicant-specific. Funding rates were checked against the separate [2026–27 decision](https://www.sciencespo.fr/students/sites/sciencespo.fr.students/files/sciencespo-decision-fixation-taux-financement-erasmus-plus-en.pdf): the funded period is 89% of actual duration. Do not promise full-stay finance.
- **P09-OF02, doctoral Erasmus:** the [official doctoral mobility page](https://www.sciencespo.fr/ecole-recherche/fr/formations/doctorats/programmes-echanges/) sets a 15 November 2026, 23:59 Paris deadline. At the verification cutoff this was already past. The record is therefore **closed**, although the user-facing as-of date is still 15 November in Los Angeles. Its quoted amounts are total example grants, not monthly rates.
- **P09-OF03–06, CIERA research stays:** each current French call expressly lists 20 April 2027 at 12:00 for the spring round, covering stays beginning July–December 2027. Those dates are verified upcoming deadlines, not extrapolations. The opening date and time zone are not specified; stale “Candidatez” buttons alongside the closed autumn deadline are insufficient to call spring applications currently open.
- **CIERA eligibility conflict:** the current [Master's call](https://www.ciera.fr/fr/manifestation/12189) and doctoral calls require French higher-education registration and at least six months' residence before application. The [general FAQ](https://www.ciera.fr/fr/node/12977) additionally describes one year of French university registration. Neither rule should silently replace the other. Retain `conflicting` for these student records and ask the responsible institutional function to clarify before presenting a particular student as eligible. The young-doctor call has a separate, coherent French-degree-or-French-contract plus French-residence route.
- **P09-OF07, subsidised methods training:** the [21–22 January workshop](https://www.ciera.fr/fr/manifestation/24827) accepts Master's, doctoral and postdoctoral profiles, with 7 December 2026 application deadline. This is a verified currently open Master's-stage option, subject to CIERA registration, bilingual competence and selection. Paris residents receive no travel reimbursement under the published rule; listed subsistence benefits should not be described as a cash award.
- **P09-OF08, small collaborative activity:** the [autumn 2026 junior-conference call](https://www.ciera.fr/fr/manifestation/24218) is closed. Retain it for monitoring, not the live deadlines. An indexed CIERA social-media post mentioned a February 2027 call, but no exact new deadline was verified on the programme/call pages; no deadline was manufactured.

## Shared CIERA conditions and preparation

Source P09-SF08 states that CIERA mobility can combine with Université Franco-Allemande support, but cannot overlap with DAAD/OFAJ grants for the same period; Master's support may combine with social-criteria bursaries. A doctoral contract is why the partial doctoral variant exists. Unknown combination rules for other programmes remain unknown.

Source P09-SF09 advises requesting host/recommendation letters roughly one to one-and-a-half months before the deadline; the file must be complete by submission. Documents may be French or German, with host certificates also accepted in English. These are scheme rules, not a commitment to contact anyone.

Suggested **internal preparation milestones**, not funder deadlines:

- Training: by 23 November, test language/text fit and current CIERA registration; by 30 November, select and check the discussion text; aim for a final file by 4 December, ahead of the verified 7 December deadline.
- CIERA mobility: clarify residence/enrollment conflict before investing heavily; plan host and referee requests by early March; build work plan and project in March; use 16 April as an internal completeness check before 20 April noon. Do not infer Paris time: verify the unspecified zone before submission.
- Master Erasmus: verify credit eligibility with the Master's programme function and mobility approval with Erasmus administration before relying on finance. Link the signed-credit certificate and host agreement requirements in the guide.

## Task-specific source tree and retrieval status

```
Sciences Po Students
├─ Erasmus programme (FR) — retrieved
│  └─ 2026–27 rate decision (EN PDF, one page) — retrieved
└─ Mobility grants (FR) — retrieved; 2026–27 non-European cycle closed
Sciences Po École de la recherche
├─ Doctoral international mobility — retrieved
│  ├─ Erasmus spring2027 — extracted, closed at timestamp
│  ├─ CamPo2027 — checked; no dedicated funding, closed8Nov
│  └─ Alliance doctoral mobility — official partner call opened; cycle ambiguity
└─ Current funding hub — retrieved
   └─ public Google funding sheet — title only; rows unavailable
Sciences Po MENA
└─ Master's fieldwork call2Apr2026 — retrieved; closed28Apr2026
CIERA home, programme2026–27 — retrieved
├─ Mobility overview — retrieved
│  ├─ Master's research — FR manifestation page retrieved
│  │  └─ /node language redirect — older EN-route text, not used for2027 date
│  ├─ full doctoral research — FR manifestation retrieved
│  ├─ partial doctoral research — FR manifestation retrieved
│  ├─ young-doctor research — FR manifestation retrieved
│  ├─ René Lasserre internship — retrieved, excluded from selected8
│  ├─ eligibilityFAQ — retrieved, conflict retained
│  └─ preparationFAQ — retrieved, updated9Oct2026
├─ methods workshop21–22Jan2027 — retrieved; deadline7Dec
├─ junior conferences — retrieved
│  ├─ autumn2026 call — retrieved; closed
│  ├─ membership page — retrieved official EN redirect
│  └─ application DOCX — tool rejected unsupported content type; not read
└─ Réseaux et terrains — retrieved; no exact next call date
```

Raw /node and language-free CIERA links sometimes produced cache misses/404s. The French /fr/manifestation routes resolved the key calls. This is a tool/retrieval observation, not a claim that the site's public links are universally broken. Historical programme pagination was not traversed: this prospective P09 selection does not seek a census of past conferences or grants. No automated bulk crawl was performed.

## Exclusions and remaining leads

- **CamPo:** Sciences Po's checked page expressly says there is no dedicated participant funding (fee waiver only), and the 2027 application deadline was 8 November 2026. Do not import Cambridge opportunities merely because CHEP has a partner relationship.
- **Alliance:** the official [funder call](https://alliance.columbia.edu/alliance-call-doctoral-mobility) says “Call 2026” and “January 10” without a year, while Sciences Po labels the link a 2026 call and states 10 January 2027. It was not retained among the eight stronger rows. Resolve the cycle with dated official call material before placing it on a ready-to-apply calendar. This is not evidence that the scheme is unavailable.
- **MENA Master's fieldwork:** the [2 April 2026 call](https://www.sciencespo.fr/mena/fr/actualites/appel-a-candidature-pour-le-soutien-a-la-mobilite-des-etudiant-e-s-realisant-un-memoire-de-master-sur-la-region-afrique-du-nord-moyen-orient-mena/) funds Sciences Po Master's research leading to a 2027 defence; application closed 28 April 2026, travel15May–31December2026. Amount and next round were not publicly specified in the call. Good thematic watchlist lead, not currently open.
- **Non-European general mobility:** the [student mobility page](https://www.sciencespo.fr/students/fr/financer/bourses-aides-financieres/aides-mobilite/) expressly marks 2026–27 applications closed, with last standard deadline15October2026 at16:00 Paris. Do not merge it with Erasmus Europe, which has a different administrative route.
- **CIERA René Lasserre:** the [official internship call](https://www.ciera.fr/fr/manifestation/12190) was opened and provides announced spring2027 terms. Not retained solely to keep this subtask to the requested eight rows; it is a legitimate further Master's lead, with the same residence/FAQ conflict. Internship at a French diplomatic/cultural organisation abroad is excluded; German-language competence matters. Record separately if the overall corpus needs this purpose.
- **CIERA Réseaux et terrains:** [programme](https://www.ciera.fr/fr/reseaux-terrains) announces a spring2027 round but no exact call deadline in checked content. Academic teams and a cross-border partnership are required; this is not an individual student application. Further call retrieval remains queued.
- **European/COST exploratory searches:** no tightly relevant historical/economic Action with a verified current call was established in this subtask; unrelated science-network grants were excluded. No claim that COST lacks suitable history activities.
- **Centre Jacques Berque:** discovery lead passed by parent but not independently checked within this bounded subtask. Remains a next retrieval item.
- Parent is independently covering CHEP/CHSP and the doctoral support fund. No duplicate rows were created here.

No evidence here establishes any applicant's nationality, residence, current degree registration, contract, German competence, funded status or willingness to travel. Those are selection questions, not assumptions.
