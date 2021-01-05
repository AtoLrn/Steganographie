#!/usr/bin/python3
# coding: utf-8
import cgi
form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

print(form.getvalue("name"))

html = """<!DOCTYPE html>
    <head>
        <title>Steganography</title>
    </head>
    <body>

    </body>
</html>
"""

print(html)