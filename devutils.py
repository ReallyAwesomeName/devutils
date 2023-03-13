#!C:\Users\jgeog\AppData\Local\Programs\Python\Python311\python
#
# TODO: CLI arguments for various files or file additions such as:
# TODO: adding argparse skeleton to a file
# TODO: make webapp directory structure with skeletons

import templates
import argparse


def write_file(which, dir="./"):
    """write <which> file to <dir> (default to CWD)"""
    # TODO: allow providing relative path
    try:
        with open("reset.css", "x") as f:
            f.write(templates.CSS_RESET_STRING)
    except FileExistsError:
        print("reset.css already exists in this directory.")


def main():
    """driver function for devutils"""
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Build custom project structures and skeletons from templates"
    )
    parser.add_argument("-x", "--xxxxx", type=None, default=None, help="")

    args = parser.parse_args()
    main()
