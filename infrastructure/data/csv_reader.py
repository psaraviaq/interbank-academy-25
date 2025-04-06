import csv
from typing import List

from domain.enums import TransactionType
from domain.models import Transaction


def read_transactions_from_csv(csv_file: str) -> List[Transaction]:
    transactions = []
    try:
        with open(csv_file, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # * Convert row to a Transaction instance.
                transaction = Transaction(
                    id=row["id"],
                    type=TransactionType(row["type"]),
                    amount=float(row["amount"]),
                )
                transactions.append(transaction)
        return transactions
    #! Handle errors: File not found or any other exception.
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {csv_file}")
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")
