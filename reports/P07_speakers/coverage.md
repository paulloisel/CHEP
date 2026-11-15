# P07 — Coverage and methods record

**as_of_date: 2026-11-15. All research access dates: 2026-11-15.**

## Scope and stopping rule

Executed P07 and the entire shared research brief only. Read `prompts_proposal.md` and nonempty `Summary.md`; the latter contained the four expected institutional links and no substantive additions. Other P01–P12 reports were not used or awaited. Outputs are confined to `reports/P07_speakers/`. No messages, invitations, subscriptions, applications, website edits or publication actions occurred.

This is a Paris-centred, purposive speaker search, not a census of eligible historians. Candidate works span 2012–2026 editions and current projects; historical subject matter ranges from early modern history to contemporary political economy. Selection sought concrete connections across credit, law, public finance, empire and climate, including researchers at documented junior and senior ranks, European possibilities and selected international contributions. Demographics, personal networks and willingness were not inferred. Full Cambridge/Harvard memberships, publications and calendars are excluded except documented Paris-linked programmes.

The appearance check traversed available relevant programme branches, then checked all 20 selected names against those pages and targeted searches. It stops at 20 supported candidates, a P07 planning target; it does **not** claim a comprehensive speaker census. Unretrieved programmes and workshop participant lists are a remaining queue. The latest programme pages were followed after legacy routes proved older, avoiding a false claim that the calendar stopped in 2025.

## Corpus counts

- **20** candidate records; **8** candidate briefs; **4** proposed pilot sessions; **2** invitation drafts (French/English).
- **99 source records / 97 distinct URLs** in `sources.csv`. Two duplicate URLs are retained with source-ID provenance: P07-S015/S321 (Delalande) and P07-S011/S326 (EHC). This is not a count of 99 independent sources or successful retrievals.
- **40 announced/numbered Histoires slots** across five academic programmes, 2022–23 to 2026–27, including future and postponed entries. They are not 40 verified held events.
- **30 dated entries** in the joint online archive, 20 May 2020–1 April 2026. They are shared-network listings, not Paris-only events.
- **La matière du politique:** six academic programmes, 2021–22 through 2026–27, inspected through the current canonical page. No total held-event count calculated.
- CHEP recent events checked for 2022–2026 examples; regional archive inspected for 2019–November 2024 leads. Regional inclusion alone does not establish CHEP sponsorship.
- No percentage of all CHEP events or all possible speakers is stated because the full denominator is unknown. No private invitation or attendance data was available.

## Source tree: Paris and institutional boundaries

`R` = substantive opened material; `I` = indexed material only; `F` = failed/empty/partial retrieval. These describe this research tool's results, not live website health. Detailed statuses and crawl-age qualifications appear in the source register.

```text
Summary.md starting points
├── CHEP Paris EN www home [R] / supplied index route [not separately resolved]
│   ├── FR home [R, older cached state]
│   ├── Organisation [R] → Levy: Coordinator
│   ├── People navigation / Associates [R] → scoped respondent pool
│   │   └── Executive committee [F; no governance census attempted]
│   ├── Publications [R] → selective participant bibliography only
│   ├── EN Projects [F] / FR Projets [R, older cached state]
│   │   ├── Archives Notariales [R]
│   │   └── EHC programme [R; explicitly Paris/Cambridge/Harvard]
│   ├── Seminars EN/FR and aliases [F]
│   ├── Conferences index [F] → Recent events [R]
│   │   ├── 2025 New Paths workshop Cambridge target [F]
│   │   └── 2026 joint workshop Cambridge target [F]
│   ├── Upcoming events [I; direct retrieval failed]
│   ├── Regional archive [R; mixed organisers]
│   └── robots.txt / sitemap.xml [F; no automated crawler used]
├── Sciences Po CHEP page [R]
│   ├── Histoires legacy route [R, older] → canonical route [R, 2026–27]
│   │   └── Five annual calendars 2022–27; no pagination found
│   ├── La matière legacy route [R, older] → canonical route [R, 2026–27]
│   │   └── 2024–25 PDF [F]; HTML supports programme claims
│   └── Current staff profiles → specific publications and research interests [R]
├── Harvard joint centre
│   ├── Joint online archive [R, 2020–26; no pagination found]
│   └── EHC [R] → Paris-linked activity, not blanket membership
└── Cambridge
    └── Linked Paris/joint workshop targets [F]; descriptions on Paris retained
```

