# P11 coverage, source map and remaining queue

**as_of_date: 2026-11-15.** This run executed P11 only. `Summary.md` was available and contained the four institutional starting URLs, without additional substantive instructions. No other P01–P12 report was required or imported. All output is inside `reports/P11_retrospective/`.

## Corpus boundaries and counts

The bibliography covers **2019-01-01 through 2026-11-15**, with the **2022-01-01 through 2026-11-15** establishment era separately labelled. An earlier featured item is retained as context, and first-publication dates are distinguished from in-window translations or reprints. January 1 is an editorial boundary, not the establishment day. Future 2027 material is not counted.

| Layer | Coverage achieved | Meaning and limits |
|---|---|---|
| CHEP featured-publication pages | **18 of 18 displayed edition entries**, **14 underlying works** | Same titles observed on EN/FR pages. Four displayed translation pairs: Rothschild, Trivellato, Todd and Delalande. No pagination or publication-archive link appeared on either inspected list. This is a complete extraction of those checked lists, not a complete centre bibliography. |
| Junior expansion | **14 work records**: Balguy 5, Chaker 5, Giosuè 4 | All in-window published entries in the three specified author-bibliography sections, plus the linked Chaker 2026 article. Completeness of those public bibliographies is not guaranteed. |
| Context/linked additions | **4 records** | Oualdi’s English original; two chapters within *A World of Public Debts*; Trivellato’s reception article. These are targeted connections, not a census of all chapters or senior authors’ careers. |
| Combined bibliography | **36 edition/record rows, 31 unique work IDs** | Includes one volume-level contribution with entry details unresolved. Chapters and edited volumes are separately typed; do not interpret this as 31 independent institutional achievements. |
| Date strata, by edition/record | **15 establishment-era; 20 collaboration-prehistory; 1 earlier-context** | The 15 establishment-era rows represent 15 distinct works, some originally published earlier. Not a count of work produced or funded at CHEP. Rows across strata must not be summed as distinct works. |
| Editorial selection | **18 unique works**, including **six full cards** | Smaller reading selection drawn from the inventory. Translations stay within a work’s selection record. |
| Separate degree-research register | **4 theses/dissertations** | Excluded from all published-work totals; two completion years inferred, one unknown. |
| Evidence register | **94 source records** | Component IDs preserved, including repeated URLs and failed attempts. Not 94 independent corroborating sources. |
| Languages, by edition/record | French 14; English 18; Arabic 1; Italian 3 | The showcase is primarily English/French; inventory language diversity is wider. No demographic inference made. |

Counting rules: deduplicate translations/reprints with `work_id`; use `edition_id` for bibliographic manifestations; keep distinct serial essays separate; preserve a chapter’s parent-volume note. The Arabic Chaker essay’s earlier-version lead is provisionally grouped as one work. No raw publication total is a quality or impact measure. No percentage of all CHEP research is given because that denominator is unknown.

## Task-specific source tree

**R = substantive text retrieved through the web tool, commonly from an indexed copy; F = retrieval failed; C = access challenge only; I = indexed evidence available but direct open failed.** These labels describe tool access, not whether a website is publicly broken. Full source titles, access dates, exposed cache ages and identifiers are in [sources.csv](sources.csv).

