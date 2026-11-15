# P04 workshop research handoff

`as_of_date: 2026-11-15`. This subtask contains **21 event records**, comprising **20 events with day-level dates plus one 2020 planned research day with no exact date**. Status counts: **12 documented as held, eight announced, one status unknown**. No event here has a date after the cutoff. Past-dated notices remain `announced` when no positive held evidence was found. No cancellation/postponement has been established.

The 21 rows are a focused census of retrieved CHEP workshop, conference, roundtable and book-event records plus explicit CHEP-supported host events. They are not all Paris economic-history meetings, all Cambridge/Harvard activities, or every event in CHSP's programme. Two date conflicts are retained. Sources use P04-W001–P04-W035; root should remap event IDs W001–W021 to final P04 IDs. Source and event files have UTF-8 CSV with quoted cells. `data.json` is a parallel structured handoff.

## What this branch establishes

- The [5 June 2019 spatial workshop report](https://histecon.fr/en/spatial.html) explicitly says the workshop was held at the CSO and served as CHEP's launch event. Its programme describes brief contributions followed by discussion and a shared bibliography. This supports a public launch in 2019; it does not negate the distinct 2022 establishment wording on today's institutional pages (handled by origins researcher).
- [Recent Centre Events](https://histecon.fr/en/events_recent.html) covers 2019–2026, with a [French counterpart](https://histecon.fr/fr/evenement_recents.html). It contains positive retrospective evidence for several events, but titles/dates alone for others. Its recent French material is partly English. Several older search renditions lack the 2026 entries returned by opening the underlying page. Cite access date and cached/indexed status without claiming live page verification.
- [‘Valuing’ Empires](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2022-11-09-METTREENVALEURLESEMPIRES-6.pdf), [La vie matérielle des déplacés](https://www.sciencespo.fr/histoire/fr/les-formations/les-etudes-doctorales/le-colloque-junior/), [Invisible Actors](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2025-11-27ET28-INVISIBLE-ACTORS-VERSION5.pdf), and [Quand la filiation ne va pas de soi](https://www.sciencespo.fr/histoire/fr/evenements/colloque-junior-quand-la-filiation-ne-va-pas-de-soi-filiations-et-violences-x-xe-xx-ie-siecles/) document CHEP support/co-funding for junior conferences in 2022, 2023, 2025 and 2026. These are support relationships, not evidence that CHEP was sole organizer. They extend the visible intellectual range beyond environmental history.
- Held evidence for the 2022 conference comes from the [Hugo Carlier institutional profile](https://www.sciencespo.fr/histoire/fr/annuaire/carlier-hugo/), which records his conference presentation. Held evidence for the 2023 displaced-persons conference is the retrospective caption on PDF page 4 (printed page 6) of the [2025–26 doctoral guide](https://www.sciencespo.fr/histoire/files/Guidedoctorant2025-2026-15sept.pdf). These establish conference activity, not that every scheduled session took place.
- The [Onur İnal publisher frontmatter](https://assets.cambridge.org/97810096/07261/frontmatter/9781009607261_frontmatter.pdf), acknowledgments pp. xii–xiii, describes attending the 2023 Ottoman workshop and receiving feedback. This is a useful documented example of scholarly benefit without inventing impact metrics or treating the book as CHEP-funded.
- The [EHC archive](https://histecon.fas.harvard.edu/ehc/activities_recent.html) expressly records the 2024 Emotions workshop as held and CHEP-funded, and the June 2025 New Paths workshop as having brought Paris/Cambridge researchers together. The Paris recent-events page additionally records the second JCHE/CHEP workshop on 26 June 2026 as held. Its Cambridge location is inferred from the preceding announcement; the linked programme was inaccessible.
- [State and Capital](https://www.sciencespo.fr/histoire/fr/evenements/state-and-capital-old-problems-new-trajectories/) was announced for 6–7 July 2026, jointly organized with CHSP and Sciences Po's Centre for Political Research. The detailed programme includes climate, monetary policy, state intervention and democracy. No held evidence was located in this branch. Its CHEP [upcoming page](https://histecon.fr/en/events_upcoming.html) survives as indexed past-date announcement; it is not a future event on 15 November 2026.

## Source tree and traversal

```text
CHEP /en/events_sub.html [timeout; www cache miss]
└── /fr/activites_sub.html [cache miss; www inaccessible]
CHEP /en/events_recent.html [retrieved; no pagination or older archive link in returned body]
├── /fr/evenement_recents.html [retrieved; bilingual comparison]
├── /en/spatial.html [retrieved full report/programme]
│   └── afhe.hypotheses.org/y-a-t-il-un-tournant-spatial-en-histoire-economique [challenge]
├── /ottoman/index.html; /participants.html [retrieved]
│   └── /schedule.html; /organisers.html [failed]
├── /emotions_climate_environment/index.html [retrieved]
│   └── /schedule.html; /papers/papers.html [failed; host programme substituted]
├── /belonging/index.html; /participants.html [retrieved]
│   └── /programme.html [failed; IHMC indexed programme substituted]
├── Cambridge /new_paths/; /JCHE_CHEP_Workshop/index.html [failed]
├── Sciences Po /book-presentation-jonathan-levy/ [retrieved]
└── Climate and Capitalism reading group [handed to root; not counted here]
CHEP /en/events_upcoming.html [indexed body retrieved; direct open cache miss]
└── Sciences Po /state-and-capital-old-problems-new-trajectories/ [retrieved]
Sciences Po junior-colloquium FR and EN indexes [retrieved; 2015–2025 browsed]
├── 2022 Valuing Empires PDF [text retrieved]
├── 2023 displaced-persons linked programme [failed]
│   └── doctoral guide 2025–2026 [PDF text retrospective caption retrieved]
├── 2024 after-violence PDF [zero text; screenshot failed; no CHEP evidence on index]
├── 2025 Peripheral Archives PDF [retrieved; no CHEP support in text]
├── 2025 Invisible Actors PDF [retrieved; explicit CHEP co-funding]
└── 2026 filiation event [discovered by targeted search; full programme retrieved]
Partner crosscheck: Harvard /ehc/activities_recent.html [retrieved]
Participant-held evidence: Sciences Po Carlier profile; CUP İnal frontmatter [retrieved]
Primary 2020 context: Sciences Po 10 March 2020 CS minutes [retrieved pp14–15]
```

Targeted searches included CHEP workshop/conference terms with 2019, 2020, 2022, 2025, 2026; site-specific programme URLs; exact event titles; and Sciences Po CHEP/colloque terms. Search results were opened; where open failed but a full indexed rendition was available, the source register expressly identifies that limit. Direct Python HTTP access failed at DNS resolution. A robots.txt check could not be completed, so there was no bulk crawl; web retrievals were targeted. PDF extraction was used for metadata; attempted screenshots failed or produced no usable image, so no claims depend on unreadable visual logos.

## Conflicts and counting decisions

1. **Belonging:** CHEP FR/EN index says 18–19 September 2023. The [IHMC institutional programme](https://ihmc.ens.psl.eu/belonging-membership-and-affiliation.html), published 16 September 2024, explicitly says Wednesday 18 and Thursday 19 September 2024. That detailed source is the working date, but was available as a full indexed rendition with direct-open 502. Row stays `conflicting`; one event, not two. Cambridge September 2023 precursor is background, not a Paris event automatically counted here.
2. **Invisible Actors:** both junior-colloquium indexes say 26–27 November 2025. Their linked programme says 27–28 November in its header and daily schedule. Use programme dates while retaining `conflicting`; do not claim postponement without evidence.
3. **Emotions:** host event display says 11:00–19:45 while detailed programme spans 09:00–17:45. Day is consistent (24 May 2024); inventory stores only dates, not disputed hours.
4. **2026 coordinator label:** State and Capital programme calls David Todd coordinator. This is a dated programme label, not proof of the role at the current cutoff. Origins researcher has the lead.
5. **2020 law/economics day:** March 2020 minutes identify an annual research-day theme but no exact date or formal title. Searches did not find a matching programme. W021 is a descriptive-title record, year precision, `status unknown`. No inference that COVID cancelled it.
6. Series and session counting: one multi-day conference = one event. Parent reading-group pages and the 28 June 2023 Moscona seminar are not added here; root covers them. Speakers fields distinguish scheduled participants, authors, chairs or discussants where sources permit. A participant roster does not establish every person presented or attended.

## Exclusions and remaining queue

Wider economic-history listing pages [current French agenda](https://histecon.fr/fr/agenda.html) and [English archive](https://histecon.fr/en/econhist_paris_archive.html) were discovered as community advertising, with root responsible for its corpus policy. Their existence does not attribute PSE/EHESS/Paris-wide events to CHEP. Whole Cambridge/Harvard programmes, ordinary CHSP events and the pre-2019 junior-colloquium archive were excluded without an explicit CHEP link. Peripheral Archives 2025 and after-violence 2024 have no CHEP support established by the checked index/text; inclusion would need additional evidence.

Priority retrieval queue: inaccessible main workshops navigation; Cambridge 2025/2026 workshop programmes; Ottoman schedule and organizers; Belonging programme/direct IHMC page; displaced-persons 2023 programme; the precise date/outcome of the 2020 law/economics day. No public recordings were found on inspected relevant pages; this is not proof none exist. Location/language remain explicit missing values where unsupported. Internal organizers' calendars, final programmes and post-event reports could resolve occurrence and dates. Attendance, audience composition, budgets and demand for new activities remain unverified and should not be filled from inference.

This branch's yearly record counts (including W021 year-only plan): 2019 1; 2020 2; 2021 2; 2022 2; 2023 4; 2024 3; 2025 3; 2026 4. Counts measure this checked corpus, not total institutional production. No total-corpus percentage is defensible.
