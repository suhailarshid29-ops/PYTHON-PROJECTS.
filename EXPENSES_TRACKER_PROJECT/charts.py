import matplotlib.pyplot as plt

def show_chart(summary):
    summary.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Expense Distribution by Category")
    plt.ylabel("")
    plt.show()
