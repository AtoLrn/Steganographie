#!/usr/bin/python
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
<<<<<<< HEAD
        
=======
        petit test
>>>>>>> afb4a4a... Rectification part 2
    </body>
</html>
"""

print(html)