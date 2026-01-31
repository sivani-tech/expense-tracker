import expense_manager

if __name__ == "__main__":
    expense_manager.load_expenses()

    print("TRACK YOUR EXPENSE HERE")

    while True:
        print("\nMENU")
        print("-----\n")
        print("1.Add Expense")
        print("2.Delete Expense")
        print("3.View Expenses")
        print("4.Summary of all Expenses")
        print("5.Help")
        print("6.Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Please enter a number.\n")
            continue

        if (choice == 1):
            expense_manager.add_expense()
        elif (choice == 2):
            expense_manager.delete_expense()
        elif (choice == 3):
            expense_manager.view_expenses()
        elif (choice == 4):
            expense_manager.summary()
        elif (choice == 5):
            expense_manager.show_help()
        elif (choice == 6):
            print("Exiting...Goodbye")
            break
        else:
            print("Invalid Choice\n")

