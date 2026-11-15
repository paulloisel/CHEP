# Data dictionary and reuse rules

`as_of_date: 2026-11-15` (America/Los_Angeles). Research draft; no publication or contact has been undertaken.

- **people.csv** contains one identity per person. Categories can contain several semicolon-separated values. It deliberately includes separately labelled historical affiliates, host-unit staff, partner governance, and selected event/publication participants. It is **not a list of current CHEP members**. `institution` reports the sourced institutional context; a dated historical affiliation is not silently updated to today.
- **roles.csv** contains one record per sourced role/category assertion or distinct period. Parallel labels for the same affiliation are preserved (for example fellow/postdoctoral researcher and research student/scholarship holder); rows must not be counted as distinct appointments. `organisation` is an `organisation_id`, not free text. `role_exact` preserves the source label or relevant source wording; descriptive participation labels are explicitly qualified. `date_precision` distinguishes an appointment period from a dated attestation. `date_unknown` in `end_date` does **not** mean the role is ongoing. Current/historical qualification is recorded in `date_precision`, `people.current_status`, and evidence notes.
- **organisations.csv** distinguishes centres, host institutions/units, committees and programmes. A committee name on navigation establishes the body/page label, not its current composition or legal status. A thematic programme is not a fourth centre or a parent institution.
- **relationships.csv** uses existing person/organisation IDs for both endpoints. Relationship labels are descriptive and directed for readability. Neither arrows nor shared support functions imply line management. Observation dates are not appointment dates. Only evidenced host, membership, role, collaboration and historical-support relations are included.
- **sources.csv** records direct URLs, titles, owners, source dates, access dates, purpose, and retrieval limitations. Where two runs reached the same URL, one source record is retained and the source-ID crosswalk preserves the duplicate IDs. Search-result text alone is not treated as a verified present-day affiliation. Retrieved indexed copies are identified; their crawl ages are neither source dates nor archived snapshot dates.
- **evidence_notes.csv** supplies record-level locators, uncertainty and source wording where the required table schema has no notes column. **identifiers.csv** records only observed canonical profile URLs or identifiers; absence of an ORCID lookup is not evidence that a person has no ORCID.
- **coverage.md** is the authoritative scope and remaining queue. **organigram.md** is a readable subset of the entity graph, separating formal functions from partnerships. The CSV tables retain additional dated history.

## Evidence and missing values

`verified`: the named relationship or fact is explicitly stated in a retrieved responsible source, within the record's temporal scope. This does not certify employment status on the day of access.

`inferred`: an analytic connection or cautious interpretation is explicitly marked. Proposed thematic links belong in the report, not as established collaboration edges.

`conflicting`: retrieved sources disagree in a material way; alternatives and practical consequences remain visible.

`unverified`: the relevant source/claim could not be checked. These records must not populate a confirmed-current public roster.

`not_found_publicly`: not located in the declared checked corpus. `not_applicable`: the field does not apply. `date_unknown`: effective/source date not established. No missing value means zero.

## Editing protocol

Keep stable IDs. Add a dated role when status changes rather than rewriting history. Check both the affiliation evidence and the individual's institutional profile. Store the exact date precision given by the source. Do not infer continued tenure from an empty end date, membership from a book/event appearance, employment from a website credit, or a reporting line from a partnership. Before publishing a current directory, obtain institutional confirmation of category definitions, appointment periods, the current committee list and the intended contact/maintenance function. This is an editorial dependency, not a claim that private approval is needed to conduct public research.
