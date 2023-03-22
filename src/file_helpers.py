#
# tasks.py
# desc: collection of functions for development tasks
#
# Author: Rin | Discord: Rin#0304
# https://github.com/ReallyAwesomeName/devutils
#
# ========================================================================== #
#                                                                            #
#   devutils - Utilities for setting up and managing development environment #
#   Copyright (C) 2023  Rin                                                  #
#                                                                            #
#   This file is a part of devutils                                          #
#                                                                            #
#   devutils is free software: you can redistribute it and/or modify         #
#   it under the terms of the GNU General Public License as published by     #
#   the Free Software Foundation, either version 3 of the License, or        #
#   (at your option) any later version.                                      #
#                                                                            #
#   devutils is distributed in the hope that it will be useful,              #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #
#   GNU General Public License for more details.                             #
#                                                                            #
#   You should have received a copy of the GNU General Public License        #
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.   #
#                                                                            #
# ========================================================================== #


from string import punctuation
from . import templates
from os import makedirs, curdir
import re


def write_file(fname, ftype, dir=curdir):
    """
    write <fname> file with <ext> extension to <dir> (default to curdir)

    Args:
        fname (string): name of file to write
        ext (str): extension of file to write
        dir (string, optional): location to write file. Defaults to curdir.
    """
    if dir == curdir:
        dir = f"{curdir}/{fname}.{ftype}"
    elif dir != curdir:
        dir = f"{dir}/{fname}.{ftype}"
    # check file type and set skeleton template to use
    # todo: add more cases and directory structures
    match ftype.lower().strip():
        case "css":
            THIS_TEMPLATE = templates.CSS_SKELETON
        case "html":
            THIS_TEMPLATE = templates.HTML_SKELETON
        case _:
            # REVIEW: huh?
            raise ValueError(f"Extension {ftype} not supported")

    # write the file
    try:
        with open(f"{dir}", "x") as f:
            f.write(f"{THIS_TEMPLATE}\n")

    except FileExistsError:
        return print(f"{dir} already exists")

    print(f"wrote file {fname}.{ftype} to {dir}")
    return True


def build_dir_structure(dir_structure, dir=curdir):
    """
    build directory structure from <dir_structure>

    Args:
        dir_structure (string): string specifying a project type
        dir (string, optional): target parent directory. Defaults to curdir.
    """
    try:
        match dir_structure.lower().strip():
            case "javascript_webapp":
                THIS_TEMPLATE = templates.DIR_STRUCTURE_JAVASCRIPT_WEBAPP
            case "python_project":
                THIS_TEMPLATE = templates.DIR_STRUCTURE_PYTHON_PROJECT
            case _:
                raise ValueError(f"Directory structure {dir_structure} not supported")
    # REVIEW: huh?
    except ValueError:
        return ValueError


# TEMP:
if __name__ == "__main__":
    write_file("css_rEset", "css")
