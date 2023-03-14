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


import templates


def write_file(which, dir="./"):
    """write <which> file to <dir> (default to CWD)"""
    # TODO: allow providing relative path
    try:
        with open("reset.css", "x") as f:
            f.write(templates.CSS_RESET_STRING)
    except FileExistsError:
        print("reset.css already exists in this directory.")
