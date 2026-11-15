# Verification record

As of 2026-11-15. Checks concern the delivered synthesis, not certification of the institution or every inherited source.

- Required deliverables and shared source/coverage files are present and nonempty. The proposal CSV has the exact ten requested columns. CSV parsing, rectangularity and unique source/reconciliation/input IDs were checked.
- All 297 input files have links in the manifest. Required input-file existence was compared with the prompt pack; no named required file is missing. All writes were confined to P13. Original sizes were unchanged; modified times compared within one microsecond, with smaller timestamp differences recorded in the machine results. This is a metadata check, not an exhaustive content checksum.
- Local Markdown targets and crosswalk input-file paths were checked. Original master-source IDs remain represented. Edition IDs do not map to multiple underlying works. Source observations, canonical source chains and entity IDs have distinct namespaces.
- Portfolio arithmetic independently reconciles to 37, 52 and 52.5 hours, with every scheduled week at or below five. The recommended action totals are 10 + 18 + 9 = 37. The SLAVEVOICES beneficiary allocations reconcile to the funder parent without addition to it.
- CSV tables were authored and read back through the bundled artifact-tool workbook API before UTF-8 CSV serialization. All scalar values round-tripped unchanged. These are plain CSVs, with no spreadsheet formulas, formatting or recalculation features promised.
- The meeting brief has two intentionally separated reading pages and fewer than 850 whitespace-delimited words. Markdown pagination varies by viewer; the explicit page break provides the intended print split. No fixed-layout PDF is supplied.
- Independent final reviews checked portfolio capacity and entity/funding claims. They caught and corrected duplicated source-alias path segments and a source/role namespace collision. Remaining factual conflicts are preserved in the reconciliation log.

Machine results: [content checks](working/validation_results.json), [CSV round-trip checks](working/table_validation.json), [build counts](working/build_summary.json), [input metadata snapshot](working/input_metadata_snapshot.json). Reproduction: [table builder](working/build_tables.py), [table export](working/export_tables.mjs), [validation script](working/validate_pack.py), [structured table input](working/tables.json). These supporting files are not additional meeting material.
