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
import templates


def write_file(which, dir="./"):
    """write <which> file to <dir> (default to CWD)"""
    # DEBUG: only writing to pycache instead of actually writing a new file
    if (
        which.lower().strip(punctuation).replace(" ", "").replace("-", "")
        ) == "cssreset":
        try:
            if (".css" in dir):
                #strip filename off if provided
                i = dir.find(("/" or "\\"), -1)
                dir = dir[:i]
                print(dir)
            with open(f"{dir}reset.css", "x") as f:
                print(templates.CSS_RESET_STRING)
                f.write(templates.CSS_RESET_STRING)
        except FileExistsError:
            print("reset.css already exists in this directory.")


write_file("css_reset", "./reset.css")