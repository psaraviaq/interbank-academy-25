from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from application.services import TransactionService


def display_report(service: TransactionService):
    # * Get metrics from the service.
    final_balance = service.get_final_balance()
    highest_transaction = service.get_highest_transaction()
    credit_count, debit_count = service.get_transaction_counts()

    # * Build report table.
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="green")
    table.add_row("Final Balance", f"{final_balance:.2f}")
    table.add_row(
        "Highest Transaction",
        (
            f"ID {highest_transaction.id} - {highest_transaction.amount:.2f}"
            if highest_transaction
            else "N/A"
        ),
    )
    table.add_row("Credit Transactions", str(credit_count))
    table.add_row("Debit Transactions", str(debit_count))

    # * Display the table in a panel.
    console = Console()
    panel = Panel(
        table,
        title="Transaction Report",
        title_align="left",
        border_style="bright_blue",
    )
    console.print(panel)
