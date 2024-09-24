from mylib.lib import statistics
from tabulate import tabulate


def print_table():
    mean, median, std = statistics()
    table_data = [["Mean", mean], ["Median", median], ["Standard Deviation", std]]
    print(tabulate(table_data, headers=["Statistic", "Value"], tablefmt="fancy_grid"))
    return table_data


if __name__ == "__main__":
    print_table()