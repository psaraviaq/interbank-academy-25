import pytest

from domain.models import Transaction
from infrastructure.data import read_transactions_from_csv


def test_read_valid_csv(tmp_path):
    data = "id,tipo,monto\n1,Crédito,100.0\n2,Débito,50.0\n3,Crédito,200.0"
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(data)
    expected_transactions = [
        Transaction(id="1", type="Crédito", amount=100.0),
        Transaction(id="2", type="Débito", amount=50.0),
        Transaction(id="3", type="Crédito", amount=200.0),
    ]
    assert read_transactions_from_csv(csv_file) == expected_transactions


def test_file_not_found(tmp_path, capsys):
    csv_file = tmp_path / "not_found.csv"
    with pytest.raises(SystemExit):
        read_transactions_from_csv(csv_file)
    captured = capsys.readouterr()
    assert "File not found" in captured.out


@pytest.mark.parametrize(
    "data",
    [
        "id,tipo,monto\n1,Crédito,100.0\n2,Débito,invalid",
        "id,tipo,monto\n3,Credit,200.0\n4,Debit,75.0",
    ],
)
def test_invalid_rows(tmp_path, data, capsys):
    csv_file = tmp_path / "data.csv"
    csv_file.write_text(data)
    with pytest.raises(SystemExit):
        read_transactions_from_csv(csv_file)
    captured = capsys.readouterr()
    assert "Error reading CSV file" in captured.out
