# P05 coverage, source tree and remaining work

**as_of_date: 2026-11-15.** Read `prompts_proposal.md` (entire shared research brief and P05) and the nonempty `Summary.md`. Summary supplied four starting sites and no additional substantive notes. Only P05 was executed. Other reports were neither required nor used. All work products are inside `reports/P05_website/`.

## Corpus and counting rules

The corpus is a bounded audit of CHEP's publicly accessible Paris website and its French/English host landing pages, with selected linked profiles, event detail and comparator pages. It covers current display as observed on the access date and historical content where necessary to assess navigation and date clarity. It is not a complete domain crawl or a membership, grant, event or publication census.

- **48 live URL observations** in the inventory: **43 CHEP routes + 5 Sciences Po routes = 48**. The Sciences Po observations cover the English and French landings, an older English alias, one researcher profile and one event page. One Sciences Po alias resolves to a previously counted destination; these are requested-route observations, not 48 distinct underlying documents.
- **73 distinct requested URLs** in `page_inventory.csv`, including supporting/comparator pages and failed discovery endpoints. The count includes aliases and attempted endpoints; it is not a count of successfully retrieved pages.
- **89 source observation records** in `sources.csv`: 48 live browser observations, 15 comparator records, 23 journey-research records and three robots/sitemap attempts. Some observations share a URL because indexed and live representations differ. Source IDs identify observations, not unique publications or organisations.
- **13 prioritised backlog records**, **six visitor journeys**, **three comparator institutions/groups**, **three page prototype types** (homepage in both languages, researcher, event), **five screenshots**, 49 accessibility-tree text files (48 page observations plus the keyboard destination), and one embedded-form DOM extract.
- The publication listings display **18 title-level entries per language**. This is a page-content count, not 18 unique works, a complete bibliography or a count of CHEP-funded outputs. Translations/editions were not deduplicated for this website audit.

No coverage percentage is given because the total public site universe, inbound URLs and internal CMS inventory are unknown. All main bilingual entry sections and all six People category landings in both languages were checked live. Deeper French archive destinations and most individual/external profiles remain outside the live sample, listed below.

## Task-specific source tree

Legend: **V** = live browser page checked; **I** = underlying indexed/retrieved representation inspected, live state untested; **F** = retrieval failed, not a verified broken page; **L** = link observed, target not inspected in this run. All source access dates are 2026-11-15. Full URLs, owners, titles, retrieval states and source IDs are in `sources.csv`; language and issue fields are in `page_inventory.csv`.

For the following paths the base is **https://histecon.fr** unless a full URL is given. Paired EN/FR paths represent separate observations.

