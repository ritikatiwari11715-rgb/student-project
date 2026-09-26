expenses = []


def add_expense():
    try:
        amount = float(input("Enter expense amount: "))
        category = input("Enter category: ").strip()
        description = input("Enter description: ").strip()

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        if not category:
            print("Category cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }

        expenses.append(expense)
        print("Expense added successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print("\n--- All Expenses ---")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} | "
            f"{expense['category']} | "
            f"{expense['description']}"
        )


def search_expenses():
    category = input("Enter category to search: ").strip().lower()

    found = False

    for expense in expenses:
        if expense["category"].lower() == category:
            print(
                f"₹{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['description']}"
            )
            found = True

    if not found:
        print("No expenses found for this category.")


def show_summary():
    if not expenses:
        print("No expenses recorded.")
        return

    total = sum(expense["amount"] for expense in expenses)

    print(f"\nTotal Expenses: ₹{total:.2f}")
    print(f"Number of Expenses: {len(expenses)}")

    category_totals = {}

    for expense in expenses:
        category = expense["category"]
        category_totals[category] = (
            category_totals.get(category, 0) + expense["amount"]
        )

    print("\nCategory-wise Spending:")

    for category, amount in category_totals.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    while True:
        print("\n===== Student Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Show Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            search_expenses()
        elif choice == "4":
            show_summary()
        elif choice == "5":
            print("Thank you for using Student Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