The linked source table below provides exact URLs for each mapped branch. The shared map was applied as a navigation framework, not treated as an instruction to execute unrelated grant, publication-census or organisation workstreams. Fellows/students/visitors were not exhaustively traversed because speaker selection uses a focused respondent and thematic corpus; no population-wide affiliation conclusion is made. Grants, mailing-list subscription, anniversary planning and current funding eligibility are outside this P07 question.

## Candidate-source expansion

Each of the 20 people has a source-backed institutional route and named scholarship in `candidates.csv`. Profile searches were followed to responsible institutional pages wherever possible; publisher/repository pages supplied the work. Primary author essays support the Dermineur, Farber, Murphy and van Waijenburg readings. Chatterjee has an open research article. Barca and Calafat have enough description/abstract evidence for a precise question, but need a substantive permitted excerpt before a full workshop. Remaining candidates have their actual reading depth stated, rather than being described as fully assessed books.

Searches included combinations of `site:histecon.fr` and candidate surnames, `site:sciencespo.fr/histoire` with CHEP/programme titles, and institutional/publisher searches with exact work titles. Negative grouped-name searches were treated only as leads and supplemented with programme inspection. No bulk automated crawl or account access was attempted; robots/sitemap requests failed through the browser tool, so no crawling permissions were inferred.

## Prior-appearance and affiliation reconciliation

| Item | Evidence/status | Decision |
|---|---|---|
| Calafat, 2023 | Histoires lists 30 May and 17 October; regional archive says 10 October with a different title. P07-S007/S022, `conflicting` for October date. | Prefer responsible series' 17 October date; preserve discrepancy. Proposed 2024 article is a return contribution. No confirmed-held claim. |
| Chatterjee, 2022 | Current host-series page lists 8 April 2022, Fuel Rioters. P07-S033, `verified` announcement. | Prior host-series appearance; related topic makes duplication review essential. Do not label a separate CHEP invitation. |
| Ogle and Warde | Joint archive and recent CHEP events. P07-S009/S005, `verified` listings. | Returning-network possibilities; no inference of attendance, availability or private ties. |
| Albritton Jonsson | Scarcity is a suggested future climate-group reading. P07-S006. | Not evidence of an appearance, completed reading session or Paris affiliation. |
| Pompermaier | Regional archive lists a PSE event on 23 October 2019. P07-S022. | A nearby precedent, not a verified CHEP appearance. |
| Remaining candidates | No appearance found in checked corpus; `unverified` prior-appearance status. | Record `not_found_publicly`; never “has never visited CHEP.” |
| Bridges | Current Vanderbilt profile calls Harvard fellowship previous; publisher bio still says Harvard. P07-S109/S110. | Current institution Vanderbilt Policy Accelerator; publisher biography is stale for affiliation purposes. |
| Farber | Current Columbia profile updated 29 October 2026: Associate Professor; leave Fall 2026/Spring 2027. P07-S204. | Preserve leave notice; do not infer residence, refusal or availability. |
| Barca | USC current position differs from older fellowship/Coimbra descriptions; CISPAC translated headline describes application rather than completed appointment. P07-S303/S325. | Use retrieved USC current title; do not promote the translated announcement into stronger employment evidence. |
| Vettese | Spring 2026 fellowship announcement and current directory, no verified end date. P07-S314–316. | Historical stage documented; continuing November appointment is `unverified`. Recheck before outreach. |
| Juliette Levy / Pompermaier | Current institutional affiliation supported; rank only older publisher or indexed profile. P07-S114–116/S215–218. | Do not silently promote old/indexed ranks into unqualified current-stage claims. |
| Editions and works | Farber, Bridges, Bürbaumer, Vettese have later editions of older works. | Retain original/edition dates; do not advertise them as newly researched 2026 books. |

All suggested matches are `inferred`. Calafat–Trivellato coauthorship is a separately `verified` relationship; proposed participation is still unverified. CHEP associate, host colleague, co-convenor, regional speaker and wider-network respondent remain distinct categories.

## Access limits and remaining queue

Some sources were delivered from caches ranging from days to years old. Access on 15 November 2026 does not mean a same-day live capture. No dated web-archive snapshot was obtained; archive-snapshot dates are therefore `not_applicable`, not confused with crawl dates. The canonical 2026–27 programme pages improve coverage beyond older legacy pages, but future events remain announcements.

