import matplotlib.pyplot as plt

from . import Expense


def main():
    expenses = Expense.Expenses()
    expenses.read_expenses("data/spending_data.csv")
    divided_for_loop = expenses.categorize_for_loop()
    divided_set_comp = expenses.categorize_set_comprehension()
    if divided_for_loop != divided_set_comp:
        print("Sets are NOT equal by == test")
    for a, b in zip(divided_for_loop, divided_set_comp):
        if not (b.issubset(a) and a.issubset(b)):
            print("Sets are NOT equal by subset test")


if __name__ == "__main__":
    main()