```text
Paris home, history and navigation
├─ https://www.histecon.fr/en/ [R, M001]
├─ https://histecon.fr/en/index.html [F:406, M017]
├─ https://histecon.fr/fr/ [R, M002]
├─ https://histecon.fr/fr/index.html [R: older indexed copy, M011]
├─ https://histecon.fr/robots.txt [F:tool unavailable, S024]
├─ https://histecon.fr/sitemap.xml [F:tool unavailable, S025]
├─ https://histecon.fr/en/publications.html [R, S001]
│  ├─ https://histecon.fr/fr/publications.html [R, S002]
│  ├─ Princeton / CNRS / La Découverte / Other Press / Cambridge Core [R]
│  ├─ Springer / UVA Press / Peter Lang / Penguin / Columbia UP [R]
│  ├─ Seuil three translations and Delalande original [F:403; alternatives below]
│  ├─ EHESS Génard target [F:502 → author announcement / institution R]
│  └─ author sites, abstracts, introductions and edition confirmations [R/I]
├─ https://histecon.fr/en/people.html [R, S021]
│  ├─ https://histecon.fr/en/organisation.html [R, S003/M010]
│  ├─ https://histecon.fr/en/research_associates.html [R, S004]
│  ├─ https://histecon.fr/en/executive_committee.html [F, S027]
│  ├─ https://histecon.fr/en/research_fellows.html [R, JS001]
│  │  └─ https://histecon.fr/en/research_fellows_past.html [R, BS004/JS002]
│  ├─ https://histecon.fr/en/research_students.html [R:2026 label, JS003]
│  │  └─ Giosuè / Mathiot / Piumelli / Virely leads [mixed R/F]
│  └─ https://histecon.fr/en/research_visitors.html [R, S022]
├─ https://histecon.fr/en/projects.html [F:406, S023]
├─ https://histecon.fr/en/events_sub.html [F:timeout, M016]
├─ https://histecon.fr/en/events_recent.html [R, M008]
│  └─ https://histecon.fr/en/spatial.html [R:2019 launch report, M005]
├─ https://histecon.fr/en/announcements_archive.html [R, M015]
└─ https://histecon.fr/fr/archive.html [R:regional archive, M018]
Sciences Po host and historical record
├─ https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/ [R, M003/JS004]
├─ https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2021/2021_10_12_CSFR.pdf [R:text, M006]
├─ https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/LaRechercheaSciencesPo-2022.pdf [R:text, M007]
├─ https://www.sciencespo.fr/histoire/en/our-productions/the-publications/ [R, S019]
│  └─ used for translation check; entire host roster excluded
└─ current author profiles and 2025–26 institutional announcements [R]
Junior author expansion
├─ Balguy: CMU CV p.1 → Karthala/CIRESC, Champ Vallon [R]; BnF [I]
├─ Chaker: Orient-Institut Beirut → Jadaliyya, Public Works, Urban Matters [R]
│  └─ Progressive International [R:rewritten tool summary identified]
└─ Giosuè: Sciences Po bibliography → Engramma, Age of Revolutions [R]
Partners, narrowly used
├─ https://www.histecon.magd.cam.ac.uk/ [F:403, M014]
├─ https://www.histecon.magd.cam.ac.uk/chep/ [F:cache miss, M012]
├─ https://www.histecon.magd.cam.ac.uk/chep/index.html [F, M013]
└─ Harvard publications / Génard profile [R:cross-check only; no network-wide census]
```

Detailed publisher URLs and retrieval decisions are in [coverage_books.md](coverage_books.md); author bibliography routes and each checked year are in [coverage_junior.md](coverage_junior.md); archive and historical alias checks are in [coverage_milestones.md](coverage_milestones.md). Each component source ID takes the `P11-` prefix shown in the master register.

## Checked people, years and forms

The featured layer covers all 14 title-level works, including every coauthor/editor named in those entries; it does not expand each author’s career. The three junior bibliographies were processed across the entire 2019–cutoff window, including years with no entries, without equating an empty year with zero output. Balguy’s checked list has five entries dated 2020, 2021 and 2023; Chaker has 2020–2021 essays plus the 2026 article; Giosuè has one published entry in each year 2022–2025. A December 2026 entry is beyond the cutoff and excluded.

Formats checked include monographs, translations, short and coauthored books, edited volumes, source editions, chapters, journal articles and public scholarship. Student degree research is separate. Databases, talks, recordings, ongoing projects and event programmes are not published-text records. No grants inventory or annual-report programme was undertaken. Historical events were inspected only to establish milestones and a feasible celebration precedent.

## Conflicts and evidential limits

