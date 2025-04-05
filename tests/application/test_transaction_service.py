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
    assert empty_service.get_final_balance() == 0.0


# * --------------------- get_highest_transaction() ---------------------
def test_highest_transaction(transaction_service):
    expected_transaction = Transaction(id="3", type="Crédito", amount=200.0)
    assert transaction_service.get_highest_transaction() == expected_transaction


def test_empty_highest_transaction(empty_service):
    assert empty_service.get_highest_transaction() == None


# * --------------------- get_transaction_counts() ---------------------
def test_transaction_counts(transaction_service):
    expected_counts = (3, 2)
    assert transaction_service.get_transaction_counts() == expected_counts


def test_empty_transaction_counts(empty_service):
    assert empty_service.get_transaction_counts() == (0, 0)
