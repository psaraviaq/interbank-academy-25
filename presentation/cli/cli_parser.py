import sys

from .cli_display import display_error


def parse_arguments():
    # * Require exactly one argument: the CSV file path.
    if len(sys.argv) < 2:
        display_error("No CSV file provided. Please specify a CSV file path.")
    if len(sys.argv) > 2:
        display_error("Too many arguments. Please provide only one CSV file path.")

    csv_file = sys.argv[1]
    return csv_file
