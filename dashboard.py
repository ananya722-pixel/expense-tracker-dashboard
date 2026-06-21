import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Expense Tracker Dashboard")

# Read CSV
df = pd.read_csv("expenses.csv")

# Show data
st.subheader("All Expenses")
st.dataframe(df)

# Total spending
total = df["Amount"].astype(float).sum()
st.metric("Total Spending", f"₹{total}")

# Category summary
st.subheader("Expense By Category")
summary = df.groupby("Category")["Amount"].sum()
st.write(summary)

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(summary)

# Pie chart
st.subheader("Pie Chart")

fig, ax = plt.subplots()

ax.pie(
    summary,
    labels=summary.index,
    autopct="%1.1f%%"
)

ax.set_title("Expenses by Category")

st.pyplot(fig)