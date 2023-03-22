from src import file_helpers


def test_write_file():
    assert file_helpers.write_file("css_rEset", "css") == True


if __name__ == "__main__":
    test_write_file()
