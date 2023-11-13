import os
from expense import Expense

total_budget = 0

# ANSI color codes
PINK = '\033[95m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
END = '\033[0m'

def main():
    global total_budget
    
    print(f"Running Your Expense Tracker!")
    script_directory = os.path.dirname(os.path.realpath(__file__))
    expense_file_path = os.path.join(script_directory, "expenses.csv")

    total_budget = 0

    if total_budget == 0:
        set_total_budget()

    expense = get_user_expense()

    save_expense_to_file(expense, expense_file_path)

    summarize_expenses(expense_file_path)

def set_total_budget():
    global total_budget
    print("What is Your Budget This Month?")
    total_budget = float(input("Enter Your Total Budget: "))
    print(f"{GREEN}Total Budget Set to{END} ฿{total_budget}\n")
    return total_budget

def get_user_expense():
    print(f"Getting User Expense")
    expense_name = input("Enter Expense Name: ")
    expense_amount = float(input("Enter Expense Amount: "))
    print(f"Expense Entered: {expense_name}, {expense_amount} ฿")

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc.",
    ]

    while True:
        print("Please Select a Category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"{PINK}{i + 1}. {category_name}{END}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a Category Number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]

            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category, Please Submit Another Response")

def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving User Expense: {expense} to {expense_file_path}")
    try:
        with open(expense_file_path, "a", encoding="utf-8") as f:
            f.write(f"{expense.name}, {expense.amount}, {expense.category}\n")
    except FileNotFoundError:
        print(f"Error: File not found at {expense_file_path}")

def summarize_expenses(expense_file_path):
    global total_budget

    print(f"\nSummarizing User Expenses by Category:\n")
    expenses_by_category = {}

    try:
        with open(expense_file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(', ')
                if len(parts) == 3:
                    name, amount, category = parts
                    expense = Expense(name=name, category=category, amount=float(amount))

                    if category in expenses_by_category:
                        expenses_by_category[category].append(expense)
                    else:
                        expenses_by_category[category] = [expense]
                else:
                    print(f"Warning: Invalid line - {line.strip()}. Skipping.")

        total_amount_spent = 0

        # print summed expenses
        for category, expenses in expenses_by_category.items():
            total_amount_spent += sum(expense.amount for expense in expenses)
            print(f"{PINK}{category}:{END} Total Amount Spent - {sum(expense.amount for expense in expenses)}, Expenses - {expenses}")

        total_budget_remaining = total_budget - total_amount_spent
        print(f"\n{YELLOW}Total Amount Spent: {total_amount_spent} ฿{END}\n{GREEN}Total Budget Remaining: {total_budget_remaining} ฿{END}\n")

    except FileNotFoundError:
        print(f"{YELLOW}Error: File Not Found at {expense_file_path}{END}")

if __name__ == "__main__":
    main()
