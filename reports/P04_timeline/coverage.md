# P04 coverage, evidence rules and remaining questions

**as_of_date: 2026-11-15.** Research followed the entire shared brief and P04. `Summary.md` contained the four institutional starting URLs and no additional substantive instructions. No other report was needed or used. All outputs are confined to `reports/P04_timeline/`; no invitations, subscriptions, website edits or publication occurred.

## Corpus and boundaries

The event census covers the earliest precisely dated CHEP activity located, **5 June 2019**, through **15 November 2026**, with future announcements retained separately through **4 June 2027**. Institutional history also retains an earlier, imprecise phase suggested by the 2020 council minutes. It includes:

- Paris events explicitly organised, hosted, supported or listed as Centre events, plus explicitly supported Sciences Po conferences.
- All visible sessions in the CHEP-supported **Histoires de la vie économique** calendar, 2022–23 through 2026–27.
- All visible sessions in the linked **La matière du politique** calendar, 2021–22 through 2026–27, labelled linked/advertised rather than automatically CHEP-organised.
- The explicitly joint Cambridge/Harvard/Paris online seminar from its first archived entry in May 2020.
- Two day-dated Climate and Capitalism sessions and one season-only plan; three unverified atelier leads are retained outside the census totals.

Whole Harvard, Cambridge and CHSP programmes, publication appearances by affiliates, and ordinary regional economic-history notices are excluded without an explicit CHEP or included-series connection. The regional agenda is used for discovery and discrepancy checking, not enumerated as CHEP output. Personal affiliations alone do not prove institutional organisation. No public evidence of an event is treated as evidence of its audience composition.

This scope supports a **census within the enumerated calendars and checked event branches**, with the limitations below. It does not support a claim to all events ever advertised by CHEP or a complete institutional history.

## Counts and denominator

- **151 rows in events.csv:** **148 census records** and **3 unverified atelier leads** (`counted_in_census=false`).
- **148 census records:** 25 Paris Centre/standalone/reading-workshop records; 39 explicitly supported economic-life seminar sessions; 52 linked host-series sessions; 32 joint online sessions.
- **Status:** 32 documented as held; 114 announced; one status unknown (2020 year-only plan); one cancelled/postponed (replacement date unknown).
- **Future:** 12 census records after the cutoff, all announcements. Nine fall in 2027 and three in late 2026. One further postponed session has no replacement date.
- **Date precision:** two census records have only year/season precision (2020 law/economics plan and spring-2025 Tarbell discussion). All others except the undated postponement have a day or day range. Three unverified atelier leads also have candidate day dates.
- **28 milestones** in timeline.csv; **15 selected entries** in timeline.md, sometimes grouping closely related milestones.
- **129 source-observation rows covering 114 distinct URLs.** Duplicate URLs preserve observations made in different research branches or cached renditions; they are not independent corroboration. All access dates are 15 November 2026.

The 32 held records consist of 12 Paris workshop/conference/book records and 20 online-network records. No session in the two host seminar calendars was upgraded solely because of its past date or a general retrospective description of the series.

| Year | Records | Documented as held | Announced | Status unknown / postponed | Future subset |
|---|---:|---:|---:|---:|---:|
| 2019 | 1 | 1 | 0 | 0 | 0 |
| 2020 | 8 | 1 | 6 | 1 | 0 |
| 2021 | 14 | 7 | 7 | 0 | 0 |
| 2022 | 16 | 5 | 11 | 0 | 0 |
| 2023 | 28 | 7 | 21 | 0 | 0 |
| 2024 | 26 | 4 | 22 | 0 | 0 |
| 2025 | 23 | 4 | 19 | 0 | 0 |
| 2026 | 22 | 3 | 19 | 0 | 3 |
| 2027 | 9 | 0 | 9 | 0 | 9 |
| unknown | 1 | 0 | 0 | 1 | 0 |

There is no known denominator for all CHEP activity, so no corpus-completeness percentage is reported. Year totals measure visibility under this method, not institutional growth or contraction.

## Task-specific source tree

