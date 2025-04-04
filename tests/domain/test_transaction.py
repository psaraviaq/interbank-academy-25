import pytest
from pydantic import ValidationError

from domain.enums import TransactionType
from domain.models import Transaction


@pytest.mark.parametrize(
    "id, type, amount, expected_type",
    [
        ("1", "Crédito", 100.0, TransactionType.CREDIT),
        ("2", "Débito", 50.0, TransactionType.DEBIT),
    ],
)
def test_valid_transaction(id, type, amount, expected_type):
    transaction = Transaction(id=id, type=type, amount=amount)
    assert transaction.id == id
    assert transaction.type == expected_type
    assert transaction.amount == amount


@pytest.mark.parametrize(
    "id, type, amount",
    [
        ("3", "Crédito", "Two hundred"),
        ("4", "Unknown", 75.0),
        ("5", 123, 100.0),
    ],
)
def test_invalid_transaction(id, type, amount):
    with pytest.raises(ValidationError):
        Transaction(id=id, type=type, amount=amount)
