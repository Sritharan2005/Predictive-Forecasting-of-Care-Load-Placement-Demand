import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "data" / "HHS_UAC_Cleaned.csv"

df = pd.read_csv(DATA_PATH)

df["Date"] = pd.to_datetime(df["Date"])

df = df.sort_values("Date")


# -----------------------------
# Page Title
# -----------------------------

st.title("🏠 HHS Care Demand Dashboard")

st.write(
    """
    This dashboard provides an overview of historical HHS care demand
    and operational activity.
    """
)

st.divider()


# -----------------------------
# Key Metrics
# -----------------------------

total_records = len(df)

average_care = df["Children in HHS Care"].mean()

maximum_care = df["Children in HHS Care"].max()

minimum_care = df["Children in HHS Care"].min()


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Records",
        f"{total_records:,}"
    )

with col2:
    st.metric(
        "Average HHS Care",
        f"{average_care:,.0f}"
    )

with col3:
    st.metric(
        "Maximum HHS Care",
        f"{maximum_care:,.0f}"
    )

with col4:
    st.metric(
        "Minimum HHS Care",
        f"{minimum_care:,.0f}"
    )

st.caption(
    "Historical statistics are calculated from the cleaned HHS UAC dataset."
)

st.divider()

# -----------------------------
# Date Filter
# -----------------------------

st.subheader("📅 Historical Data Filter")

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

selected_dates = st.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:

    start_date, end_date = selected_dates

    filtered_df = df[
        (df["Date"].dt.date >= start_date) &
        (df["Date"].dt.date <= end_date)
    ]

else:

    filtered_df = df


st.subheader("📊 Operational Metric")

metric_options = [
    "Children apprehended and placed in CBP custody*",
    "Children in CBP custody",
    "Children transferred out of CBP custody",
    "Children in HHS Care",
    "Children discharged from HHS Care"
]

selected_metric = st.selectbox(
    "Select a metric",
    metric_options
)


metric_fig = px.line(
    filtered_df,
    x="Date",
    y=selected_metric,
    title=f"{selected_metric} Over Time"
)

metric_fig.update_layout(
    xaxis_title="Date",
    yaxis_title=selected_metric,
    hovermode="x unified"
)

st.plotly_chart(
    metric_fig,
    use_container_width=True
)


# -----------------------------
# Historical HHS Care Chart
# -----------------------------

st.subheader("📈 Historical HHS Care Demand")

fig = px.line(
    filtered_df,
    x="Date",
    y="Children in HHS Care",
    title="HHS Care Population Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Children in HHS Care",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# -----------------------------
# Operational Overview
# -----------------------------

st.subheader("📊 Operational Overview")

operational_columns = [
    "Children apprehended and placed in CBP custody*",
    "Children in CBP custody",
    "Children transferred out of CBP custody",
    "Children discharged from HHS Care"
]

summary = df[operational_columns].mean().reset_index()

summary.columns = [
    "Metric",
    "Average Daily Value"
]

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

# -----------------------------
# Model Performance
# -----------------------------

st.divider()

st.subheader("🤖 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "MAE",
        "65.77"
    )

with col2:
    st.metric(
        "RMSE",
        "87.70"
    )

with col3:
    st.metric(
        "R² Score",
        "0.752"
    )

st.caption(
    "Performance of the forecast-safe Random Forest model on the test dataset."
)

# -----------------------------
# Feature Importance
# -----------------------------

st.subheader("📊 Random Forest Feature Importance")

feature_importance = pd.DataFrame({
    "Feature": [
        "Lag_1",
        "Rolling7",
        "Rolling14",
        "Lag_7",
        "Lag_14",
        "WeekOfYear",
        "DayOfWeek",
        "Month",
        "Quarter"
    ],
    "Importance": [
        0.8388,
        0.0990,
        0.0288,
        0.0242,
        0.0066,
        0.0013,
        0.0007,
        0.0005,
        0.0001
    ]
})

feature_importance = feature_importance.sort_values(
    "Importance",
    ascending=True
)

fig_importance = px.bar(
    feature_importance,
    x="Importance",
    y="Feature",
    orientation="h",
    title="Random Forest Feature Importance"
)

fig_importance.update_layout(
    xaxis_title="Importance",
    yaxis_title="Feature"
)

st.plotly_chart(
    fig_importance,
    use_container_width=True
)

st.divider()

st.caption(
    "Predictive Forecasting of Care Load & Placement Demand | "
    "Machine Learning & Time-Series Forecasting Project"
)