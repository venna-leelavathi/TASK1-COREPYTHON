import csv
import os

FILENAME = "expenses.csv"

# Create file if not exists
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount"])  # Header


# Add Expense
def add_expense():
    desc = input("Enter expense description: ")
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount! Please enter a number.")
        return

    with open(FILENAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print(" Expense added successfully!\n")


# View All Expenses
def view_expenses():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            
            print("\n All Expenses:")
            print("-" * 30)
            for row in reader:
                print(f"Item: {row[0]} | Amount: ₹{row[1]}")
            print("-" * 30)
    except FileNotFoundError:
        print("No expenses found.\n")


# View Total Expenses
def total_expenses():
    total = 0
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header
            for row in reader:
                total += float(row[1])
        print(f"\n Total Expenses: ₹{total}\n")
    except FileNotFoundError:
        print("No expenses found.\n")


# Main Menu
def main():
    initialize_file()
    
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print(" Exiting... Thank you!")
            break
        else:
            print(" Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()