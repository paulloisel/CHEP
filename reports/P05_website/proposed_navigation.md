# P05 — Proposed navigation and content system

as_of_date: **2026-11-15**. Discussion draft; no site changes are authorised by this document. Current observations are documented in `sources.csv`, `page_inventory.csv` and `evidence/`. Proposed labels and paths are design choices, not existing services.

## Current navigation, observed live

```text
CHEP /en/index.html ↔ /fr/index.html
├── Home / Accueil: notices, introduction, selected books, mailing-list link
├── People / Participants
│   ├── Organisation
│   ├── Executive Committee / Comité exécutif
│   ├── Research Fellows → Past Research Fellows
│   ├── Research Associates / Chercheurs associés → institutional profiles
│   ├── Research Students / Doctorant·e·s (2026) → previous cohorts
│   └── Research Visitors / Chercheurs invités → visiting graduate students
├── Publications: selected participant books → publishers
├── Projects / Projets
│   ├── Economic History, Climate, and the Environment (Harvard)
│   ├── Archives Notariales (CHEP-hosted portal)
│   └── Slavery and French Economic life (2020–2022, Cambridge)
├── CHEP Events / Activités du CHEP
│   ├── Seminars / Séminaires → two CHSP series and joint online seminar
│   └── Conferences, meetings and workshops / Colloques, réunions et ateliers
│       ├── Centre events → Upcoming / Recent
│       └── Centre-supported events → Upcoming / Recent
├── Grants / Bourses: current 2027 doctoral call → application portal
├── Announcements archive / Archive des annonces
└── Contact Us / Contacts
Utility: FR / EN; Harvard; Cambridge; homepage search field
Sciences Po CHEP landing pages → CHEP; separate host editorial system
```

