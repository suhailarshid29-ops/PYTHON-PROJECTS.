import pandas as pd

def generate_report(expenses):
    df = pd.DataFrame(
        expenses,
        columns=["ID", "Date", "Category", "Amount", "Description"]
    )

    summary = df.groupby("Category")["Amount"].sum()
    print("\n--- Expense Report ---")
    print(summary)

    return summary
