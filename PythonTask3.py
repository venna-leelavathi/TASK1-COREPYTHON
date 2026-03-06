import csv
from datetime import datetime

FILE = "expenses.csv"

# Add expense with category
def add_expense(desc, amount, category):
    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        date = datetime.now().strftime("%Y-%m-%d")
        writer.writerow([desc, amount, category, date])
    print("Expense added successfully")

# View all expenses
def view_expenses():
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

# Search expenses by category
def search_category(category):
    print("Expenses in category:", category)
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2].lower() == category.lower():
                print(row)

# Total spent per category
def total_per_category(category):
    total = 0
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[2].lower() == category.lower():
                total += int(row[1])
    print("Total spent on", category, ":", total)

# Monthly total
def monthly_total(month):
    total = 0
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if row[3].startswith(month):   # Example: 2025-09
                total += int(row[1])
    print("Monthly Total:", total)

# Menu
while True:
    print("\nExpense Tracker")
    print("1.Add Expense")
    print("2.View Expenses")
    print("3.Search by Category")
    print("4.Total per Category")
    print("5.Monthly Total")
    print("6.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        desc = input("Enter description: ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")
        add_expense(desc, amount, category)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        cat = input("Enter category to search: ")
        search_category(cat)

    elif choice == "4":
        cat = input("Enter category: ")
        total_per_category(cat)

    elif choice == "5":
        month = input("Enter month (YYYY-MM): ")
        monthly_total(month)

    elif choice == "6":
        break

    else:
        print("Invalid choice")
