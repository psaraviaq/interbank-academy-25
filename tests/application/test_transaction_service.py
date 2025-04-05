import pytest

from application.services import TransactionService
from domain.models import Transaction


@pytest.fixture
def transaction_service():
    return TransactionService(
        [
            Transaction(id="1", type="Crédito", amount=100.0),
            Transaction(id="2", type="Débito", amount=50.0),
            Transaction(id="3", type="Crédito", amount=200.0),
            Transaction(id="4", type="Débito", amount=75.0),
            Transaction(id="5", type="Crédito", amount=150.0),
        ]
    )


@pytest.fixture
def empty_service():
    return TransactionService([])


# * --------------------- get_final_balance() ---------------------
def test_final_balance(transaction_service):
    expected_balance = 325.0
    assert transaction_service.get_final_balance() == expected_balance


def test_empty_final_balance(empty_service):
    expected_balance = 0.0
    assert empty_service.get_final_balance() == expected_balance
