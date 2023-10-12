#!/usr/bin/python3

"""
Convert Markdown to HTML
"""


import sys
import os
if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not os.path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}")
        sys.exit(1)

    sys.exit(0)
