import pytest

from application.services import TransactionService
from domain.models import Transaction


@pytest.fixture
def fake_transactions():
    return [
        Transaction(id="1", type="Crédito", amount=100.0),
        Transaction(id="2", type="Débito", amount=50.0),
        Transaction(id="3", type="Crédito", amount=200.0),
        Transaction(id="4", type="Débito", amount=75.0),
        Transaction(id="5", type="Crédito", amount=150.0),
    ]


@pytest.fixture
def transaction_service(fake_transactions):
    return TransactionService(fake_transactions)


def test_final_balance(transaction_service):
    expected_balance = 325.0
    assert transaction_service.get_final_balance() == expected_balance
