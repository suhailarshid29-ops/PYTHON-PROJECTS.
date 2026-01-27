from database import Database
from expense import Expense
from reports import generate_report
from charts import show_chart
from datetime import date

db = Database()

def menu():
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Generate Report")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Category: ")
        amount = float(input("Amount: "))
        description = input("Description: ")
        today = date.today().isoformat()

        expense = Expense(today, category, amount, description)
        db.add_expense(expense.date, expense.category, expense.amount, expense.description)
        print("✅ Expense added successfully")

    elif choice == "2":
        expenses = db.fetch_expenses()
        for exp in expenses:
            print(exp)

    elif choice == "3":
        expense_id = int(input("Enter Expense ID to delete: "))
        db.delete_expense(expense_id)
        print("❌ Expense deleted")

    elif choice == "4":
        expenses = db.fetch_expenses()
        if expenses:
            summary = generate_report(expenses)
            show_chart(summary)
        else:
            print("No expenses found")

    elif choice == "5":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
