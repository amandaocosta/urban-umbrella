# Amount at Risk Dashboard Proposal

## Objective

Build a new dashboard (outside Looker Studio) with deeper monitoring of **Amount at Risk** and operational drivers.

This proposal is implemented in `dashboard_app.py` and can be adapted to Power BI, Metabase, or Tableau.

## Recommended Structure

### 1) Executive Overview

**KPI Cards**
- Total Amount at Risk
- Total Rows (volume processed)
- Total Unique IDs
- Manual Share (%)

**Main visuals**
- Top Document Types by Amount at Risk
- Top Users by Amount at Risk

### 2) Composition and Segmentation

**Visuals**
- Sunburst: Movement Type -> Document Type
- Scatter: Volume vs Amount at Risk (bubble size by unique IDs)

**Purpose**
- Explain if risk is concentrated in specific processes, document classes, or users.

### 3) Concentration and Controls

**Table**
- User + Document Type concentration table
- Amount share (% of total risk)

**Purpose**
- Identify ownership concentration and control priorities.

## Filters

Global filters that should affect all charts:
- Movement type
- Document type
- Creator user

## Data Model (expected)

Minimum columns:
- transaction code
- creator user id
- movement type
- document type
- amount at risk (or equivalent monetary field)

Optional but strongly recommended:
- row count / line count
- unique id count
- posting date (for trends)
- company code / country / legal entity

## Tool Recommendation

If your priority is speed and collaboration:
- **Power BI**: strongest for enterprise sharing and drill-through.
- **Metabase**: fastest lightweight setup with SQL-first workflows.
- **Streamlit** (already provided here): best for quick custom logic and iteration.

## Current Prototype Included

`dashboard_app.py` includes:
- CSV upload + local path mode
- Flexible column mapping (JSON in sidebar)
- Automatic fallback to activity proxy when amount column is empty/zero
- Extra charts and concentration table beyond the current Looker layout

Run locally:

```bash
pip install -r requirements-dashboard.txt
streamlit run dashboard_app.py
```

## Next Improvements

1. Add monthly trend line (requires date field).
2. Add thresholds and RAG status (green/yellow/red).
3. Add anomaly detection (z-score on user/document spikes).
4. Add split by business unit/legal entity.
