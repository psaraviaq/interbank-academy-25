from typing import List, Optional, Tuple

from domain.models import Transaction


class TransactionService:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions

    def get_final_balance(self) -> float:
        credit_total = 0.0
        debit_total = 0.0
        for t in self.transactions:
            # * Add to credit total if it's a credit.
            if t.type.value == "Crédito":
                credit_total += t.amount
            # * Add to debit total if it's a debit.
            elif t.type.value == "Débito":
                debit_total += t.amount
        return credit_total - debit_total

    def get_highest_transaction(self) -> Optional[Transaction]:
        highest_transaction = None
        for t in self.transactions:
            # * Update highest_transaction if None or t.amount is higher
            if not highest_transaction or t.amount > highest_transaction.amount:
                highest_transaction = t
        return highest_transaction

    def get_transaction_counts(self) -> Tuple[int, int]:
        credit_count = 0
        debit_count = 0
        for t in self.transactions:
            # * Increment count based on transaction type.
            if t.type.value == "Crédito":
                credit_count += 1
            elif t.type.value == "Débito":
                debit_count += 1
        return credit_count, debit_count
