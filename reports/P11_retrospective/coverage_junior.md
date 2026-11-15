# P11 junior-scholar expansion: coverage and decisions

as_of_date: **2026-11-15**. This is a research module for P11 only. All URLs below were accessed on that date; the source register identifies retrieval failures and crawler ages. No P02 output was required or imported.

## Declared cohort and corpus

The bounded expansion cohort is **Jessica Balguy, Joan Chaker and Francesco Giosuè**, selected to add current postdoctoral and student scholarship to CHEP’s featured-books corpus. Their Paris connection is explicit on the [Sciences Po CHEP overview](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) (P11-JS004), with Balguy also in [CHEP Research fellows](https://histecon.fr/en/research_fellows.html) (P11-JS001) and Giosuè in [Research students 2026](https://histecon.fr/en/research_students.html) (P11-JS003). This is not a census of every CHEP junior researcher.

Publication window: **2019-01-01 to 2026-11-15 inclusive**. The extraction includes every dated in-window publication entry in the three bibliographies specified below, plus Chaker’s linked 2026 journal article. The core contains **14 distinct published work records**: Balguy 5; Chaker 5; Giosuè 4. Formats: one source-edition book, one contribution documented at collective-volume level, three journal articles, one research article, two book chapters, five public essays, and one public scholarly essay. The fine-grained format labels distinguish publisher presentation from institutional bibliography headings. These labels sum to 14; they are not quality rankings.

A separate file, `student_research_supplement.csv`, records **four degree dissertations/theses**, excluded from the published-work total. Two Giosuè completion years are inferred from degree end dates; Chaker’s exact defence date/year remains unknown. Her institutional completion announcement is headed 2025/2026. There are no verified CHEP funding acknowledgements for the 14 works in this checked corpus; that finding means **support not found publicly**, not that support was absent.

## Task-specific source tree

```text
CHEP / Sciences Po
├── Research fellows [retrieved, cached six months]
│   https://histecon.fr/en/research_fellows.html
│   └── Balguy → CMU author CV, p.1 [retrieved, cached ten months]
│       https://www.cmu.edu/dietrich/lcal/about-us/cvs/jessica-balguy-cv-compressed.pdf
│       ├── 2020 book → Karthala + CNRS/CIRESC [retrieved]
│       ├── 2020 journal article → author CV [retrieved], CORE PDF [403]
│       ├── 2021 Lexique → BnF + Karthala [indexed records; direct opens failed]
│       ├── 2023 chapter → Champ Vallon volume [retrieved; contents link loops]
│       └── 2020 EHESS essay → CV [retrieved]; original text [not located]
├── Sciences Po CHEP overview [retrieved; cached two weeks]
│   https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/
│   └── Chaker → Orient-Institut Beirut institutional bibliography [retrieved]
│       https://www.orient-institut.org/people/person/Joan%20Chaker.html
│       ├── 2020 Jadaliyya Parts 1 and 2 [retrieved]
│       ├── 2020 Public Works Arabic essay [retrieved]
│       │   └── earlier Jadaliyya version lead [cache miss; deduplicated provisionally]
│       ├── 2021 Progressive International [retrieved as rewritten tool summary]
│       └── Urban Matters author page → 2026 research article [retrieved]
│           https://urbanmattersjournal.com/researcher/joan-chaker/
├── Research students 2026 [retrieved; crawler said today]
│   https://histecon.fr/en/research_students.html
│   └── Giosuè → Sciences Po institutional bibliography [retrieved]
│       https://www.sciencespo.fr/histoire/en/directory/giosue-francesco/
│       ├── 2022 Engramma article [publisher text and DOI retrieved]
│       ├── 2023 Quaderni Stefaniani article [profile metadata only]
│       ├── 2024 chapter [profile metadata only]
│       ├── 2025 Age of Revolutions essay [full text retrieved]
│       └── December 2026 Annales Benjamin Constant article [excluded: forthcoming]
└── Past fellows [retrieved; crawler said today]
    https://histecon.fr/en/research_fellows_past.html
    ├── Génard → Harvard fellowship profile [retrieved; books handled by other P11 module]
    ├── Le Bras → UVSQ profile [two timeouts; books handled by other P11 module]
    └── Hewitt [outside this expansion cohort]
```

All article/volume URLs, source titles, access dates and source IDs are in `sources_junior.csv`. Giosuè’s CHEP individual page retrieved only navigation; the Sciences Po directory supplied the substantive biography. The School of Research duplicate directory route returned a cache miss; the Centre for History route succeeded. The students’ linked Mathiot page returned a cache miss, Piumelli’s a cache miss, and Virely’s a 406. A Sciences Po Mathiot profile was indexed but failed direct opening. These limits do not establish that those pages are broken in a browser.

## Checked categories and years

| Author | Author bibliography processed | In-window entries extracted | Exclusions and limits |
|---|---|---:|---|
| Jessica Balguy | CMU CV: Publications and Other publications, p.1 | 5 | All five listed entries extracted; no 2019, 2022 or 2024–2026 publication entries in that document. CV update date absent; later publications remain a coverage gap. Thesis abstract separately retrieved. Database and talks excluded from text total. |
| Joan Chaker | OIB bibliography plus Urban Matters linked-author bibliography | 5 | Four OIB in-window essays plus one 2026 research article. OIB’s 2010 chapter, 2016 article and 2017 review are outside window. Thesis and first-book project not counted as published books. |
| Francesco Giosuè | Sciences Po publications section and two dissertation titles in education section | 4 | All four already-published entries extracted. December 2026 article excluded at cutoff. Degree research stored separately; talks and event organisation excluded. |

Completion means **all in-scope entries in these checked author-bibliography sections**, not all publications ever written by the three authors. None of the author pages claims to be a complete up-to-date bibliography. No percentage of all CHEP output is reported because the denominator is unknown. A repository-wide sweep of HAL/ORCID has not been completed; no invented ORCID has been assigned.

## Attribution, edition and title decisions

- Balguy’s 2020 book is an edition of documentary debates; her 2023 dissertation is a different work. The publisher biography places the earlier book in her EHESS/CIRESC research context. The current CHEP profile does not date her appointment. Therefore the older works are labelled earlier scholarship of a later-listed fellow, not CHEP output.
- Chaker’s 2026 research article is dated **17 June 2026** on [Urban Matters](https://urbanmattersjournal.com/debt-domicide-and-the-politics-of-method-in-urban-studies-towards-a-structural-analysis-from-palestine-to-lebanon-and-beyond/) (P11-JS016). The linked author biography still says Harvard PhD candidate (P11-JS017); the [OIB completion announcement](https://www.orient-institut.org/news-detail/congratulation-to-our-doctoral-fellow-joan-chaker-2025-2026-who-received-her-phd-thesis-from-the-history-department-at-harvard-university.html) (P11-JS018) describes a future CHEP start but supplies no exact date. Publication-time CHEP affiliation remains unverified. The current Sciences Po CHEP overview supports present inclusion.
- Chaker’s Arabic housing essay appears at Public Works with a 17 February 2020 date. Her 2026 reference list cites a same-title Jadaliyya item dated 5 January 2020. That item could be an earlier version/republication, but its direct page could not be fetched. Preserve the lead in P11-JW009; count one underlying work provisionally. Do not silently treat February as the first-publication day.
- Jadaliyya’s Part 2 title omits “101”; use the inspected publisher title. Parts 1 and 2 are distinct serial essays, not duplicate editions.
- Giosuè’s August 2025 essay predates the 2026 CHEP student list. Its byline note says his Sciences Po doctorate starts in autumn 2025; do not retroactively assign his Master’s work or earlier essays to CHEP.
- The Le Bras affiliation conflict is real in checked public pages: past-fellows page says **2021–2023**, while the parent’s homepage inspection says **since 2023**. Neither should be silently preferred for attributing a publication to a fellowship period. This is outside the three-person expansion but relevant to the combined retrospective.

## Rights and interpretation

Metadata and original paraphrase are suitable for the draft. No cover, archival image, quotation, publisher abstract, or full article is licensed for republication by this research. The Engramma article reproduces magazine covers; the Urban Matters article credits a photographer and permission granted to another organisation. Neither supplies permission for CHEP reuse. Link readers to the sources instead. Thematic pairings are editorial analysis, not evidence of personal collaboration or influence. The Giosuè essay, Chaker research-article introduction and Balguy publisher synopsis provide enough accessible evidence for short argument-led cards; metadata-only entries should remain bibliographic notices.

## Next retrieval queue and internal decisions

1. Retrieve Balguy’s current author bibliography or repository profile and the original EHESS essay; check whether 2024–2026 texts are missing. Her CV is an identifiable historical source, not a live completeness guarantee.
2. Resolve Balguy’s exact Lexique entry/pages, chapter pagination, journal article DOI and the Chaker Arabic essay version chain. Do not block a text-only retrospective on images.
3. Confirm appointment dates for Balguy and Chaker, CHEP’s intended meaning of “research student,” and whether any selected work explicitly acknowledged CHEP support. These require institutional/author confirmation; no contact has been made.
4. Finish publisher checks for Giosuè’s 2023 article and 2024 chapter; recheck the December 2026 article after publication if updating for 2027.
5. Expand future junior coverage to the other three 2026 students and former fellows as a clearly separated work package. This run’s source-bound corpus supports a draft, not a claim that those scholars have no publications.