Sources: [People](https://histecon.fr/en/people.html), [projects](https://histecon.fr/en/projects.html), [events](https://histecon.fr/en/chep_events.html), [event branches](https://histecon.fr/en/events_sub.html), [French homepage](https://histecon.fr/fr/index.html), accessed 2026-11-15. The two upcoming conference/workshop pages already have empty states. The proposal improves the connection between these branches; it does not invent an absent archive.

## Proposed compact navigation

```text
Home / Accueil
├── People / Chercheuses et chercheurs
│   ├── Short topic labels + links, retaining documented categories
│   ├── Organisation and governance
│   └── Former participants and dated cohorts
├── Research / Recherche
│   ├── Projects and research resources
│   └── Selected publications / Sélection de publications
├── Events / Événements
│   ├── Next announced activities (all formats; organiser clearly labelled)
│   ├── Seminar series
│   └── Archive by year, retaining Centre / supported attribution
├── Funding / Bourses
│   ├── Current calls with eligibility, cycle and status
│   └── Past calls and award notices (separate record types)
└── About and participation / Présentation et participation
    ├── Remit, history, host and partners
    ├── Attend an event / receive notices / ask a question
    └── Institutional contact and practical location
Utility: same-page Français / English; News archive; search if retained
Footer: institutional contact, host/partner links, accessibility contact if approved
```

Keep existing URLs in the first phase; these groupings can be ordinary links on existing pages. Do not require a CMS migration, faceted search, a member portal or a new calendar service. Publication cards can remain a simple list sorted by verified year. Do not rename “Research Students” to a universal student membership scheme. “Participation” must distinguish event registration, announcements and formal affiliation.

## Reusable records

Every record: `record_id`, `record_type`, `language`, `translation_of`, `title`, `canonical_public_url`, `source_url`, `source_title`, `source_date`, `checked_on`, `evidence_status`, `editor_function`, `review_due`, `publication_status`. Use `date_unknown` or `not_found_publicly` explicitly; an editorial review date is not the original activity date.

| Type | Minimum additional fields | Validation and maintenance |
|---|---|---|
| Person | Display name; exact CHEP category; role start/end or unknown; current/former/visiting status; home institution; 1–3 verified research topics; 60–100-word biography; institutional profile; selected work IDs; image permission if used | Academic coordinator validates affiliations and category changes; subject checks biography; student prepares edits; communications publishes. Do not infer end dates from omission. |
| Publication | Author IDs; full title; year; output type; language; publisher/journal; DOI/ISBN where verified; edition/translation relationship; publisher/repository link; explicit CHEP relationship; rights status | Student checks authoritative metadata; academic editor approves attribution. “By a participant” is distinct from centre-funded research. Preserve original French titles and accents. |
| Event | Start/end date and time; explicit time zone; format; venue/room; speaker; organiser/co-organiser/supporter; title; short description; language; audience/access rules; registration destination/deadline; announced/held/cancelled status; series ID; programme/recording link; accessibility information attributed to organiser | Event organiser validates logistics and access; student updates listings; communications publishes. A past date alone does not verify an event occurred. |
| Grant | Funder; call cycle; eligible stage/affiliation; permitted costs; amount/currency/basis; application and referee deadlines separately; time zone; official terms; portal; status; enquiry route | Scheme administrator validates eligibility/deadlines. Mark closed after the verified deadline; do not predict next year's dates. Keep awards separate from calls and expenditure. |
| News | Publication date; underlying activity date; item type (appointment/award/project/call); short summary; person/project IDs; institutional attribution; source; expiry/archive rule | Communications validates publication and provenance. Historical role wording should remain attributed and dated rather than presented as current biography. |
| Project/resource | Title; brief question; CHEP role; dates/status; lead institution; participating roles; resource/output links | Academic lead validates role and current status; retain historical projects with their periods. |

Start with a shared editorial register in existing institutional tools. No new database purchase is assumed. The reusable fields are a specification, not an operational system already installed.

## Bilingual policy

Publish critical facts together in both languages: names, institutional roles, dates, location, access rules, eligibility and deadline status. Preserve original event and publication titles; an explanatory translation should be visibly labelled. Link the language switch to the equivalent page, and disclose when a linked external profile or event page is available only in another language. Do not silently send a visitor to the host institution's homepage.

The live CHEP homepages have matching current notices. Remaining examples are more specific: French visitor biography text is English; French project/archive text mixes languages; the French CHEP logo leads to the English homepage; the host English language switch leads to the CHSP French homepage. The host French introductory chronology also attaches 2019 to the joint centre's founding. Prepare the corrected chronology as “La collaboration a débuté en 2019 ; le CHEP a été établi en 2022”, subject to institutional editorial validation. Sources: [French visitors](https://histecon.fr/fr/research_visitors.html), [French projects](https://histecon.fr/fr/projets.html), [French home](https://histecon.fr/fr/index.html), [host English](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/), [host French](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/), accessed 2026-11-15.

Use a weekly paired review of changed fields, with a named function responsible for each language. If translation is pending, display that status rather than allowing critical factual differences to persist. A native-level editorial review is needed before publishing the supplied French copy.

## Migration checklist for institutional staff

1. Confirm the publishing platform, editor access, deployment/backup process and separate Sciences Po owner. None was inspected internally.
2. Export existing pages and assets; keep a dated backup and an inventory of inbound URLs if analytics or logs are available.
3. Choose the preferred host and homepage route. Both `https://www.histecon.fr/en/` and `https://histecon.fr/en/index.html` loaded live; no canonical link was found in the sampled home DOM. This does not establish server configuration or indexing penalties.
4. Preserve existing URLs where practical. Record source → destination for every actual change, including encoded spaces and misspellings in historic paths. Verify redirect type, destination and loops; do not normalise paths without testing.
5. The Sciences Po `/en/content/centre-history-and-economics-paris-chep/` route already resolved in-browser to `/en/research/centre-for-history-and-economics-in-paris-chep/`. Preserve that observed mapping; its HTTP status code was not inspected.
6. Retain former fellows, previous student cohorts, past events, programme PDFs and historical project pages. Add archive labels and current-listing return links; do not silently overwrite historical dates or affiliation evidence.
7. Validate all six journeys at desktop and 390-pixel width, then broaden to 320/768/1280 pixels. Check keyboard focus, skip link, headings, image alternatives, zoom and contrast with appropriate tools and assistive technology.
8. Have the academic editor approve roles/dates, the event organiser approve logistics, and the funding administrator approve call copy. Check French/English parity before publishing.
9. Publish only after institutional approval outside this research task; retain a rollback route. Review errors and task completion after two weeks.

Do not migrate images without establishing permission. The text prototypes require no new imagery. Existing cover images appearing on the current site are not evidence of permission to reuse them in new outputs.
