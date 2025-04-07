import csv
from typing import List

from domain.enums import TransactionType
from domain.models import Transaction
from presentation.cli import display_error


def read_transactions_from_csv(csv_file: str) -> List[Transaction]:
    transactions = []
    try:
        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # * Convert row to a Transaction instance.
                transaction = Transaction(
                    id=row["id"],
                    type=TransactionType(row["tipo"]),
                    amount=float(row["monto"]),
                )
                transactions.append(transaction)
    #! Handle errors: File not found or any other exception.
    except FileNotFoundError:
        display_error(f"File not found: {csv_file}")
    except Exception as e:
        display_error(f"Error reading CSV file: {str(e)}")

    return transactions