Priority retrieval work if the programme advances:

1. Obtain any internal invitation list, confirmed slots and held-event record through the authorised academic/administrative function; reconcile four repeat candidates and other recent contacts.
2. Retrieve Calafat's full paper lawfully and Barca's selected chapter; validate that pre-readings support the planned discussion. Improve Dungy/Pompermaier direct access before promoting them from reserve. No bypass of anti-bot/paywall restrictions.
3. Retrieve missing Cambridge joint-workshop programmes to distinguish speakers, convenors and attendees; correct source dates against primary documents. The failed PDF and index routes do not justify absence claims.
4. Recheck current positions, especially fixed-term fellows and profiles only retrieved as shells, when dates are chosen. Confirm actual departure location independently of university affiliation.
5. Obtain the academic owner's assessment of demand, language/access needs, respondent interest, budget, honoraria, travel rules and administrative time. These internal questions determine feasibility; public scholarship cannot answer them.

`not_found_publicly`, `not_applicable` and `date_unknown` are used for missing/nonapplicable values. Unknown travel expenditure, willingness, attendance and demand are never encoded as zero. Estimated €0 incremental facilities in the pilot is explicitly conditional on institutional provision, not an observed budget.

## File and data checks

The final check verifies UTF-8 CSV parsing, unique candidate/source IDs, source-ID joins, 20/8/4/2 deliverable counts, pilot candidate-ID matches, and workload arithmetic. Each recommendation is a proposal, supported by factual research but not a commitment. The source table below is generated from `sources.csv`; handoff research notes retain provenance and may use earlier candidate IDs. **Final `candidates.csv` IDs are authoritative.** The extra `selection_matrix.csv` exposes the qualitative judgments.

## Source tree URLs and retrieval ledger

The register is authoritative for full titles, source dates, access dates and support notes. The following index makes its navigation and retrieval status readable without claiming every request succeeded.

### Paris, host and partner context

