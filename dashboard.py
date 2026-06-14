import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("💰 Expense Tracker Dashboard")
st.subheader("Add New Expense")

date = st.date_input("Date")

category = st.text_input("Category")

amount = st.number_input(
    "Amount",
    min_value=0.0,
    step=1.0
)

if st.button("Add Expense"):

    new_expense = pd.DataFrame({
        "Date": [date],
        "Category": [category],
        "Amount": [amount]
    })

    new_expense.to_csv(
        "expenses.csv",
        mode="a",
        header=False,
        index=False
    )

    st.success("Expense Added Successfully!")

# Read data
df = pd.read_csv("expenses.csv")

# Show expenses table
st.subheader("All Expenses")
st.dataframe(df)

total = df["Amount"].astype(float).sum()#show total
st.metric("Total Spending", f"₹{total}")


st.subheader("Expense By Category")#category summary

summary = df.groupby("Category")["Amount"].sum()

st.write(summary)

st.subheader("Expense Chart") #chart

fig, ax = plt.subplots()

summary.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Amount")
ax.set_title("Expenses by Category")

st.pyplot(fig)