from presentation.cli import parse_arguments, display_report, display_error
from infrastructure.data import read_transactions_from_csv
from application.services import TransactionService


def main():
    try:
        # * Parse input, load transactions, and show the report.
        csv_file = parse_arguments()
        transactions = read_transactions_from_csv(csv_file)
        service = TransactionService(transactions)
        display_report(service)
    except Exception as e:
        #! Display an error if something goes wrong.
        display_error(f"An unexpected error occurred: {str(e)}")


if __name__ == "__main__":
    main()
