#!/usr/bin/python3
"""
Convert Markdown to HTML
"""


import sys
from os import path
if __name__ == "__main__":
    if len(sys.argv) < 3:
        message = "Usage: ./markdown2html.py README.md README.html\n"
        sys.stderr.write('{}'.format(message))
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    if not path.exists(input_file):
        sys.stderr.write("Missing {}\n".format(input_file))
        sys.exit(1)

    sys.exit(0)
