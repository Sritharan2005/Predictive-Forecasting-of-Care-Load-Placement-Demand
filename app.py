import streamlit as st

st.set_page_config(
    page_title="HHS Care Forecasting",
    page_icon="📊",
    layout="wide"
)

home_page = st.Page(
    "dashboard/pages/Home.py",
    title="Home",
    icon="🏠"
)

forecast_page = st.Page(
    "dashboard/pages/Forecast.py",
    title="Forecast",
    icon="📈"
)

pg = st.navigation(
    [home_page, forecast_page]
)

with st.sidebar:
    st.title("📊 HHS Forecasting")

    st.write(
        "Predictive Forecasting of Care Load & Placement Demand"
    )

    st.divider()

    st.caption("Machine Learning Model")
    st.write("Random Forest Regressor")

    st.caption("Forecast Horizon")
    st.write("7 Days")

    st.divider()

    st.caption("Project Status")
    st.success("Dashboard Active")

pg.run()