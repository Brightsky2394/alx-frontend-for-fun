#!/usr/bin/python3
"""
Markdown to HTML
"""


import sys
from os import path

if __name__ == '__main__':
    if len(sys.argv) != 3:
        message = "Usage: ./markdown2html.py README.md README.html"
        sys.stderr.write("{}\n".format(message))
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not path.exists(input_file):
        sys.stderr.write(f"Missing {input_file}\n")
        sys.exit(1)

    with open(input_file, mode='r') as md_file:
        lines = md_file.readlines()

    with open(output_file, mode='w') as html_file:
        for line in lines:
            if line.startswith('#'):
                count = line.count('#')
                content = line.strip('# ').strip()
                html_header = f"<h{count}>{content}</h{count}>\n"
                html_file.write(html_header)
            else:
                html_file.write(line)

    sys.exit(0)
