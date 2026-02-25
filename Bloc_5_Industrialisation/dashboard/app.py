import streamlit as st
import pandas as pd
import numpy as np
import requests
import os
import plotly.express as px

# ============================
# CONFIG
# ============================

st.set_page_config(
    page_title="Getaround Late Checkout Decision Tool",
    layout="wide"
)

API_URL = "http://localhost:8000/predict"
AVERAGE_DAILY_PRICE = 120

# ============================
# LOAD DATA
# ============================

@st.cache_data
def load_data():

    BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

    DATA_PATH = os.path.join(
        BASE_DIR,
        "data",
        "get_around_delay_analysis.xlsx"
    )

    df = pd.read_excel(DATA_PATH)

    df = df[df["state"] == "ended"]

    df["delay_at_checkout_in_minutes"] = (
        df["delay_at_checkout_in_minutes"]
        .fillna(0)
    )

    return df

df = load_data()
# ============================
# SIDEBAR
# ============================

st.sidebar.header("Feature Configuration")

threshold = st.sidebar.slider(
    "Minimum delay between rentals (minutes)",
    0, 180, 60, step=10
)

scope = st.sidebar.radio(
    "Enable feature for:",
    ["All cars", "Connect cars only"]
)

# ============================
# SCOPE FILTER
# ============================

if scope == "Connect cars only":
    df_filtered = df[df["checkin_type"] == "connect"].copy()
else:
    df_filtered = df.copy()

# ============================
# REVENUE ESTIMATION
# ============================

df_filtered["estimated_revenue"] = AVERAGE_DAILY_PRICE

# ============================
# PRODUCT LOGIC
# ============================

df_conflict = df_filtered.dropna(
    subset=["time_delta_with_previous_rental_in_minutes"]
).copy()

df_conflict["conflict"] = (
    df_conflict["delay_at_checkout_in_minutes"]
    >
    df_conflict["time_delta_with_previous_rental_in_minutes"]
)

df_conflict["blocked_by_threshold"] = (
    df_conflict["time_delta_with_previous_rental_in_minutes"] < threshold
)

df_conflict["conflict_solved"] = (
    df_conflict["blocked_by_threshold"] &
    df_conflict["conflict"]
)

# ============================
# KPI CALCULATIONS
# ============================

total_rentals = len(df_conflict)

rentals_affected = df_conflict["blocked_by_threshold"].sum()
rentals_affected_pct = (rentals_affected / total_rentals) * 100

revenue_at_risk = df_conflict.loc[
    df_conflict["blocked_by_threshold"],
    "estimated_revenue"
].sum()

total_revenue = df_conflict["estimated_revenue"].sum()
revenue_at_risk_pct = (revenue_at_risk / total_revenue) * 100

conflicts_total = df_conflict["conflict"].sum()

conflicts_resolved = df_conflict["conflict_solved"].sum()

conflicts_resolved_pct = (
    conflicts_resolved / conflicts_total
) * 100 if conflicts_total != 0 else 0

avg_delay = df_filtered[
    df_filtered["delay_at_checkout_in_minutes"] > 0
]["delay_at_checkout_in_minutes"].mean()

# ============================
# KPI DISPLAY
# ============================

st.title("🚗 Late Checkout Product Decision Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Rentals affected", f"{rentals_affected_pct:.1f}%")
col2.metric("Revenue at Risk", f"{revenue_at_risk_pct:.1f}%")
col3.metric("Conflicts resolved", f"{conflicts_resolved_pct:.1f}%")
col4.metric("Average delay", f"{avg_delay:.1f} min")

# ============================
# PIE CHART RENTALS
# ============================

pie_df = pd.DataFrame({
    "Category": ["Affected rentals", "Safe rentals"],
    "Count": [rentals_affected, total_rentals - rentals_affected]
})

fig = px.pie(pie_df, names="Category", values="Count")
st.plotly_chart(fig, width="stretch")

# ============================
# PIE CHART REVENUE
# ============================

safe_revenue = total_revenue - revenue_at_risk

rev_df = pd.DataFrame({
    "Category": ["Revenue at risk", "Safe revenue"],
    "Amount": [revenue_at_risk, safe_revenue]
})

fig2 = px.pie(rev_df, names="Category", values="Amount")
st.plotly_chart(fig2, width="stretch")

# ============================
# TRADEOFF CURVE
# ============================

thresholds = np.arange(0,180,10)
tradeoff = []

for t in thresholds:

    blocked = (
        df_conflict["time_delta_with_previous_rental_in_minutes"] < t
    )

    solved = (
        blocked & df_conflict["conflict"]
    ).sum()

    revenue_lost = df_conflict.loc[
        blocked,
        "estimated_revenue"
    ].sum()

    tradeoff.append([t, solved, revenue_lost])

trade_df = pd.DataFrame(
    tradeoff,
    columns=["Threshold","Conflicts Solved","Revenue Lost"]
)

fig3 = px.line(
    trade_df,
    x="Revenue Lost",
    y="Conflicts Solved",
    hover_data=["Threshold"],
    title="Revenue Lost vs Conflicts Solved"
)

st.plotly_chart(fig3, width="stretch")

# ============================
# ML PRICING TOOL (FASTAPI)
# ============================

st.subheader("Pricing Recommendation Tool")

mileage = st.number_input("Mileage",0,300000,50000)
engine_power = st.slider("Engine Power",50,400,100)

fuel = st.selectbox("Fuel",["diesel","petrol","hybrid","electric"])
paint_color = st.selectbox("Color",["black","white","grey","blue","red"])
car_type = st.selectbox("Car Type",["sedan","suv","convertible","estate"])

private_parking = st.selectbox("Private Parking",["no","yes"])
gps = st.selectbox("GPS",["no","yes"])
ac = st.selectbox("Air Conditioning",["no","yes"])
automatic = st.selectbox("Automatic",["no","yes"])
connect = st.selectbox("Connect",["no","yes"])
regulator = st.selectbox("Speed Regulator",["no","yes"])
winter = st.selectbox("Winter Tires",["no","yes"])

if st.button("Predict Price"):

    input_data = [[
        mileage,
        engine_power,
        fuel,
        paint_color,
        car_type,
        1 if private_parking=="yes" else 0,
        1 if gps=="yes" else 0,
        1 if ac=="yes" else 0,
        1 if automatic=="yes" else 0,
        1 if connect=="yes" else 0,
        1 if regulator=="yes" else 0,
        1 if winter=="yes" else 0
    ]]

    response = requests.post(
        API_URL,
        json={"input":input_data}
    )

    if response.status_code==200:
        prediction=response.json()["prediction"][0]
        st.success(f"Recommended price: {prediction:.2f} €/day")
    else:
        st.error("API Error")

