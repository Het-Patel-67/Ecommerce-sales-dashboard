# app.py

import streamlit as st
import plotly.express as px

from data_cleaning import load_and_clean_data
from analysis import *

st.set_page_config(
    page_title="E-Commerce Dashboard",
    layout="wide"
)

st.title("📊 E-Commerce Sales Analytics Dashboard")

df = load_and_clean_data(
    "data/sales.csv"
)

# Sidebar Filters

st.sidebar.header("Filters")

selected_state = st.sidebar.multiselect(
    "Select State",
    options=df["State"].unique(),
    default=df["State"].unique()
)

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["State"].isin(selected_state))
    &
    (df["Category"].isin(selected_category))
]

# KPIs

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Revenue",
        f"₹{total_revenue(filtered_df):,.0f}"
    )

with col2:
    st.metric(
        "Total Orders",
        total_orders(filtered_df)
    )

with col3:
    st.metric(
        "Avg Order Value",
        f"₹{average_order_value(filtered_df):,.0f}"
    )

st.divider()

# Category Sales

st.subheader("Category Wise Revenue")

category_df = (
    category_sales(filtered_df)
    .reset_index()
)

fig = px.bar(
    category_df,
    x="Category",
    y="Revenue"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# State Sales

st.subheader("State Wise Revenue")

state_df = (
    state_sales(filtered_df)
    .reset_index()
)

fig2 = px.pie(
    state_df,
    names="State",
    values="Revenue"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# Monthly Trend

st.subheader("Monthly Revenue Trend")

month_df = (
    monthly_sales(filtered_df)
    .reset_index()
)

fig3 = px.line(
    month_df,
    x="Month",
    y="Revenue",
    markers=True
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

# Top Products

st.subheader("Top Products")

st.dataframe(
    top_products(filtered_df)
)

# Raw Data

with st.expander("View Dataset"):
    st.dataframe(filtered_df)