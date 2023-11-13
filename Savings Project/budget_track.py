import os

script_directory = os.path.dirname(os.path.abspath(__file__))

total_budget = 0

def set_total_budget():
    global total_budget
    print("What is Your Budget This Month?")
    total_budget = float(input("Enter Your Total Budget: "))
    print(f"Total Budget Set to ฿{total_budget:.2f}\n")

    save_total_budget()

    return total_budget

def load_total_budget():
    global total_budget
    try:
        budget_file_path = os.path.join(script_directory, "budget.txt")
        with open(budget_file_path, "r", encoding="utf-8") as budget_file:
            total_budget = float(budget_file.read())
        print(f"Total Budget Loaded from File: ฿{total_budget:.2f}")
    except FileNotFoundError:
        print(f"Budget File Not Found at {budget_file_path}, Using Default Total Budget.")
        total_budget = 0
    except Exception as e:
        print(f"Error Loading Budget from File: {e}")

def save_total_budget():
    try:
        with open("budget.txt", "w", encoding="utf-8") as budget_file:
            budget_file.write(f"{total_budget:.2f}")
        print(f"Total Budget saved to file: ฿{total_budget:.2f}")
    except Exception as e:
        print(f"Error Saving Budget to File: {e}")


if __name__ == "__main__":
    load_total_budget()
    if total_budget == 0:
        set_total_budget()
        save_total_budget()
