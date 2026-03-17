import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Amount at Risk Dashboard", layout="wide")

DEFAULT_DATA_PATH = "New_Query_2026_02_25_16_33_43 (1).csv"

DEFAULT_MAPPING = {
    "transaction_code": ["erp_transaction_code", "transaction_code", "tcode"],
    "creator_user_id": ["creator_user_id", "created_by", "user_id", "user"],
    "movement_type": ["movement_type", "posting_type", "entry_type"],
    "document_type": ["document_type", "doc_type", "document"],
    "total_rows": [" total_linhas ", "total_linhas", "total_rows", "row_count"],
    "unique_ids": [" total_id_unicos ", "total_id_unicos", "unique_ids", "id_count"],
    "amount_at_risk": [
        "valor_total_movimentado",
        "amount_at_risk",
        "total_amount_at_risk",
        "risk_amount",
    ],
}


def normalize_colname(value: str) -> str:
    return value.strip().lower().replace(" ", "_")


def find_column(df: pd.DataFrame, aliases: list[str]) -> str | None:
    normalized = {normalize_colname(col): col for col in df.columns}
    for alias in aliases:
        key = normalize_colname(alias)
        if key in normalized:
            return normalized[key]
    return None


def parse_number(series: pd.Series) -> pd.Series:
    cleaned = (
        series.astype(str)
        .str.replace(",", "", regex=False)
        .str.replace(" ", "", regex=False)
        .str.replace("(", "-", regex=False)
        .str.replace(")", "", regex=False)
    )
    return pd.to_numeric(cleaned, errors="coerce").fillna(0.0)


def load_dataset(file_obj, data_path: str) -> pd.DataFrame:
    if file_obj is not None:
        return pd.read_csv(file_obj)
    return pd.read_csv(data_path)


def map_and_prepare(df: pd.DataFrame, mapping: dict[str, list[str]]) -> pd.DataFrame:
    resolved = {}
    missing = []
    for semantic_name, aliases in mapping.items():
        found = find_column(df, aliases)
        if found is None:
            missing.append(semantic_name)
        else:
            resolved[semantic_name] = found

    required = ["movement_type", "document_type", "creator_user_id", "transaction_code"]
    missing_required = [col for col in required if col in missing]
    if missing_required:
        raise ValueError(
            "Missing required columns after mapping: " + ", ".join(missing_required)
        )

    prepared = pd.DataFrame(
        {
            "transaction_code": df[resolved["transaction_code"]].fillna("UNKNOWN"),
            "creator_user_id": df[resolved["creator_user_id"]].fillna("UNKNOWN"),
            "movement_type": df[resolved["movement_type"]].fillna("UNKNOWN"),
            "document_type": df[resolved["document_type"]].fillna("UNKNOWN"),
            "total_rows": parse_number(df[resolved["total_rows"]])
            if "total_rows" in resolved
            else 0.0,
            "unique_ids": parse_number(df[resolved["unique_ids"]])
            if "unique_ids" in resolved
            else 0.0,
            "amount_at_risk": parse_number(df[resolved["amount_at_risk"]])
            if "amount_at_risk" in resolved
            else 0.0,
        }
    )

    prepared["activity_proxy"] = prepared["total_rows"].fillna(0) + prepared[
        "unique_ids"
    ].fillna(0)
    prepared["metric_value"] = prepared["amount_at_risk"]
    prepared["metric_label"] = "Amount at Risk"
    if prepared["amount_at_risk"].abs().sum() == 0:
        prepared["metric_value"] = prepared["activity_proxy"]
        prepared["metric_label"] = "Risk Activity Proxy"

    return prepared


def with_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.header("Filters")
    movement_type = st.sidebar.multiselect(
        "Movement type",
        sorted(df["movement_type"].dropna().unique().tolist()),
        default=sorted(df["movement_type"].dropna().unique().tolist()),
    )
    document_type = st.sidebar.multiselect(
        "Document type",
        sorted(df["document_type"].dropna().unique().tolist()),
        default=sorted(df["document_type"].dropna().unique().tolist()),
    )
    creator_user_id = st.sidebar.multiselect(
        "Creator user",
        sorted(df["creator_user_id"].dropna().unique().tolist()),
        default=sorted(df["creator_user_id"].dropna().unique().tolist())[:25],
    )
    filtered = df[
        df["movement_type"].isin(movement_type)
        & df["document_type"].isin(document_type)
        & df["creator_user_id"].isin(creator_user_id)
    ].copy()
    return filtered