1. **Launch versus establishment:** June 2019 launch and 2022 establishment are compatible but different anniversary bases. Exact 2022 day remains unknown. No archived snapshot or establishment instrument was obtained. PDF locators follow retrieved text/printed pagination; screenshot verification failed in the milestone subtask.
2. **Affiliation:** Le Bras dates conflict across official/publisher pages. Levy’s present Coordinator title does not establish his start date. Todd’s 2025 interview describes a historical coordinator role; no handover date is inferred. Chaker’s June 2026 article gives Harvard affiliation; CHEP start remains undated in checked evidence. Giosuè’s 2025 essay predates the 2026 student listing.
3. **Edition relationships:** Oualdi’s enriched French edition and Lemercier/Zalc’s revised translation are linked using indexed BnF/author evidence, with direct-retrieval gaps flagged as `inferred` in the consolidated edition-relationship field. Trivellato’s year is secure but exact original-format release day and French translator spelling need rechecking. Amrith’s selected 2020 paperback is not a new original work. Rosental’s first-original year remains `date_unknown`; 2018 identifies the checked English edition.
4. **Partial bibliographic detail:** Balguy’s *Lexique* contribution is identified at volume level; exact entry/pages remain unknown. Several junior records rely on author/institutional bibliographies without accessible full text. Their existence may be verified while a DOI, page span or precise title remains qualified in notes. No argument is supplied for unseen texts.
5. **Support:** no inspected evidence establishes a CHEP funding acknowledgement for these records. The public-debt collection has documented support elsewhere; no support amount or grant total is invented.
6. **Retrieval:** current pages arrived with different reported crawl ages. This is source research, not a live availability audit. Failed Seuil/EHESS/legacy links were cross-checked using authorised alternatives; bot challenges were not bypassed. `robots.txt` and sitemap were unavailable through the tool, and no automated bulk crawl was attempted.

## Remaining queue and stopping rule

The stopping point is completion of the displayed publication list and the three named author-bibliography sections, with the discovered inaccessible leads retained. This is a practical bounded research batch, not an arbitrary top-ten sample. The following work remains before making a centre-wide completeness claim:

- Expand the other 2026 students (Rébecca Mathiot, Giulio Piumelli, Aesa Virely), former fellows including Liane Hewitt, and remaining associates/visitors in explicit person batches. Individual student pages had cache-miss/406 responses; this is not evidence of no publications. Cordelli’s visitor profile was inspected but her career was outside the expansion cohort.
- Sweep HAL/ORCID and current author repositories for the bounded cohort; obtain a newer Balguy bibliography, missing original essay, exact chapter/entry pages, and Giosuè publisher metadata. Reconcile Chaker’s Arabic version chain. No repository-wide search is represented as finished.
- Recheck exact edition details from title pages/colophons, particularly indexed-only relationships. Verify acknowledgements before any claim of CHEP support. Inspect later 2026–2027 publications only in a dated update.
- Retrieve Cambridge’s historical pages and AFHE’s launch account if ordinary access becomes available. Obtain the dated 2022 institutional decision and coordinator handover evidence if needed for publication.
- Ask the responsible institutional functions, later and with authorisation, about intended milestone, affiliation intervals, support acknowledgements, audience demand, editorial ownership, existing hosting and actual available staff time. Those answers cannot be inferred from public pages.

## Deliverable map and verification

- [report.md](report.md): decision brief and analysis (about 1,900 words).
- [anniversary_basis.md](anniversary_basis.md): exact windows, milestones and institutional question.
- [bibliography.csv](bibliography.csv): consolidated 36-record inventory; [selection.csv](selection.csv): 18-work editorial selection.
- [retrospective_draft.md](retrospective_draft.md): 300-word opening, four thematic introductions, six 150-word cards, three junior notices and sourced timeline.
- [celebration_options.md](celebration_options.md): three scenarios and preferred six-week/optional discussion programme.
- [student_research_supplement.csv](student_research_supplement.csv): four separately counted degree-research records.
- [sources.csv](sources.csv): master source register. Component CSVs and notes retain provenance; consolidation scripts reproduce the master files.

Validation checked UTF-8 CSV parsing, unique edition/source IDs, source-ID resolution, the 18 unique selection works, date cutoffs, counts, and the prescribed opening/card word lengths. No covers, photographs or full copyrighted texts are included. Cost figures are estimates with in-kind dependencies, not quotes; proposed contributors have made no commitments. Only P11 files were written.
