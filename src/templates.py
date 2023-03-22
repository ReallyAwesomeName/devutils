#
# templates.py
# desc: collection of templates for development tasks
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


# TODO: make webapp directory structure with skeletons


# NOTE: HTML_SKELETON, CSS_SKELETON, CSS_RESET_STRING, FILE_HEADER_PYTHON_GNUV3,

HTML_SKELETON = (
    "<!DOCTYPE html>\n"
    "<html>\n"
    "<head>\n"
    '	<meta charset="UTF-8">\n'
    '	<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
    "	<title>My Responsive Web App</title>\n"
    '	<link rel="stylesheet" href="assets/css/reset.css">\n'
    '	<link rel="stylesheet" href="assets/css/style.css">\n'
    "</head>\n"
    "<body>\n"
    "	<header>\n"
    "		<h1>Web App</h1>\n"
    "		<nav>\n"
    "			<ul>\n"
    '				<li><a href="#">Home</a></li>\n'
    '				<li><a href="#">About</a></li>\n'
    '				<li><a href="#">Contact</a></li>\n'
    "			</ul>\n"
    "		</nav>\n"
    "	</header>\n"
    "	<main>\n"
    "		<section>\n"
    "			<h2>Section 1</h2>\n"
    "			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet ipsum in risus vehicula laoreet vel nec mauris.</p>\n"
    "		</section>\n"
    "		<section>\n"
    "			<h2>Section 2</h2>\n"
    "			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet ipsum in risus vehicula laoreet vel nec mauris.</p>\n"
    "		</section>\n"
    "		<section>\n"
    "			<h2>Section 3</h2>\n"
    "			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet ipsum in risus vehicula laoreet vel nec mauris.</p>\n"
    "		</section>\n"
    "	</main>\n"
    "	<footer>\n"
    "		<p>&copy; 2023 Web App</p>\n"
    "	</footer>\n"
    "</body>\n"
    "</html>\n"
    "\n"
)

CSS_SKELETON = (
    "/* style.css */\n"
    "* {\n"
    "box-sizing: border-box;\n"
    "}\n"
    "body {\n"
    "	font-family: Arial, sans-serif;\n"
    "	margin: 0;\n"
    "	padding: 0;\n"
    "}\n"
    "\n"
    "header {\n"
    "	background-color: #333;\n"
    "	color: #fff;\n"
    "	padding: 20px;\n"
    "}\n"
    "\n"
    "header h1 {\n"
    "	margin: 0;\n"
    "}\n"
    "\n"
    "nav ul {\n"
    "	margin: 0;\n"
    "	padding: 0;\n"
    "	list-style: none;\n"
    "}\n"
    "\n"
    "nav li {\n"
    "	display: inline-block;\n"
    "	margin-right: 20px;\n"
    "}\n"
    "\n"
    "nav li:last-child {\n"
    "	margin-right: 0;\n"
    "}\n"
    "\n"
    "nav a {\n"
    "	color: #fff;\n"
    "	text-decoration: none;\n"
    "}\n"
    "\n"
    "main {\n"
    "	margin: 20px;\n"
    "}\n"
    "\n"
    "section {\n"
    "	margin-bottom: 40px;\n"
    "}\n"
    "\n"
    "section h2 {\n"
    "	margin-top: 0;\n"
    "}\n"
    "\n"
    "footer {\n"
    "	background-color: #333;\n"
    "	color: #fff;\n"
    "	padding: 20px;\n"
    "	text-align: center;\n"
    "}\n"
)

CSS_RESET_STRING = (
    "/* reset.css */\n"
    "/* Resets the box size of every element */\n"
    "* {\n"
    "  margin: 0;\n"
    "  padding: 0;\n"
    "  box-sizing: border-box;\n"
    "}\n"
    "\n"
    "/* Gives the body element a parent height to compare against */\n"
    "html {\n"
    "  height: 100%;\n"
    "}\n"
    "\n"
    "body {\n"
    "  min-height: 100%;\n"
    "  line-height: 1;\n"
    "  font-family: sans-serif;\n"
    "}\n"
    "\n"
    "h1,\n"
    "h2,\n"
    "h3,\n"
    "h4,\n"
    "h5,\n"
    "h6 {\n"
    "  font-size: 100%;\n"
    "}\n"
    "\n"
    "/* Matches the font of special elements to the rest of the page */\n"
    "input,\n"
    "select,\n"
    "option,\n"
    "optgroup,\n"
    "textarea,\n"
    "button,\n"
    "pre,\n"
    "code {\n"
    "  font-size: 100%;\n"
    "  font-family: inherit;\n"
    "}\n"
    "\n"
    "/* Removes default bullet points from lists */\n"
    "ol,\n"
    "ul {\n"
    "  list-style: none;\n"
    "}\n"
)

# NOTE: Placeholders: <file_name.py>, <file_description>, <author_names>,
# NOTE: <author_contacts>, <repo_name>, <project_name>, <current_year>
FILE_HEADER_PYTHON_GNUV3 = (
    "#\n"
    "# <file_name.py>\n"
    "# desc: <file_description>\n"
    "#\n"
    "# Author: <author_names> | <author_contacts>\n"
    "# <link_to_repo>\n"
    "#\n"
    "# ========================================================================== #\n"
    "#                                                                            #\n"
    "#   <project_name> - <project_description>                                   #\n"
    "#   Copyright (C) <current_year>  <author_names>                             #\n"
    "#                                                                            #\n"
    "#   This file is a part of <project_name>                                    #\n"
    "#                                                                            #\n"
    "#   <project_name> is free software: you can redistribute it and/or modify   #\n"
    "#   it under the terms of the GNU General Public License as published by     #\n"
    "#   the Free Software Foundation, either version 3 of the License, or        #\n"
    "#   (at your option) any later version.                                      #\n"
    "#                                                                            #\n"
    "#   <project_name> is distributed in the hope that it will be useful,        #\n"
    "#   but WITHOUT ANY WARRANTY; without even the implied warranty of           #\n"
    "#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the            #\n"
    "#   GNU General Public License for more details.                             #\n"
    "#                                                                            #\n"
    "#   You should have received a copy of the GNU General Public License        #\n"
    "#   along with this program.  If not, see <https://www.gnu.org/licenses/>.   #\n"
    "#                                                                            #\n"
    "# ========================================================================== #\n"
)

# TODO: finish these
DIR_STRUCTURE_PYTHON_PROJECT = (
    "<repo_name>/"
    "----.gitignore"
    "----COPYING"
    "----main.py"
    "----README.md"
    "----src/"
    "--------module.py"
)

DIR_STRUCTURE_JAVASCRIPT_WEBAPP = (
    "<repo_name>/"
    "----index.html"
    "README.md"
    "----assets/"
    "--------css/"
    "------------style.css"
    "--------js/"
    "------------script.js"
    "--------img/"
)
