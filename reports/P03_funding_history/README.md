# P03 — Deliverables and data conventions

**as_of_date: 2026-11-15.** Authoritative deliverables are the files in this directory root. `_research/` retains intermediate evidence and assembly scripts; its branch counts and provisional classifications may predate final reconciliation.

Start with [report.md](report.md), the decision brief, analysis, funding-flow diagram and draft support box.

| File | Contents |
|---|---|
| [funding_ledger.csv](funding_ledger.csv) | Historical awards, appointments, explicit funding acknowledgements and the institutional receipt; all required P03 fields, plus reconciliation fields |
| [cohort.csv](cohort.csv) | Independently established Paris-connected people, inclusion categories, affiliation dates and evidence |
| [funding_coverage.csv](funding_coverage.csv) | Person, scheme, project, institution and year checks; zero findings is not proof of no funding |
| [calls_and_unverified_leads.csv](calls_and_unverified_leads.csv) | Current/historical calls, planned support, accounting context, generic support and unresolved award/amount leads |
| [sources.csv](sources.csv) | Direct URLs, titles, ownership, source dates, access date, evidence supported and retrieval qualifications |
| [coverage.md](coverage.md) | Source tree, counts, years checked, exclusions, conflicts, access failures and remaining queue |
| [administrator_questions.md](administrator_questions.md) | Targeted draft request for the missing institutional records; not sent |
| [source_id_crosswalk.csv](source_id_crosswalk.csv) | Original-to-canonical source IDs after exact-URL deduplication |
| [award_groups.csv](award_groups.csv) | One collective 2019 economics prize underlying two in-scope recipient-share records |
| [validation.json](validation.json) | Final record counts and referential/arithmetic checks |

## Reading the ledger

- `funding_id` is the stable local record identifier. `parent_award_id` identifies a parent **ledger** record only where the relationship is documented. SLAVEVOICES allocations are children of its project total. A missing upstream funder is not invented.
- `relationship_category` has three values: `incoming_institutional_project_funding`; `CHEP_administered_or_distributed_support`; and `independent_awards_to_CHEP_connected_researchers`. The last includes external projects legally received by institutions, not necessarily money paid to the named individual. `relationship_detail` retains the research branch's narrower original label.
- `funder`, `recipient`, `administrator`, `beneficiary`, and `project` are distinct. Recipient means the stated recipient; wording explicitly flags when a legal entity is not established. A scheme name alone does not prove the legal administrator.
- `award_date`, `start_date` and `end_date` preserve reported precision: `YYYY`, `YYYY-MM` or `YYYY-MM-DD`. Award announcement, selection and funding period are not automatically the same. Source publication dates are in `sources.csv`; a reporting year or archive date is labelled where exact publication date is unavailable. The 2022 receipt is dated in its evidence note, not misrepresented as a known grant start date.
- `amount` contains a numeric string only where the source supplies a figure. `amount_basis` governs its interpretation. An amount may be known while its ISO currency is not stated; `$` does not automatically establish USD or AUD. Call ceilings, annual advertised salaries and the €0.9m accounting entry are outside the award ledger.
- `period_category=earlier_independent_award` identifies awards or starts before 2019. Other records may still precede the individual's documented Paris connection; `CHEP_connection` preserves that distinction. No retrospective funding attribution is intended.
- `evidence_status` is `verified`, `inferred`, `conflicting` or `unverified`. It applies to the assertion explained in `evidence_note` and `CHEP_connection`. For example, SLAVEVOICES amounts are verified while its end date conflicts; TRADEDEPRESSION has an inferred person–project match.
- `award_or_call_status` distinguishes announcements, accepted appointments, acknowledged funding and payments. A verified award is not evidence of expenditure. `counting_treatment` makes non-additive relationships explicit. The two 2019 Nobel recipient shares have a common `award_group_id`, not two independent prize pools.
- `person_ids` resolve to the cohort; they identify Paris-connected people, not every collaborator or legal recipient. `source_ids` resolve to the canonical source register. Several sources may support different aspects of one record.

## Missing values and counts

`not_found_publicly` means the checked public corpus did not establish the field. `date_unknown` means no defensible date was recovered. `not_applicable` means the field does not apply. None means zero. For a wholly unknown upstream award, `parent_award_id=not_found_publicly` differs from an independent record with no applicable parent.

Person coverage `findings_count` counts that person's distinct ledger records after reconciliation, excluding SLAVEVOICES institutional components. Scheme, year and project rows describe their stated branch; their counts overlap and must not be added across the coverage table. The 2020 year row counts named selections, while a separate aggregate record reports approximately six bursaries; this is a discovery count, not a combined award population.

The valid numerical reconciliation is €421,690 + €1,578,285 = €1,999,975 within SLAVEVOICES. No cross-project, cross-currency, annual-spending or all-time CHEP total is supplied. Source access dates are 15 November 2026; indexed crawl ages do not establish publication dates or authenticated historical snapshots.

## Reproducing the assembly

From the CHEP workspace, run `python3 reports/P03_funding_history/_research/consolidate.py` and then `python3 reports/P03_funding_history/_research/write_coverage.py`. These assemble the already collected branch CSVs and regenerate the root tables, validation and coverage; they do not fetch web sources. The report and administrator questions are editorial outputs and are not regenerated by those scripts.
