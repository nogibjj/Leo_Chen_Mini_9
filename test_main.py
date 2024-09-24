from main import print_table


def test_print_table():
    table = print_table()
    assert table is not None


if __name__ == "__main__":
    test_print_table()