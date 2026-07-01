class FinanceTracker:

    def __init__(self):
        self.transactions = []

    def add_income(self, description, amount):
        self.transactions.append (
            {
                "type": "income",
                "description": description,
                "amount": amount 
            }
        )

    def add_expense(self, description, amount):
        self.transactions.append({
            "type": "expense",
            "description": description,
            "amount": amount
            }
        )

    def monthly_summary(self):
        total_income = 0
        total_expense = 0

        for t in self.transactions:
            if t["type"] == "income":
                total_income += t["amount"]
            else:
                total_expense += t["amount"]
        
        print("\n========== Monthly Summary ==========")
        print(f"Toatl Income  : Rs. {total_income}")
        print(f"Total Expenses: Rs. {total_expense}")
        print(f"Balance       : Rs. {total_income - total_expense}")
        print("=======================================")


def main():
    tracker = FinanceTracker()

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            desc = input("Description: ")
            amount = float(input("Amount (Rs.): "))
            tracker.add_income(desc, amount)
            print("Income added!")

        elif choice == "2":
            desc = input("Description: ")
            amount = float(input("Amount (Rs.): "))
            tracker.add_expense(desc, amount)
            print("Expense added!")

        elif choice == "3":
            tracker.monthly_summary()

        elif choice == "4":
            print("Have a GoodDay! :) ")
            break

        else:
            print("Invalid choice, try again.")

main()