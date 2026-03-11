# Regulatory Dataset Inventory (First Pass)

## Scope

This inventory covers documented datasets used to:

- assemble regulatory reports,
- track reporting process execution, and
- generate KPI and monitoring outputs

across:

- **Brazil (BR)**
- **Mexico (MX)**
- **Colombia (CO)**
- **Global KPI / Monitoring flows**

Sources referenced for this first pass:

- Confluence pages
- internal docs
- shared sheets

## Inventory maturity (current state)

- **Colombia:** highest dataset-level detail available in current documentation.
- **Mexico:** strong dataset-level detail available in current documentation.
- **Brazil:** currently documented at a higher level; dataset-level decomposition still pending.
- **Global KPI / Monitoring:** process-level and indicator-level documentation available, with dataset linkage partial.

## Dataset inventory table

> Note: This is an initial structure and includes the known coverage status.  
> Dataset names and technical metadata should be filled from source artifacts in the next iteration.

| Region / Flow | Regulatory report or monitoring output | Dataset name | Purpose in flow | Documented source (Confluence/Doc/Sheet) | Documentation depth | Owner / Team | Refresh cadence | Current status | Notes / Gaps |
|---|---|---|---|---|---|---|---|---|---|
| Colombia | Regulatory reporting (multiple reports) | _To be populated from source docs_ | Assemble and validate report inputs | Confluence + docs + sheets | Dataset-level | _TBD_ | _TBD_ | Partially inventoried | Richest country coverage in this pass |
| Mexico | Regulatory reporting (multiple reports) | _To be populated from source docs_ | Assemble and validate report inputs | Confluence + docs + sheets | Dataset-level | _TBD_ | _TBD_ | Partially inventoried | Strong dataset-level documentation available |
| Brazil | Regulatory reporting (multiple reports) | _To be decomposed_ | Assemble and validate report inputs | Confluence + docs + sheets | High-level | _TBD_ | _TBD_ | High-level only | Requires dataset-level breakdown |
| Global | KPI / monitoring flows | _To be linked to source datasets_ | Track operational and reporting KPIs | Confluence + docs + sheets | Mixed (indicator-level + partial dataset-level) | _TBD_ | _TBD_ | Partially inventoried | Complete lineage from KPI to datasets pending |

## Field definitions

- **Region / Flow:** Country scope (BR, MX, CO) or cross-country/global process.
- **Regulatory report or monitoring output:** Report family or KPI dashboard/process output.
- **Dataset name:** Canonical dataset or table identifier.
- **Purpose in flow:** How the dataset is used (e.g., source-of-record, enrichment, reconciliation, submission).
- **Documented source:** Where evidence exists (Confluence page, internal doc, sheet link).
- **Documentation depth:** High-level, process-level, or dataset-level.
- **Owner / Team:** Responsible business/engineering/data team.
- **Refresh cadence:** Daily, monthly, event-based, etc.
- **Current status:** Not started, partially inventoried, validated, or complete.
- **Notes / Gaps:** Missing metadata, unclear ownership, unresolved lineage, etc.

## Next-pass actions

1. Extract and normalize dataset names from Colombia and Mexico documentation into this table.
2. Break down Brazil report families into explicit dataset dependencies.
3. Add lineage links for global KPI/monitoring outputs back to country and shared datasets.
4. Validate ownership, cadence, and control points with reporting and data platform teams.

