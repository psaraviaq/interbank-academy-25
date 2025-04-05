from typing import List

from domain.models import Transaction


class TransactionService:
    def __init__(self, transactions: List[Transaction]):
        self.transactions = transactions

    def get_final_balance(self) -> float:
        credit_total = 0.0
        debit_total = 0.0
        for t in self.transactions:
            if t.type.value == "Crédito":
                credit_total += t.amount
            elif t.type.value == "Débito":
                debit_total += t.amount
        return credit_total - debit_total
