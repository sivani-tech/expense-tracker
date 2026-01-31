from datetime import datetime
expenses = []
filename = "expenses.txt"


def load_expenses():
    """Load expenses from file to memory"""
    try:
        with open(filename,"r") as f:
            for line in f:
                line = line.strip()
                if line:
                    date_str,amount_str,category,description = line.split("|")
                    date = datetime.strptime(date_str, "%Y-%m-%d").date()
                    amount = float(amount_str)
                    expenses.append({"date":date,
                                     "amount":amount,
                                     "category":category.strip(),
                                     "description":description.strip()})
    except FileNotFoundError:
        pass


def save_expenses():
    """Save all expenses from memory to file"""
    with open(filename,"w") as f:
        for expense in expenses:
            f.write(f"{expense['date']}|{expense['amount']}|{expense['category']}|{expense['description']}\n")


def get_date_input(prompt,field_name):
    while True:
        value = input(prompt).strip()
        if not value:
            print(f"{field_name} cannot be empty!")
            continue
        try:
            org_value = datetime.strptime(value, "%Y-%m-%d").date()
            return org_value
        except ValueError:
            print("Invalid date format! Please use YYYY-MM-DD.")


def get_amount_input(prompt,field_name):
    while True:
        value = input(prompt).strip()
        if not value:
            print(f"{field_name} cannot be empty!")
            continue
        try:
            org_value = float(value)
            if org_value <= 0:
                print(f"{field_name} must be greater than 0!")
                continue
            return org_value
        except ValueError:
            print("Please enter a valid number!")


def get_input(prompt, field_name):
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print(f"{field_name} cannot be empty!")


def add_expense():
    """Add a new expense"""
    expense_date = get_date_input("Enter the date(YYYY-MM-DD): ", "Expense date")
    expense_amount = get_amount_input("Enter the amount: ", "Expense amount")
    expense_category = get_input("Enter the category: ", "Expense category")
    expense_description = get_input("Enter the description: ", "Expense description")
    
    for expense in expenses:
        if (expense['date'] == expense_date and 
            expense['amount'] == expense_amount and 
            expense['category'].lower() == expense_category.lower() and 
            expense['description'].lower() == expense_description.lower()):
            print(f"Expense on {expense_date} of {expense_amount} in '{expense_category}' already exists!\n")
            return
        
    expenses.append({"date":expense_date,
                     "amount":expense_amount,
                     "category":expense_category,
                     "description":expense_description})
    save_expenses()
    print("Expense added successfully.\n")


def delete_expense():
    """Delete an expense by number"""
    if not expenses:
        print("\nNo expenses available")
        return
    
    view_expenses()
    
    try:
        n = int(input("Enter expense number to delete: "))
        if n < 1 or n > len(expenses):
            print(f"Invalid expense number! Please enter a number between 1 and {len(expenses)}")
            return
        
        expense = expenses[n-1]
        confirm = input(f"Are you sure you want to delete this expense? (y/n): \nDate: {expense['date']} | Amount: {expense['amount']:.2f} | Category: {expense['category']} | Description: {expense['description']}\n").lower()
        if confirm == "y":
            expenses.pop(n-1)
            save_expenses()
            print("Expense deleted successfully.\n")
        else:
            print("Delete cancelled.\n")
    except ValueError:
        print("Please enter a valid number.")


def view_expenses():
    """View all expenses"""
    if not expenses:
        print("\nNo expenses available")
        return
    print("\nYour Expenses")
    print("-------------")
    for i,expense in enumerate(expenses,start=1):
        print(f"{i}.Date - {expense['date']} | Amount - {expense['amount']:.2f} | Category - {expense['category']} | Description - {expense['description']}")
    
    total_amount = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses : {len(expenses)} | Total amount : {total_amount:.2f}")


def summary():
    """Summary of the expenses"""
    if not expenses:
        print("\nNo expense available to summarize.\n")
        return
    
    print("\nYour Expense Summary")
    print("--------------------")
    total_amount = sum(expense['amount'] for expense in expenses)
    print(f"Total number of expense = {len(expenses)}")
    print(f"Total amount spent = {total_amount:.2f}\n")

    # Break down by category
    category_totals = {}
    for expense in expenses:
        cat = expense['category'].capitalize()
        category_totals[cat] = category_totals.get(cat, 0) + expense['amount']

    print("Breakdown by category:")
    for cat, amt in category_totals.items():
        print(f" - {cat}: {amt:.2f}")

    print("")

def show_help():
    """Display instructions for the Expense Tracker"""
    print("""
Welcome to Expense Tracker!

Instructions:

1. Add Expense
   - Add a new expense by entering:
     - Date (YYYY-MM-DD)
     - Amount (positive number)
     - Category (e.g., Food, Transport)
     - Description (notes about the expense)
   - Duplicate expenses (same date, amount, category, description) will not be added.

2. Delete Expense
   - Delete an expense by its number from the list.
   - You will be asked for confirmation before deletion.

3. View Expenses
   - See all your expenses with:
     - Date
     - Amount
     - Category
     - Description
   - Shows total number of expenses.

4. Summary of Expenses
   - View totals and breakdowns by category, date, or month.
   - Helps you track where your money is going.

5. Help
   - Show these instructions at any time.

6. Exit
   - Safely exit the application.

Tips:
- Always enter date in YYYY-MM-DD format.
- Amount must be a positive number.
- Category and description cannot be empty.
- Expenses are saved automatically to 'expenses.txt'.
""")