```text
V https://www.histecon.fr/en/                          English home
V /en/index.html ↔ /fr/index.html                    home aliases/language
├── V /en/people.html ↔ /fr/participants.html
│   ├── V /en/organisation.html ↔ /fr/organisation.html
│   ├── V /en/executive_committee.html ↔ /fr/comite_exeutif.html
│   ├── V /en/research_fellows.html ↔ /fr/research_fellows.html
│   │   └── V /en/research_fellows_past.html ↔ /fr/research_fellows_past.html
│   ├── V /en/research_associates.html ↔ /fr/chercheurs_associes.html
│   │   └── V Jonathan Levy institutional profile (URL below); others not exhaustively followed
│   ├── V /en/research_students.html ↔ /fr/doctorantes.html
│   │   ├── V /en/research_students_previous.html [cohorts 2023–2025]
│   │   ├── L /fr/anciens_doctorantes.html
│   │   ├── I /en/Francesco_Giosue.html
│   │   ├── F /en/Rebecca_Mathiot%20.html
│   │   ├── F /en/Giulio_Piumelli.html; /en/Aesa_Virely.html
│   │   └── L corresponding French individual profile links
│   └── V /en/research_visitors.html ↔ /fr/research_visitors.html
│       ├── V /en/visiting_graduate_students.html [2021–2022]
│       └── L /fr/doctorantes_invitees.html
├── V /en/publications.html ↔ /fr/publications.html [18 displayed entries each]
│   └── I Princeton: The Real Economy; other publisher targets not comprehensively tested
├── V /en/projects.html ↔ /fr/projets.html
│   ├── L https://histecon.fas.harvard.edu/ehc/
│   ├── L https://www.histecon.fr/archivesnotariales/
│   └── L https://www.histecon.magd.cam.ac.uk/slavery/index.html [labelled 2020–2022]
├── V /en/chep_events.html ↔ /fr/chep_activites.html
│   ├── V /en/seminars.html ↔ /fr/seminaires.html
│   │   ├── L two CHSP series targets; one dated session checked live (below)
│   │   └── I https://histecon.fas.harvard.edu/seminars/index.html
│   └── V /en/events_sub.html ↔ /fr/activites_sub.html
│       ├── V /en/events_upcoming.html; /en/events_upcoming_cs.html [empty states]
│       ├── V /en/events_recent.html [2019–2026, plus undated item]
│       │   ├── I /belonging/index.html; F /belonging/programme.html
│       │   └── F /climate_capitalism/index.html
│       ├── V /en/events_recent_cs.html [2022–2025]
│       └── L /fr/evenements_avenir.html; /fr/evenement_recents.html;
│             /fr/evenements_soutenus_avenir.html; /fr/evenements_soutenus_recents.html
├── V /en/research_grants.html ↔ /fr/bourses.html [2027 call]
│   └── L /fr/bourses_portail.html [application not tested]
├── V /en/announcements_archive.html ↔ /fr/archive_annonces.html
├── V /en/contacts.html ↔ /fr/contacts.html
├── V /en/list.html ↔ /fr/liste.html [embedded EN form DOM inspected; no submission]
└── F /robots.txt; www robots.txt; /sitemap.xml [local DNS failure]
```

Sciences Po and selected supporting sources:

