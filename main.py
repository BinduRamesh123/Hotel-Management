def expense_tracker_list():
    expenses = []

    while True:
        print("\n1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            expenses.append([category, amount])
            print("Expense added!")

        elif choice == "2":
            print("\n--- Expense List ---")
            for cat, amt in expenses:
                print(f"{cat} : ₹{amt}")

        elif choice == "3":
            total = sum(amount for _, amount in expenses)
            print("\nTotal Expense: ₹", total)

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")
expense_tracker_list()