Status terms below: **R** opened/parsed public institutional content; **I** full indexed rendition only; **F** failed/incomplete retrieval. All R content is still subject to the retrieval tool’s cache labels; R does not mean independently verified live-origin HTTP.

- **Paris home/history**
  - [English home](https://www.histecon.fr/en/) — R, P04-H001/S014; 2019/2022 wording, navigation.
  - [French directory home](https://histecon.fr/fr/) — R, H005; [French index route](https://histecon.fr/fr/index.html) — R but old indexed version, H004/S013.
  - [Sciences Po English overview](https://www.sciencespo.fr/histoire/en/research/centre-for-history-and-economics-in-paris-chep/) and [French overview](https://www.sciencespo.fr/histoire/fr/recherche/centre-for-history-and-economics-paris-chep/) — R, H003/H008.
  - [Organisation](https://histecon.fr/en/organisation.html), [fellows](https://histecon.fr/en/research_fellows.html), [past fellows](https://histecon.fr/en/research_fellows_past.html), [2026 students](https://histecon.fr/en/research_students.html), [visitors](https://histecon.fr/en/research_visitors.html) — R for dates and history; no exhaustive P01 people directory attempted.
  - [Previous students](https://histecon.fr/en/research_students_previous.html) — F; cohort history remains partial.
  - [Announcements archive](https://histecon.fr/en/announcements_archive.html), [grants](https://histecon.fr/en/research_grants.html) — R for programme and cohort milestones; no full funding census.
  - [Projects index](https://histecon.fr/en/projects.html) — F, including aliases; specific EHC and state/economy evidence substituted.
- **Institutional records and dated corroboration**
  - Sciences Po [2020 council minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2020/2020_03_10_CSFR.pdf), pp.14–15; [2021 council minutes](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2021/2021_10_12_CSFR.pdf), p.10; [2022 research report](https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/LaRechercheaSciencesPo-2022.pdf), printed p.129 — R text, H031/H010/H011.
  - [2026 award announcement](https://www.sciencespo.fr/ecole-recherche/fr/actualites/quatre-jeunes-chercheurs-histoire-laureats-bourse-chep-2026/) and [2025 Todd interview](https://www.sciencespo.fr/ecole-recherche/fr/actualites/entretien-avec-david-todd-directeur-des-etudes-en-histoire/) — R, H006/H007.
  - [Todd profile](https://www.sciencespo.fr/histoire/fr/chercheur/David%20Todd/86024.html), [host visitor archive](https://www.sciencespo.fr/histoire/fr/le-centre/chercheurs/chercheurs-invites/), [career archive](https://www.sciencespo.fr/histoire/en/the-centre/professional-careers/) — R, role discrepancy and dated cohort/visitor evidence.
- **Paris workshops and conferences**
  - [Events navigation](https://histecon.fr/en/events_sub.html) and [French navigation](https://histecon.fr/fr/activites_sub.html) — F; [recent English events](https://histecon.fr/en/events_recent.html) and [French events](https://histecon.fr/fr/evenement_recents.html) — R, all relevant 2019–2026 entries processed; no pagination or deeper older archive link found in returned bodies.
  - [Upcoming events](https://histecon.fr/en/events_upcoming.html) — I; State and Capital is past-dated at cutoff despite the page label.
  - [2019 spatial workshop](https://histecon.fr/en/spatial.html) — R, report and programme; linked [AFHE report](https://afhe.hypotheses.org/y-a-t-il-un-tournant-spatial-en-histoire-economique) — challenge, not bypassed.
  - [Ottoman workshop](https://histecon.fr/ottoman/index.html), [participants](https://histecon.fr/ottoman/participants.html) — R; schedule/organisers F. [Publisher acknowledgments](https://assets.cambridge.org/97810096/07261/frontmatter/9781009607261_frontmatter.pdf), pp.xii–xiii — R, evidence of an actual scholarly exchange.
  - [Emotions workshop](https://histecon.fr/emotions_climate_environment/index.html) — R; schedule/papers F; [Sciences Po programme](https://www.sciencespo.fr/histoire/en/events/emotions-climate-and-the-environment-historical-perspectives-18th-21st-centuries/) — R.
  - [Belonging](https://histecon.fr/belonging/index.html), [participants](https://histecon.fr/belonging/participants.html) — R; CHEP programme F; [IHMC programme](https://ihmc.ens.psl.eu/belonging-membership-and-affiliation.html) — I, direct 502.
  - [Junior colloquium archive](https://www.sciencespo.fr/histoire/fr/les-formations/les-etudes-doctorales/le-colloque-junior/) — R, visible 2015–2025 list screened for explicit CHEP connections. 2022, 2023, 2025 and separately discovered 2026 entries included.
  - [Valuing Empires PDF](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2022-11-09-METTREENVALEURLESEMPIRES-6.pdf), [Invisible Actors PDF](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2025-11-27ET28-INVISIBLE-ACTORS-VERSION5.pdf), [filiation programme](https://www.sciencespo.fr/histoire/fr/evenements/colloque-junior-quand-la-filiation-ne-va-pas-de-soi-filiations-et-violences-x-xe-xx-ie-siecles/) — R.
  - Displacement programme F; [2025–26 doctoral guide](https://www.sciencespo.fr/histoire/files/Guidedoctorant2025-2026-15sept.pdf), PDF p.4 / printed p.6 — R, retrospective caption.
  - 2024 after-violence and 2025 Peripheral Archives programmes screened; no sufficient CHEP connection established. The former PDF returned no text and screenshot failed; the latter explicit support did not identify CHEP. Exclusion is provisional, not a claim of no support.
- **Seminar branches**
  - [CHEP seminars](https://www.histecon.fr/en/seminars.html) — I; [French route](https://histecon.fr/fr/seminaires.html) — F.
  - [Histoires de la vie économique](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/histoires-de-la-vie-economique/) — R, all five academic-year sections 2022–23 to 2026–27 processed. Three reissued dates merged; unknown replacement retained.
  - [La matière du politique](https://www.sciencespo.fr/histoire/fr/recherche/seminaires/seminaire-des-axes-et-des-domaines/la-matiere-du-politique/) — R, all six academic-year sections 2021–22 to 2026–27 processed, including internal meetings. The two-paper session on 7 April 2023 counts once.
  - [Climate and Capitalism readings/dates](https://histecon.fr/climate_capitalism/readings.html) — R after targeted discovery; parent/contact routes F. Two dated meetings plus one season-only plan; readings without meeting plans excluded.
  - [Regional agenda](https://histecon.fr/fr/agenda.html) and [regional archive](https://histecon.fr/en/econhist_paris_archive.html) — R, scope/interruptions checked and relevant series leads compared. No full transcription of regional external events.
- **Harvard and Cambridge**
  - [Harvard Events](https://histecon.fas.harvard.edu/events_main.html), [seminars](https://histecon.fas.harvard.edu/seminars.htm), [online home](https://histecon.fas.harvard.edu/seminars/index.html), [past online seminars](https://histecon.fas.harvard.edu/seminars/past_seminars.html) — R. All 31 past-index entries plus Adelman 2026 extracted; all 28 distinct event-detail links attempted. Four early entries lacked separate detail pages. No pagination found.
  - [Harvard recent events](https://histecon.fas.harvard.edu/recent_events.html) — relevant Paris mentions and 2018–2026 leads checked, not an all-Harvard census; [news archive](https://histecon.fas.harvard.edu/news.html) — R for undated Paris-project announcement.
  - [EHC programme](https://histecon.fas.harvard.edu/ehc/) and [events archive](https://histecon.fas.harvard.edu/ehc/activities_recent.html) — R, relevant 2022–2026 material processed. Cambridge-only reading-group sessions excluded without a specific Paris connection.
  - [Cambridge home](https://www.histecon.magd.cam.ac.uk/), [historic Paris project](https://www.histecon.magd.cam.ac.uk/chep/), [New Paths](https://www.histecon.magd.cam.ac.uk/new_paths/), [2026 workshop](https://www.histecon.magd.cam.ac.uk/JCHE_CHEP_Workshop/index.html) — F; Paris/Harvard accounts supply partial corroboration.

## Evidence and reconciliation decisions

1. **Origin:** official current 2019/2022 formulation retained alongside the 2019 launch and imprecise earlier-phase evidence. No exact legal date invented.
2. **Leadership:** Levy is the current dedicated-page title; Todd interview/profile/July-2026 programme labels remain in the evidence trail. Claire Lemercier’s historical co-coordination is not rewritten into a single-coordinator succession.
3. **Belonging:** use 18–19 September 2024 as the working date from the dated detailed IHMC programme; CHEP indexes say 2023. One row, `conflicting`, not two events.
4. **Invisible Actors:** use 27–28 November 2025 from the detailed PDF; archive says 26–27. One row, `conflicting`; a difference is not proof of postponement.
5. **Economic-life revisions:** 28 March 2023 was postponed to autumn and merged with 21 September; the regional archive’s 12 September variant is noted. May 2023 moved from 16 to 30; March 2025 from 11 to 25. Sukriti Issar’s April 2025 title varies across sources but the same date/speaker identifies one event.
6. **Material-politics typo:** “29 mars 2924” is normalized to 29 March 2024 with `inferred` status. Calendar-section context supports that interpretation; an institutional correction remains desirable.
7. **Languages and people:** no spoken language inferred from title language. A reading’s author is not a speaker. Author subjects in book celebrations are distinguished from named commentators; workshop participant rosters are labelled as such rather than attendance claims.
8. **Occurrence:** retrospective statements or individual retrospective accounts support “documented as held.” A conference participant account verifies activity occurred, not completion of every scheduled paper. No event is assumed cancelled because of COVID. General retrospective series prose does not upgrade every session.
9. **Temporal classification:** retained “upcoming” web labels are overridden by the actual cutoff for historical/future sorting, while original occurrence status remains separate. Record dates are event dates; source publication/validation dates remain in sources.csv.
10. **Role:** current seminar-page links establish programme publicity, not historical session-specific funding. Supported, co-organised, listed and network relationships remain separate fields/groupings. This is why the full 148 must not be called “148 CHEP-organised events.”

## Reuse and data dictionary

The requested columns lead each CSV; additional audit fields follow. IDs `P04-E###` and `P04-M###` identify final records. `source_record_id` preserves the subtask crosswalk, and `source_ids` joins to sources.csv. `source_urls` provides direct URLs without requiring a lookup. Source titles and access dates are in sources.csv; the common evidence cutoff is also repeated on every event and milestone.

- `date_start`/`date_end` retain ISO dates, years, seasons or `date_unknown`; never treat a year-only value as 1 January.
- `date_precision` explains retrospective/observed-by milestones. For undated current roles, an end value equal to the cutoff is an observation bound, not tenure end.
- `status` describes occurrence evidence; `evidence_status` describes the record’s verification, and is one of verified/inferred/conflicting/unverified.
- `temporal_scope` separates historical dates, future dates and unknown rescheduling.
- `counted_in_census` excludes only the three indexed-only atelier leads. A verified announcement is not a verified held event.
- `not_found_publicly` means absent from the checked material, not non-existent. `not_applicable` and `date_unknown` are used where appropriate. Attendance, budgets and demand are not imputed.
- Proposed interventions in report.md are estimates, not institutional commitments. No image, quotation, recording or other rights-dependent reuse is proposed as ready for publication.

## Retrieval limits and next steps

Robots and sitemap endpoints could not be retrieved. A direct public HTTP check returned 406 after the initial sandbox DNS limitation; no bulk crawl or restriction bypass was attempted. Retrieval was through bounded web requests, with source responses retained during work. Searches included CHEP workshop/conference plus years, exact event titles, Sciences Po CHEP/colloque, seminar titles, and official programme routes. Full scholarly texts were not required. PDF text was usable for several programmes and institutional reports; screenshots failed for some documents, so unreadable logos are not evidence.

No dated web-archive snapshot was recovered. “Crawled” timestamps are recorded as retrieval metadata, never treated as publication dates. When a search extract and an opened page disagreed, the difference was investigated and preserved rather than used to diagnose the live site. An indexed historical account can support a historical claim with a retrieval caveat; it cannot independently establish current live-page condition.

Priority queue:

| Question or retrieval | Next useful step | Information owner, proposed by function |
|---|---|---|
| What did the early network phase, 2019 collaboration/launch, and 2022 establishment each mean? | Locate founding agreements, administrative record or an approved dated history. | Academic coordination and institutional archives |
| When did coordination change? | Obtain appointment/handover dates; reconcile profile and programme labels. | Academic coordination / research support |
| Did the 2020 planned law/economics day occur? | Recover final programme, cancellation or post-event note; retain unknown meanwhile. | Historical event organisers / archives |
| Belonging and Invisible Actors date conflicts | Check final programmes against an organiser’s record; preserve correction history. | Event convenors |
| Cambridge 2025/2026 workshop details; Ottoman and displacement programmes | Recover the inaccessible programmes or dated official snapshots. | Partner coordination / programme owners |
| Three atelier session leads and previous student cohorts | Find archived notices and dated award lists. | Research support / early-career convenors |
| Announcements without held evidence, including recent 2026 events | Request brief factual confirmation through an authorised later process; nothing sent in this run. | Event convenors |
| Exact EHC/state-programme start dates and institutional reporting boundary | Confirm programme inception and whether network events should appear in a separate annual subtotal. | Programme coordination |
| Languages, rooms, attendance, costs, demand | Internal records or proportionate future feedback; leave unknown here. | Relevant event/research support functions |

The following source observations had failed, indexed-only, or incomplete retrieval. Their full evidence notes remain in sources.csv. Repeated aliases and source observations are retained deliberately.

| Source | Retrieval status |
|---|---|
| [P04-H010](https://www.sciencespo.fr/sites/default/files/cd_cp/cs/2021/2021_10_12_CSFR.pdf) | PDF text retrieved; screenshot failed cache miss |
| [P04-H011](https://www.sciencespo.fr/cevipof/sites/sciencespo.fr.cevipof/files/LaRechercheaSciencesPo-2022.pdf) | PDF text retrieved; screenshot failed cache miss |
| [P04-H016](https://histecon.fr/en/research_students_previous.html) | failed: cache miss/not accessible; www and French aliases also attempted |
| [P04-H023](https://www.histecon.magd.cam.ac.uk/chep/) | failed cache miss; /index.html and non-www aliases also failed |
| [P04-H024](https://histecon.fr/en/projects.html) | failed 406; www alias cache miss; French projects route inaccessible |
| [P04-H025](https://afhe.hypotheses.org/y-a-t-il-un-tournant-spatial-en-histoire-economique) | retrieved challenge page only; underlying report unverified |
| [P04-H027](https://www.sciencespo.fr/recherche/fr/content/la-soufflerie.html) | failed cache miss |
| [P04-N009](https://www.histecon.magd.cam.ac.uk/chep/) | failed web open: cache miss; non-www alias inaccessible |
| [P04-N010](https://www.histecon.magd.cam.ac.uk/) | failed web open: 403 Forbidden |
| [P04-N011](https://www.histecon.magd.cam.ac.uk/new_paths/) | failed web open: error fetching |
| [P04-N012](https://histecon.fas.harvard.edu/robots.txt) | failed web open; shell network DNS unavailable |
| [P04-N013](https://histecon.fas.harvard.edu/sitemap.xml) | failed web open: inaccessible |
| [P04-N104](https://histecon.fas.harvard.edu/seminars/ranganathan.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N106](https://histecon.fas.harvard.edu/seminars/amrith.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N107](https://histecon.fas.harvard.edu/seminars/warde.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N109](https://histecon.fas.harvard.edu/seminars/levy.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N113](https://histecon.fas.harvard.edu/seminars/ogle.html) | full indexed search text retrieved; direct opens failed; explicitly says seminar took place 13 October 2021 |
| [P04-N114](https://histecon.fas.harvard.edu/seminars/bowie.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N118](https://histecon.fas.harvard.edu/seminars/kala.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N126](https://histecon.fas.harvard.edu/seminars/kim2.html) | detail retrieval failed; non-www and www attempts; metadata verified on opened past-seminars index |
| [P04-N203](https://www.histecon.magd.cam.ac.uk/JCHE_CHEP_Workshop/index.html) | failed web open: cache miss |
| [P04-N204](https://histecon.fr/climate_capitalism/contact.html) | failed web open: cache miss |
| [P04-S003](https://www.histecon.fr/en/seminars.html) | indexed page body retrieved; direct opens cache miss |
| [P04-S009](https://histecon.fr/robots.txt) | web unavailable; direct request HTTP 406 |
| [P04-S010](https://histecon.fr/sitemap.xml) | web unavailable |
| [P04-S011](https://histecon.fr/en/projects.html) | direct URL HTTP 406; www alias cache miss |
| [P04-S012](https://histecon.fr/fr/seminaires.html) | HTTP 406; www alias cache miss |
| [P04-W009](https://ihmc.ens.psl.eu/belonging-membership-and-affiliation.html) | Full indexed page text retrieved by search; underlying direct open attempted and failed 502; conflict retained |
| [P04-W014](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2025-11-27ET28-INVISIBLE-ACTORS-VERSION5.pdf) | PDF text retrieved (1 page); screenshot attempted but cache miss |
| [P04-W016](https://www.sciencespo.fr/histoire/files/Guidedoctorant2025-2026-15sept.pdf) | PDF text retrieved (9 pages); screenshot attempted but cache miss; guide has inherited 2024–25 text, no claim based on undated current roles |
| [P04-W020](https://histecon.fr/en/events_upcoming.html) | Full indexed text retrieved by search; direct open cache miss; search rendition crawled 3 months ago |
| [P04-W022](https://histecon.fr/en/events_sub.html) | Failed: timeout; www alias failed cache miss |
| [P04-W023](https://histecon.fr/fr/activites_sub.html) | Failed: cache miss; www alias inaccessible |
| [P04-W024](https://www.histecon.magd.cam.ac.uk/JCHE_CHEP_Workshop/index.html) | Failed: cache miss; non-www alias inaccessible |
| [P04-W025](https://www.histecon.magd.cam.ac.uk/new_paths/) | Failed: error fetching; non-www alias inaccessible |
| [P04-W026](https://histecon.fr/ottoman/schedule.html) | Failed: cache miss; www alias inaccessible |
| [P04-W027](https://histecon.fr/ottoman/organisers.html) | Failed: cache miss |
| [P04-W028](https://histecon.fr/belonging/programme.html) | Failed: error fetching; www alias inaccessible |
| [P04-W029](https://histecon.fr/emotions_climate_environment/schedule.html) | Failed: cache miss; www alias inaccessible |
| [P04-W030](https://www.sciencespo.fr/agenda/chsp/fr/event/La%2Bvie%2Bmat%C3%A9rielle%2Bdes%2Bd%C3%A9plac%C3%A9s?event=4934) | Failed: cache miss |
| [P04-W031](https://afhe.hypotheses.org/y-a-t-il-un-tournant-spatial-en-histoire-economique) | Challenge page retrieved; substantive content blocked by Anubis |
| [P04-W033](https://www.sciencespo.fr/histoire/sites/sciencespo.fr.histoire/files/2024-11-28et29-APRESLAVIOLENCE-DEF.pdf) | PDF metadata retrieved with zero text; screenshot failed cache miss |

## Validation performed

CSV parsing, required headers, nonempty cells, unique record/source IDs, source joins and access dates were checked. Calendar counts, day/range handling, future cutoffs and status subtotals were recomputed from the final files. An independent pass compared all 91 Paris calendar rows with the retrieved official text; a further standalone Moscona seminar was added from the event index. Cross-posted workshops and climate-programme parent descriptions were not counted twice. Rescheduled economic-life sessions were merged. The final narrative, tables and source links were reviewed together; unresolved issues are retained explicitly rather than silently repaired.