- **V** [English CHEP landing](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/), **V** [French CHEP landing](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/), **V** [older English route](https://www.sciencespo.fr/histoire/en/content/centre-history-and-economics-paris-chep/) resolving to the current research route. French/English host content rechecked independently of search snippets.
- **V** [Jonathan Levy directory profile](https://www.sciencespo.fr/histoire/en/directory/levy-jonathan/); **I** [older profile route](https://www.sciencespo.fr/histoire/en/researcher/Jonathan%20Levy/89581.html). The latter was not independently redirect-tested.
- **V** [17 November 2026 seminar announcement](https://www.sciencespo.fr/histoire/fr/evenements/le-retour-des-inegalites-bilan-et-perspectives-historiographiques/). Date, time, venue, organiser and registration-information route checked; registration and occurrence not tested.
- **I** [Princeton's The Real Economy](https://press.princeton.edu/books/hardcover/9780691252551/the-real-economy): metadata check for a publication journey. Book text was not read or reproduced.
- **I** [CHSP French home](https://www.sciencespo.fr/histoire/fr/): target of the host language switch. An externally linked newsletter Google form was **F** in the research tool; no form interaction occurred.

Comparators/partners, with exact attempt statuses in P05-CMP-S01–15:

```text
I Harvard https://histecon.fas.harvard.edu/
├── I /events_main.html
├── I /events.htm [older retrieved placeholder conflicts with newer home representation]
└── I /seminars/index.html
I CHSP https://www.sciencespo.fr/histoire/en/
├── I /histoire/en/events/
└── I /histoire/en/the-centre/join-us/
I CAMPOP https://www.campop.geog.cam.ac.uk/
├── I /seminars/
└── I /seminars/graduate/previous.html
F Cambridge CHE https://www.histecon.magd.cam.ac.uk/
├── F non-www home; /index.html
├── F /seminars.html
└── F /chep/ [historical Paris branch]
```

CAMPOP is the third comparator after Cambridge CHE retrieval failed. It is not part of a claimed CHEP organisational hierarchy. Harvard/Cambridge membership and outputs were not imported into the Paris corpus.

## Research method and retrieval decisions

Started from the shared map and Summary URLs. Followed site navigation, language controls, directory/archive links and the host's event/profile routes. Targeted searches included `site:histecon.fr CHEP séminaires 2026`, `site:histecon.fr "research fellows"`, and `site:sciencespo.fr/histoire "CHEP"`. Opened underlying sources for used claims; unprocessed search results were not treated as evidence.

Indexed retrieval displayed crawl-age metadata from today to 2.6 years ago. Those ages are explicitly kept out of `source_date`. Live browser observations resolved consequential current-state questions. Root's local robots/sitemap GET attempts failed DNS resolution in the restricted execution environment. The work then used focused public browser visits and source retrieval, not an automated recursive crawl. Saved observations avoided further repeated research requests; several key pages were revisited solely to replace accessibility-tree diffs with complete saved snapshots.

No pagination appeared on the sampled CHEP category lists; the CHSP comparator events page exposed pagination but was inspected only as a UI pattern. Relevant linked programmes were noted, including the inaccessible Belonging programme. No PDF collection or full archive extraction was attempted because the deliverable is a website audit. Other historical programme links remain a retrieval queue, not completed checks.

## Reconciliations and unresolved evidence

| Question | Decision and status | Next step |
|---|---|---|
| Is the English index broken? | `verified` live loading; indexed 406 is a tool failure. | Preserve route; no broken-link claim. |
| Is French home outdated compared with English? | `verified` same current core notices live; old indexed 2024 representation superseded. | Review live paired changes, not cached age. |
| Does Sciences Po have two contradictory current English landings? | Old route resolved to current route live; redirect HTTP code untested. | Webmaster can inspect actual response chain. |
| Who is coordinator? | Jonathan Levy on both live organisation languages; Todd is separately committee president. | Confirm start/end dates internally before adding a timeline. |
| What happened in 2019? | `conflicting` host French wording versus CHEP and host English distinction; draft correction proposed. | Host editor and academic coordination validate wording. |
| Are fellows rosters inconsistent? | Difference in coverage verified; its explanation `unverified`. | Confirm category scopes and Joan Chaker's role period, without guessing. |
| Le Bras fellowship period? | `conflicting` past roster 2021–2023 versus archive since-2023 description. | Check original appointment/announcement date and preserve history. |
| Belonging workshop year? | `conflicting`/unresolved chronology in current archive; programme retrieval failed. | Retrieve programme or confirm with organiser; do not invent corrected year. |
| Is the mailing list functional? | Form availability observed; submission/delivery `unverified`; public issue archive `not_found_publicly` within home/list/news/host checks. | Owner confirms service/archive existence; do not infer no newsletter. |
| Does mobile overflow imply formal noncompliance? | Narrow layout/DOM findings verified; full accessibility status `unverified`. | Specialist and assistive-technology review. |

## Boundaries and retrieval queue

The practical stopping point was completion of the six desk journeys, all bilingual top-level sections, the main people category pages, English deeper event/current/archive routes, and the three comparator practices. Remaining targets are deliberately documented rather than silently treated as checked:

1. Deep French event archives and previous/visiting-student archives; individual student profile routes, particularly the encoded-space Mathiot URL. Some student targets failed indexed retrieval; live availability remains unknown.
2. Event series landing pages, the 4 December 2026 session details, application portal, linked programmes/PDFs, and the Belonging programme. Current November prototype uses the separately verified dated CHSP announcement.
3. The linked EHC programme, Archives Notariales and historical slavery-group targets. CHEP's own project page establishes the links and its stated role; target content and functionality were not verified in this run.
4. Cambridge CHE aliases and historical Paris material through another permitted retrieval method if needed; no public link is labelled broken based on the failed tool responses.
5. Every external author profile/publisher link, historical news source and search result not needed for the narrow prototypes. Those are separate censuses, not prerequisites for P05.
6. Robots/sitemap/canonical and redirect status through the webmaster; no unsupported assumptions about CMS or server configuration.

Internal information is essential for editorial access, available staff time, confirmed publication permissions, historical/current role dates, actual participation eligibility, contact ownership, translation capacity, image rights, analytics, user needs and content approval. The five-hour weekly allowance and cash estimates are planning assumptions. No audience satisfaction, attendance, conversion rate or traffic baseline was available.

## Output checks

The CSVs use UTF-8 with explicit IDs, source links and missing-value language. Live and indexed observations remain separately identifiable. No proposal is represented as an approved service. Local evidence links and required files were checked for existence; source IDs in the inventory/backlog were reconciled against the register. Screenshots support layout observations. The supplied prototypes remain text only, and no site was built, modified or published.
