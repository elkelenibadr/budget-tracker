from models.myproject import Transaction, SessionLocal
from datetime import date
import pandas as pd


def add_transaction(type, amount, category):
    session = SessionLocal()
    try:
        new_transaction = Transaction(
            type=type, amount=amount, category=category, date=date.today()
        )
        session.add(new_transaction)
        session.commit()
        print("Transaction added successfully!")
    finally:
        session.close()


def get_transactions():
    session = SessionLocal()
    try:
        return session.query(Transaction).all()
    finally:
        session.close()


def generate_report(file_format="csv"):
    session = SessionLocal()
    try:
        transactions = session.query(Transaction).all()

        data = [
            {
                "ID": t.id,
                "Type": t.type,
                "Amount": t.amount,
                "Category": t.category,
                "Date": t.date.strftime("%Y-%m-%d"),
            }
            for t in transactions
        ]

        df = pd.DataFrame(data)

        if file_format == "csv":
            file_name = "transactions_report.csv"
            df.to_csv(file_name, index=False)
        elif file_format == "excel":
            file_name = "transactions_report.xlsx"
            df.to_excel(file_name, index=False, engine="openpyxl")
        else:
            print("Invalid file format. Please choose 'csv' or 'excel'.")
            return

        print(f"Report generated successfully: {file_name}")
    finally:
        session.close()
