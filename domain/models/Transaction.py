from pydantic import BaseModel

from domain.enums import TransactionType


class Transaction(BaseModel):
    id: str
    type: TransactionType
    amount: float
