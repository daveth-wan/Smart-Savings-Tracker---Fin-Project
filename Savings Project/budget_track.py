import os

script_directory = os.path.dirname(os.path.realpath(__file__))

total_budget = 0

def set_total_budget():
    global total_budget
    print("What is Your Budget This Month?")
    total_budget = float(input("Enter Your Total Budget: "))
    print(f"Total Budget Set to ฿{total_budget}\n")
    print(f"Script Directory: {script_directory}")
    budget_file_path = os.path.join(script_directory, "budget.txt")
    print(f"Budget File Path: {budget_file_path}")

def load_total_budget():
    global total_budget
    try:
        budget_file_path = os.path.join(script_directory, "budget.txt")
        print(f"Script Directory: {script_directory}")
        print(f"Budget File Path: {budget_file_path}")
        with open(budget_file_path, "r", encoding="utf-8") as budget_file:
            total_budget = float(budget_file.read())
            print(f"Total Budget Loaded from File: ฿{total_budget}\n")
    except FileNotFoundError:
        print("Budget File Not Found, Using Default Total Budget.\n")
        total_budget = 0
    except Exception as e:
        print(f"Error Saving Budget to File: {e}\n")

def save_total_budget():
    try:
        budget_file_path = os.path.join(script_directory, "budget.txt")
        print(f"Script Directory: {script_directory}")
        print(f"Budget File Path: {budget_file_path}")
        with open(budget_file_path, "w", encoding="utf-8") as budget_file:
            budget_file.write(str(total_budget))
    except Exception as e:
        print(f"Error Saving Budget to File: {e}")