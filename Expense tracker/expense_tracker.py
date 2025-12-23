expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append((amount, category))
    print("Expense added")

def view_expenses():
    total = 0
    for amount, category in expenses:
        print(category, ":", amount)
        total += amount
    print("Total Expense:", total)

while True:
    print("\n1.Add Expense  2.View Expenses  3.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
