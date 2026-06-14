import pandas as pd
import matplotlib.pyplot as plt


def add_expense():
    date = input("Enter Date (YYYY-MM-DD): ")
    category = input("Enter Category: ")
    amount = float(input("Enter Amount: "))

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

    print("Expense Added Successfully!")


def view_expenses():
    df = pd.read_csv("expenses.csv")
    print(df)


def show_total():
    df = pd.read_csv("expenses.csv")
    total = df["Amount"].astype(float).sum()
    print(f"Total Spending: Rs {total}")


def category_summary():
    df = pd.read_csv("expenses.csv")
    summary = df.groupby("Category")["Amount"].sum()

    print("\nExpense By Category")
    print(summary)


def show_chart():
    df = pd.read_csv("expenses.csv")
    summary = df.groupby("Category")["Amount"].sum()

    summary.plot(kind="bar")

    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")

    plt.show()


print("\nExpense Tracker")
print("1. Add Expense")
print("2. View Expenses")
print("3. Show Total Spending")
print("4. Category Summary")
print("5. Show Chart")
print("6. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    add_expense()

elif choice == "2":
    view_expenses()

elif choice == "3":
    show_total()

elif choice == "4":
    category_summary()

elif choice == "5":
    show_chart()

elif choice == "6":
    print("Goodbye!")

else:
    print("Invalid Choice")