from datetime import datetime


class Expense:
    def __init__(self, date, category, amount, description):
        self.date = date              # datetime object
        self.category = category
        self.amount = amount
        self.description = description



class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        try:
            date_input = input("Enter date (YYYY-MM-DD): ")
            date = datetime.strptime(date_input, "%Y-%m-%d")

            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")

            expense = Expense(date, category, amount, description)
            self.expenses.append(expense)

            print("✅ Expense added successfully")

        except ValueError:
            print("❌ Invalid input! Please check date or amount format.")

    def view_expenses(self):
        try:
            input_date = datetime.strptime(
                input("Enter date (YYYY-MM-DD): "), "%Y-%m-%d"
            )

            found = False

            for item in self.expenses:
                if item.date.date() == input_date.date():
                    print(f"\nDate: {item.date.date()}")
                    print(f"Category: {item.category}")
                    print(f"Amount: {item.amount}")
                    print(f"Description: {item.description}")
                    print("-------------------")
                    found = True

            if not found:
                print("❌ No expenses found for this date")

        except ValueError:
            print("❌ Invalid date format!")

    
    def total_spending(self):
        if not self.expenses:
            print("❌ No expenses found")
            return

        total = sum(item.amount for item in self.expenses)
        print(f"💰 Total spending: {total}")

    def category_spending(self):
        if not self.expenses:
            print("❌ No expenses found")
            return

        categories = {}

        for item in self.expenses:
            categories[item.category] = categories.get(item.category, 0) + item.amount

        print("\n📊 Category-wise spending:")
        for cat, amt in categories.items():
            print(f"{cat}: {amt}")

    def filter_by_category(self, category):
        found = False

        for item in self.expenses:
            if item.category.lower() == category.lower():
                print(f"\nDate: {item.date.date()}")
                print(f"Amount: {item.amount}")
                print(f"Description: {item.description}")
                print("-------------------")
                found = True

        if not found:
            print("❌ No expenses in this category")


tracker = ExpenseTracker()

while True:
    print("\n--------- MENU ---------")
    print("1. Add Expense")
    print("2. View Expenses by Date")
    print("3. Total Spending")
    print("4. Category-wise Spending")
    print("5. Filter by Category")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tracker.add_expense()

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        tracker.total_spending()

    elif choice == "4":
        tracker.category_spending()

    elif choice == "5":
        category = input("Enter category to filter: ")
        tracker.filter_by_category(category)

    elif choice == "6":
        print(" Exiting program...")
        break

    else:
        print("❌ Invalid choice")       
    
            