def main() -> None:
    st.title("Amount at Risk - Advanced Dashboard")
    st.caption("Prototype with richer visuals and tables than the current report.")

    st.sidebar.header("Data source")
    uploaded = st.sidebar.file_uploader("Upload support CSV", type=["csv"])
    default_path = st.sidebar.text_input("Local CSV path", value=DEFAULT_DATA_PATH)
    mapping_str = st.sidebar.text_area(
        "Column mapping (JSON)", value=json.dumps(DEFAULT_MAPPING, indent=2), height=240
    )

    try:
        mapping = json.loads(mapping_str)
    except json.JSONDecodeError:
        st.error("Column mapping JSON is invalid.")
        return

    try:
        if uploaded is None and not Path(default_path).exists():
            st.error(
                f"File not found: {default_path}. Upload a CSV in the sidebar or fix the path."
            )
            return
        raw_df = load_dataset(uploaded, default_path)
        df = map_and_prepare(raw_df, mapping)
    except Exception as exc:  # pragma: no cover
        st.error(f"Failed to load data: {exc}")
        return

    filtered = with_filters(df)
    if filtered.empty:
        st.warning("No data after filters.")
        return

    metric_label = filtered["metric_label"].iloc[0]
    total_metric = filtered["metric_value"].sum()
    total_rows = filtered["total_rows"].sum()
    unique_ids = filtered["unique_ids"].sum()
    manual_share = (
        filtered.loc[filtered["movement_type"].str.lower() == "manual", "metric_value"].sum()
        / max(total_metric, 1)
    )

    c1, c2, c3, c4 = st.columns(4)
    c1.metric(metric_label, f"{total_metric:,.2f}")
    c2.metric("Total Rows", f"{total_rows:,.0f}")
    c3.metric("Unique IDs", f"{unique_ids:,.0f}")
    c4.metric("Manual Share", f"{manual_share:.1%}")

    if metric_label != "Amount at Risk":
        st.info(
            "Amount column is empty/zero in this dataset, so visuals are using an activity-based proxy."
        )

    left, right = st.columns(2)

    by_doc = (
        filtered.groupby("document_type", as_index=False)["metric_value"]
        .sum()
        .sort_values("metric_value", ascending=False)
        .head(15)
    )
    fig_doc = px.bar(
        by_doc,
        x="document_type",
        y="metric_value",
        title=f"Top Document Types by {metric_label}",
    )
    left.plotly_chart(fig_doc, use_container_width=True)

    by_user = (
        filtered.groupby("creator_user_id", as_index=False)["metric_value"]
        .sum()
        .sort_values("metric_value", ascending=False)
        .head(15)
    )
    fig_user = px.bar(
        by_user,
        x="creator_user_id",
        y="metric_value",
        title=f"Top Users by {metric_label}",
    )
    right.plotly_chart(fig_user, use_container_width=True)

    left2, right2 = st.columns(2)
    movement_doc = (
        filtered.groupby(["movement_type", "document_type"], as_index=False)["metric_value"]
        .sum()
        .sort_values("metric_value", ascending=False)
    )
    fig_sunburst = px.sunburst(
        movement_doc,
        path=["movement_type", "document_type"],
        values="metric_value",
        title="Composition by Movement and Document Type",
    )
    left2.plotly_chart(fig_sunburst, use_container_width=True)

    by_code = (
        filtered.groupby(["transaction_code", "creator_user_id"], as_index=False)[
            ["total_rows", "unique_ids", "metric_value"]
        ]
        .sum()
        .sort_values("metric_value", ascending=False)
    )
    fig_scatter = px.scatter(
        by_code.head(300),
        x="total_rows",
        y="metric_value",
        size="unique_ids",
        color="creator_user_id",
        hover_data=["transaction_code"],
        title=f"Volume vs {metric_label} (Top 300 combinations)",
    )
    right2.plotly_chart(fig_scatter, use_container_width=True)

    st.subheader("Risk Concentration Table")
    concentration = (
        filtered.groupby(["creator_user_id", "document_type"], as_index=False)["metric_value"]
        .sum()
        .sort_values("metric_value", ascending=False)
    )
    concentration["share_pct"] = concentration["metric_value"] / max(total_metric, 1)
    st.dataframe(concentration.head(100), use_container_width=True)

    csv_export = filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download filtered data",
        data=csv_export,
        file_name="amount_at_risk_filtered.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()