- P07-S001: [Centre for History and Economics: Paris home](https://www.histecon.fr/en/) — retrieved; web cached crawl 5 months.
- P07-S002: [Organisation](https://histecon.fr/en/organisation.html) — retrieved; web cached crawl 2 weeks.
- P07-S003: [Centre for History and Economics in Paris (CHEP)](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) — retrieved; web cached crawl 2 weeks.
- P07-S004: [Research Associates](https://histecon.fr/en/research_associates.html) — retrieved; web cached crawl today; some employer labels may lag.
- P07-S005: [Recent Centre Events](https://histecon.fr/en/events_recent.html) — retrieved; web cached crawl 2 months.
- P07-S006: [Climate and Capitalism Reading Workshop: Readings and Dates](https://histecon.fr/climate_capitalism/readings.html) — retrieved; web cached crawl 4 months.
- P07-S007: [Histoires de la vie économique](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/histoires-de-la-vie-economique/) — retrieved; web cached crawl 6 days.
- P07-S008: [La matière du politique](https://www.sciencespo.fr/histoire/fr/content/la-matiere-du-politique.html) — retrieved legacy route; web cached crawl 1.7 years.
- P07-S009: [Joint Center for History and Economics Online Seminar: Past seminars](https://histecon.fas.harvard.edu/seminars/past_seminars.html) — retrieved; web cached crawl last month.
- P07-S010: [Archives Notariales](https://www.histecon.fr/archivesnotariales/) — retrieved; web cached crawl today.
- P07-S011: [Economic History, Climate, and the Environment](https://histecon.fas.harvard.edu/ehc/) — retrieved; web cached crawl 5 days.
- P07-S012: [Claire Lemercier](https://www.sciencespo.fr/cso/en/researcher/Claire%20Lemercier/1022.html) — retrieved; web cached crawl 11 months.
- P07-S013: [1751 and Thereabout: A Quantitative and Comparative Approach to Notarial Records](https://www.cambridge.org/core/journals/social-science-history/article/1751-and-thereabout-a-quantitative-and-comparative-approach-to-notarial-records/CBDDC9D2134379765F54476F66364227) — retrieved full HTML; web cached crawl 2 days.
- P07-S014: [Jonathan Levy](https://www.sciencespo.fr/histoire/en/directory/levy-jonathan/) — retrieved; web cached crawl 2 weeks.
- P07-S015: [Nicolas Delalande](https://www.sciencespo.fr/histoire/fr/annuaire/delalande-nicolas/) — retrieved; web cached crawl 2 days.
- P07-S016: [David Todd](https://www.sciencespo.fr/histoire/en/researcher/David%20Todd/86025.html) — retrieved legacy route; web cached crawl 1.5 years.
- P07-S017: [A Velvet Empire: French Informal Imperialism in the Nineteenth Century](https://press.princeton.edu/books/hardcover/9780691171838/a-velvet-empire) — retrieved; web cached crawl last week.
- P07-S018: [Giacomo Parrinello](https://www.sciencespo.fr/histoire/fr/annuaire/parrinello-giacomo/) — retrieved; web cached crawl last week.
- P07-S019: [Alexia Yates](https://research.manchester.ac.uk/en/persons/alexia.yates) — retrieved with redirect from portal; web cached crawl 1.1 years.
- P07-S020: [Centre for History and Economics: French home](https://histecon.fr/fr/index.html) — retrieved; web cached crawl 2.6 years.
- P07-S021: [Projets](https://histecon.fr/fr/projets.html) — retrieved; web cached crawl 2.6 years.
- P07-S022: [Événements passés](https://histecon.fr/fr/archive.html) — retrieved; web cached crawl 2 months.
- P07-S023: [Seminars](https://histecon.fr/en/seminars.html) — failed: cache miss; www alias also failed.
- P07-S024: [Séminaires](https://histecon.fr/fr/seminaires.html) — failed: 406 / cache miss.
- P07-S025: [Conferences, meetings and workshops](https://histecon.fr/en/events_sub.html) — failed: timeout.
- P07-S026: [Projects](https://histecon.fr/en/projects.html) — failed: 406.
- P07-S027: [New Paths in Environmental History](https://www.histecon.magd.cam.ac.uk/new_paths/) — failed retrieval; Paris archive supplies description.
- P07-S028: [JCHE / CHEP Workshop](https://www.histecon.magd.cam.ac.uk/JCHE_CHEP_Workshop/index.html) — failed: cache miss; Paris archive supplies description.
- P07-S029: [Sitemap request](https://histecon.fr/sitemap.xml) — inaccessible via tool.
- P07-S030: [Robots request](https://histecon.fr/robots.txt) — inaccessible via tool.
- P07-S031: [La matière du politique: programme 2024–2025 PDF](https://bo-k2s.sciences-po.fr/histoire/sites/sciencespo.fr.histoire/files/matiere-politique.pdf) — failed: cache miss.
- P07-S032: [Upcoming Centre Events](https://histecon.fr/en/events_upcoming.html) — search index retrieved; underlying open cache miss.
- P07-S033: [La matière du politique (canonical current programme)](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/la-matiere-du-politique/) — retrieved; web cached crawl today.
- P07-S034: [Recent publications by CHEP participants](https://histecon.fr/en/publications.html) — retrieved via web index; crawled three months before access.

### Root candidate profiles and works

- P07-S101: [Destin Jenkins](https://facultydevelopment.stanford.edu/people/destin-jenkins) — retrieved via web index; crawl dates vary.
- P07-S102: [The Bonds of Inequality: Debt and the Making of the American City](https://www.bibliovault.org/BV.landing.epl?ISBN=9780226721682) — retrieved via web index; crawl dates vary.
- P07-S103: [Vanessa Ogle](https://history.yale.edu/people/vanessa-ogle) — retrieved via web index; crawl dates vary.
- P07-S104: [Archipelago Capitalism: Tax Havens, Offshore Money, and the State, 1950s–1970s](https://academic.oup.com/ahr/article-abstract/122/5/1431/4724819) — retrieved abstract via publisher CDN redirect.
- P07-S105: [Business, Government & the International Economy: Faculty](https://www.hbs.edu/faculty/units/bgie/Pages/faculty.aspx) — retrieved via web index; crawl dates vary.
- P07-S106: [Financing the African Colonial State: The Revenue Imperative and Forced Labor](https://www.cambridge.org/core/journals/journal-of-economic-history/article/abs/financing-the-african-colonial-state-the-revenue-imperative-and-forced-labor/9514245BA11D58B053FBB83E4EADF565) — retrieved via web index; crawl dates vary.
- P07-S107: [Financing the African Colonial State: Fiscal Capacity Building and Forced Labor](https://aehnetwork.org/financing-the-african-colonial-state-fiscal-capacity-building-and-forced-labor/) — retrieved via web index; crawl dates vary.
- P07-S108: [Financing the African Colonial State: Fiscal Capacity and Forced Labor](https://www.economics.harvard.edu/sites/g/files/omnuum5991/files/2026-03/Financing%20the%20African%20Colonial%20State%20Fiscal%20Capacity%20and%20For.pdf) — retrieved PDF text; abstract read.
- P07-S109: [Mary Bridges](https://www.vanderbilt.edu/vanderbilt-policy-accelerator/mary-bridges/) — retrieved via web index; crawl dates vary.
- P07-S110: [Dollars and Dominion: US Bankers and the Making of a Superpower](https://press.princeton.edu/books/paperback/9780691248387/dollars-and-dominion) — retrieved via web index; crawl dates vary.
- P07-S111: [Professor Anne Murphy](https://www.port.ac.uk/about-us/structure-and-governance/our-people/our-staff/anne-murphy) — retrieved via web index; crawl dates vary.
- P07-S112: [Virtuous Bankers: A Day in the Life of the Eighteenth-Century Bank of England](https://press.princeton.edu/books/hardcover/9780691194745/virtuous-bankers) — retrieved via web index; crawl dates vary.
- P07-S113: [In search of virtuous bankers](https://www.bankofengland.co.uk/museum/online-collections/blog/in-search-of-virtuous-bankers) — retrieved via web index; crawl dates vary.
- P07-S114: [People: Science and Technology Studies](https://sciencetechstudies.ucr.edu/people) — retrieved via web index; crawl dates vary.
- P07-S115: [The Making of a Market: Credit, Henequen, and Notaries in Yucatán, 1850–1900](https://www.psupress.org/books/titles/978-0-271-05213-7.html) — retrieved via web index; crawl dates vary.
- P07-S116: [Juliette Levy profile](https://profiles.ucr.edu/app/home/profile/juliette) — empty dynamic page; current rank unverified.
- P07-S117: [Marlous van Waijenburg profile](https://www.hbs.edu/faculty/Pages/profile.aspx?facId=1200880) — 403; roster used.
- P07-S118: [Destin Jenkins full profile](https://profiles.stanford.edu/56551) — cache_miss; faculty page used.
- P07-S119: [Financing the African Colonial State replication package](https://www.icpsr.umich.edu/sites/jeh/view/studies/101190/versions/V1) — dynamic shell only; files unverified.

### Credit, law and political-economy candidates

- P07-S201: [Elise Dermineur Reuterswärd — Universitetslektor, docent](https://www.su.se/profiles/e/elde6129) — opened; indexed/crawled one week before access.
- P07-S202: [Before Banks: The Making of Credit and Debt in Preindustrial France](https://www.cambridge.org/core/books/before-banks/822A8C3F63F39643F0169EE675442FB6) — opened; indexed/crawled one week before access.
- P07-S203: [Before banks: Historical lessons for rethinking credit](https://cepr.org/voxeu/columns/banks-historical-lessons-rethinking-credit) — opened full author essay; indexed/crawled three weeks before access.
- P07-S204: [Farber, Hannah](https://history.columbia.edu/person/farber-hannah/) — opened; crawl reported today; page explicitly updated October 29 2026.
- P07-S205: [Underwriters of the United States: How Insurance Shaped the American Founding](https://uncpress.org/9781469699073/underwriters-of-the-united-states/) — opened; indexed/crawled one week before access.
- P07-S206: [Insurance For (and Against) the Empire](https://commonplace.online/article/insurance-for-and-against-the-empire/) — opened full article; indexed/crawled two weeks before access.
- P07-S207: [M. Guillaume Calafat — Maître de conférences](https://www.pantheonsorbonne.fr/page-perso/guillaume.calafat@) — opened; indexed/crawled four days before access; English book tense stale compared with French.
- P07-S208: [The Shipwreck of the Turks: Sovereignty, Barbarism and Civilization in the Legal Order of the Eighteenth-Century Mediterranean](https://albert.ias.edu/entities/publication/6c55edbd-b125-4643-bc4b-f7592c1d302d) — opened abstract; full PDF link listed but not inspected; indexed/crawled one month before access.
- P07-S209: [Madeleine Dungy](https://www.ntnu.edu/employees/madeleine.dungy) — opened; indexed/crawled one month before access.
- P07-S210: [Order and Rivalry: Rewriting the Rules of International Trade after the First World War](https://www.cambridge.org/core/books/order-and-rivalry/5C8204E8343F078403CF7CDB9ADA1C78) — indexed full synopsis retrieved in search; direct open timed out; current live state not established.
- P07-S211: [Hannah Catherine Davies, PD Dr.](https://www.hist.uzh.ch/de/fachbereiche/neuzeit/oberassistierende/davies.html) — opened; indexed/crawled two weeks before access.
- P07-S212: [Transatlantic Speculations: Globalization and the Panics of 1873](https://cup.columbia.edu/book/transatlantic-speculations/9780231546218/) — opened; indexed/crawled one month before access.
- P07-S213: [Benjamin Bürbaumer](https://www.centreemiledurkheim.fr/membre/benjamin-burbaumer/) — opened; indexed/crawled two days before access.
- P07-S214: [Chine/États-Unis, le capitalisme contre la mondialisation](https://www.editionsladecouverte.fr/chine_etats_unis_le_capitalisme_contre_la_mondialisation-9782348094729) — opened; indexed/crawled two weeks before access.
- P07-S215: [POMPERMAIER, Matteo](https://iris.unibs.it/cris/rp/rp110348) — opened; indexed/crawled one week before access.
- P07-S216: [POMPERMAIER Matteo](https://www.unibs.it/en/ugov/person/230281) — indexed profile retrieved; direct open returned 403.
- P07-S217: [2023 SIHS Article Prize for Medieval and Early Modern Italian History: Matteo Pompermaier](https://www.italianhistoricalstudies.org/2023-sihs-article-prize-for-medieval-and-early-modern-italian-history-matteo-pompermaier/) — opened; indexed/crawled two months before access; not a reading of full article.
- P07-S218: [Credit and Poverty in Early Modern Venice](https://su.diva-portal.org/smash/get/diva2%3A1646480/FULLTEXT01.pdf) — indexed opening text retrieved; direct PDF open timed out twice; full text not read.
- P07-S219: [Underwriters prologue and introduction (profile-linked repository file)](https://academiccommons.columbia.edu/doi/10.7916/2t2e-jb86) — anti-bot challenge; content inaccessible.
- P07-S220: [The Shipwreck of the Turks (HAL record)](https://hal.science/hal-04771272v1) — anti-bot challenge; content inaccessible.

### Climate and environmental candidates

- P07-S301: [Elizabeth Chatterjee — Department of History](https://history.uchicago.edu/directory/elizabeth-chatterjee) — retrieved; web cache crawled today.
- P07-S302: [Towards an Energetics of Class: Comparing Energy Protests in India and the United States](https://www.cambridge.org/core/journals/comparative-studies-in-society-and-history/article/towards-an-energetics-of-class-comparing-energy-protests-in-india-and-the-united-states/F6ADAA8A37E7C839615D7C4E4F67BCA5) — retrieved open full HTML; abstract, opening and concluding section read; cache crawled two days ago.
- P07-S303: [STEFANIA BARCA — USC research profile](https://investigacion.usc.gal/investigadores/190416/detalle?lang=en) — retrieved in Galician despite English query; cache crawled three months ago.
- P07-S304: [Forces of Reproduction: Notes for a Counter-Hegemonic Anthropocene](https://www.cambridge.org/core/books/forces-of-reproduction/BE9B0DBDC89593F3284FE3F51D3B0418) — retrieved book description; full text not read; cache crawled two weeks ago.
- P07-S305: [Workers of the Earth: Labour, Ecology and Reproduction in the Age of Climate Change](https://www.plutobooks.com/product/workers-of-the-earth/?select_location=US) — indexed publisher text retrieved in search, including description and TOC; direct open and canonical alias both 403; not live-page verification.
- P07-S306: [Oscar SANCHEZ-SIBONY](https://www.history.hku.hk/people/oscar-sanchez-sibony) — retrieved; cache crawled three days ago.
- P07-S307: [The Soviet Union and the Construction of the Global Market: Energy and the Ascent of Finance in Cold War Europe, 1964–1971](https://www.cambridge.org/core/books/soviet-union-and-the-construction-of-the-global-market/B0D0D14FAD034EB785B3F9CBCC5F66F2) — retrieved description and metadata; cache crawled two days ago.
- P07-S308: [The Soviet Union and the Construction of the Global Market — Introduction excerpt](https://assets.cambridge.org/97811089/95184/excerpt/9781108995184_excerpt.pdf) — retrieved PDF; opening pp. 1–2 and pp. 7–8 inspected; cache crawled three weeks ago.
- P07-S309: [Professor Paul Warde](https://www.pem.cam.ac.uk/college/master-and-fellows/list-fellows/professor-paul-warde) — retrieved; cache crawled last month.
- P07-S310: [The Invention of Sustainability: Nature and Destiny, c.1500–1870](https://www.cambridge.org/core/books/the-invention-of-sustainability/DA31E7325BE2A33EBBA19C4089244A13) — retrieved; cache crawled last month.
- P07-S311: [The Invention of Sustainability — Introduction excerpt](https://assets.cambridge.org/97811071/51147/excerpt/9781107151147_excerpt.pdf) — retrieved PDF; cache crawled nine months ago.
- P07-S312: [Fredrik Albritton Jonsson — Department of History](https://history.uchicago.edu/directory/fredrik-albritton-jonsson) — retrieved; cache crawled yesterday; internal conflict on French translation date and English subtitle recorded.
- P07-S313: [Scarcity: A History from the Origins of Capitalism to the Climate Crisis](https://www.jstor.org/stable/jj.890690) — retrieved metadata and description; cache crawled last month; full book not read.
- P07-S314: [Troy Vettese](https://canada.berkeley.edu/people/troy-vettese) — retrieved; cache crawled four months ago.
- P07-S315: [Current research fellows](https://canada.berkeley.edu/people/current-research-fellows) — retrieved; cache crawled three months ago; directory includes some older cohorts, precise end date unverified.
- P07-S316: [New Sproul Fellow Troy Vettese Explores Relationship Between Capitalism and Energy Extraction](https://canada.berkeley.edu/node/260) — retrieved; cache crawled two weeks ago; announcement concerns spring 2026 not guaranteed continued residence.
- P07-S317: [Half-Earth Socialism: A Plan to Save the Future from Extinction, Climate Change and Pandemics](https://www.versobooks.com/en-gb/products/2650-half-earth-socialism) — retrieved description and metadata; cache crawled two weeks ago.
- P07-S318: [Rebecca L. Spang — Department of History](https://history.indiana.edu/faculty_staff/faculty/spang_rebecca.html) — retrieved; cache crawled five days ago.
- P07-S319: [Stuff and Money in the Time of the French Revolution](https://www.jstor.org/stable/j.ctt1287gs4) — retrieved description and metadata; cache crawled last week; full book requires access.
- P07-S320: [Rebecca L. Spang — Stuff and Money](https://www.rebeccalspang.org/stuff-and-money) — retrieved selected excerpts, marked adapted by author; cache crawled today.
- P07-S321: [Nicolas Delalande](https://www.sciencespo.fr/histoire/fr/annuaire/delalande-nicolas/) — retrieved; cache crawled two days ago.
- P07-S322: [Que reste-t-il des internationales ouvrières ?](https://www.sciencespo.fr/fr/actualites/nicolas-delalande/) — retrieved; cache crawled last month.
- P07-S323: [Pierre Charbonnier](https://www.sciencespo.fr/centre-etudes-europeennes/fr/annuaire/charbonnier-pierre/) — retrieved; cache crawled two weeks ago.
- P07-S324: [Sabine Dullin](https://www.sciencespo.fr/histoire/fr/annuaire/dullin-sabine/) — retrieved; cache crawled two weeks ago.
- P07-S325: [Stefania Barca (USC-CISPAC) becomes the first Beatriz Galindo researcher to apply for a tenured Associate Professor position at USC](https://cispac.gal/en/posts-actualidade/stefania-barca-usc-cispac-convertese-na-primeira-investigadora-beatriz-galindo-que-consolida-unha-praza-de-profesora-titular-na-usc/) — retrieved; cache crawled last month.
- P07-S326: [Economic History, Climate, and the Environment](https://histecon.fas.harvard.edu/ehc/) — retrieved; cache crawled five days ago.
