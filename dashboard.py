import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page Title
st.title("💰 Expense Tracker Dashboard")

# Read CSV file
df = pd.read_csv("expenses.csv")

# ==========================
# Category Filter
# ==========================

st.subheader("Filter Expenses")

category = st.selectbox(
    "Select Category",
    ["All"] + list(df["Category"].unique())
)

if category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == category]

# Show filtered data
st.subheader("Expenses")
st.dataframe(filtered_df)

# ==========================
# Total Spending
# ==========================

total = filtered_df["Amount"].astype(float).sum()

st.metric("Total Spending", f"₹{total}")

# ==========================
# Category Summary
# ==========================

summary = filtered_df.groupby("Category")["Amount"].sum()

st.subheader("Expense by Category")
st.write(summary)

# ==========================
# Bar Chart
# ==========================

st.subheader("Bar Chart")
st.bar_chart(summary)

# ==========================
# Pie Chart
# ==========================

st.subheader("Pie Chart")

fig, ax = plt.subplots()

ax.pie(
    summary,
    labels=summary.index,
    autopct="%1.1f%%",
    startangle=90
)

ax.set_title("Expenses by Category")

st.pyplot(fig)