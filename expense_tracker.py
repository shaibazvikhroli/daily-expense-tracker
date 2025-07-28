import csv
import os
from datetime import datetime

FILENAME = "expenses.csv"

def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Amount", "Category", "Note"])

def add_expense():
    amount = input("Enter amount: ₹")
    category = input("Enter category (e.g., food, travel, bills): ")
    note = input("Enter a short note (optional): ")
    date = datetime.now().strftime("%Y-%m-%d")
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    print("✅ Expense added!\n")

def view_expenses():
    with open(FILENAME, mode="r") as file:
        reader = list(csv.reader(file))[1:]  # skip header
        if not reader:
            print("No expenses recorded yet.\n")
            return
        for row in reader:
            print(f"{row[0]} | ₹{row[1]} | {row[2]} | {row[3]}")
        print()

def total_spent():
    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            total += float(row[1])
    print(f"💰 Total Spent: ₹{total:.2f}\n")

def main():
    init_file()
    while True:
        print("=== Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spent")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            print("Goodbye! 🧾")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
