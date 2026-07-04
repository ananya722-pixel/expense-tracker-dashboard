import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="Expense Tracker Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Expense Tracker Dashboard")
st.write("Track, analyze, and visualize your expenses.")

# -------------------------------
# Read CSV File
# -------------------------------
df = pd.read_csv("expenses.csv")
df["Amount"] = df["Amount"].astype(float)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("⚙️ Dashboard Controls")

category = st.sidebar.selectbox(
    "📂 Select Category",
    ["All"] + list(df["Category"].unique())
)

budget = st.sidebar.number_input(
    "💵 Monthly Budget (₹)",
    min_value=0.0,
    value=5000.0,
    step=500.0
)

# -------------------------------
# Filter Data
# -------------------------------
if category == "All":
    filtered_df = df
else:
    filtered_df = df[df["Category"] == category]

# -------------------------------
# Dashboard Metrics
# -------------------------------
total_spending = filtered_df["Amount"].sum()
total_transactions = len(filtered_df)
total_categories = filtered_df["Category"].nunique()
remaining = budget - total_spending

st.subheader("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Spending", f"₹{total_spending:.2f}")

with col2:
    st.metric("🧾 Transactions", total_transactions)

with col3:
    st.metric("📂 Categories", total_categories)

with col4:
    st.metric("💵 Remaining Budget", f"₹{remaining:.2f}")

# -------------------------------
# Budget Progress
# -------------------------------
st.subheader("💵 Budget Tracker")

progress = total_spending / budget if budget > 0 else 0
progress = min(progress, 1.0)

st.progress(progress)

if total_spending > budget:
    st.error("⚠️ Budget Exceeded!")
else:
    st.success("✅ You are within your budget.")

# -------------------------------
# Expense Table
# -------------------------------
st.subheader("📋 Expense Records")
st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# Category Summary
# -------------------------------
summary = filtered_df.groupby("Category")["Amount"].sum()

# -------------------------------
# Charts
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Bar Chart")
    st.bar_chart(summary)

with col2:
    st.subheader("🥧 Pie Chart")

    fig, ax = plt.subplots(figsize=(5, 5))

    ax.pie(
        summary,
        labels=summary.index,
        autopct="%1.1f%%",
        startangle=90
    )

    ax.set_title("Expense Distribution")

    st.pyplot(fig)

# -------------------------------
# Category Summary
# -------------------------------
st.subheader("📊 Category Summary")
st.write(summary)
