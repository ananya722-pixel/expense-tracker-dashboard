import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Title
# -------------------------------
st.set_page_config(page_title="Expense Tracker Dashboard", page_icon="💰")

st.title("💰 Expense Tracker Dashboard")

# -------------------------------
# Read CSV File
# -------------------------------
df = pd.read_csv("expenses.csv")

# Convert Amount column to float
df["Amount"] = df["Amount"].astype(float)

# -------------------------------
# Category Filter
# -------------------------------
st.subheader("📂 Filter Expenses")

category = st.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)

if category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == category]

# -------------------------------
# Display Expenses
# -------------------------------
st.subheader("📋 Expenses")
st.dataframe(filtered_df)

# -------------------------------
# Budget Tracker
# -------------------------------
st.subheader("💵 Budget Tracker")

budget = st.number_input(
    "Enter Monthly Budget (₹)",
    min_value=0.0,
    value=5000.0,
    step=500.0
)

total = filtered_df["Amount"].sum()

remaining = budget - total

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Spending", f"₹{total:.2f}")

with col2:
    st.metric("Remaining Budget", f"₹{remaining:.2f}")

progress = total / budget if budget > 0 else 0

if progress > 1:
    progress = 1

st.progress(progress)

if total > budget:
    st.error("⚠️ Budget Exceeded!")
else:
    st.success("✅ You are within your budget.")

# -------------------------------
# Category Summary
# -------------------------------
st.subheader("📊 Expense By Category")

summary = filtered_df.groupby("Category")["Amount"].sum()

st.write(summary)

# -------------------------------
# Bar Chart
# -------------------------------
st.subheader("📈 Bar Chart")

st.bar_chart(summary)

# -------------------------------
# Pie Chart
# -------------------------------
st.subheader("🥧 Pie Chart")

fig, ax = plt.subplots(figsize=(6, 6))

ax.pie(
    summary,
    labels=summary.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Expenses by Category")

st.pyplot(fig)