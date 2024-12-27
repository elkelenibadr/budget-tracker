from services.general_services import add_transaction, get_transactions, generate_report


def main():
    while True:
        print("\nBudget Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            type = input("Type (income/expense): ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            add_transaction(type, amount, category)
        elif choice == "2":
            transactions = get_transactions()
            for t in transactions:
                print(f"{t.id} | {t.type} | {t.amount} | {t.category} | {t.date}")
        elif choice == "3":
            file_format = input("Choose report format (csv/excel): ").strip().lower()
            generate_report(file_format)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
