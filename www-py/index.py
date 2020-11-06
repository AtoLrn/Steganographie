# coding: utf-8
import cgi

########################################################################
CURRENT_PATH			= "/webpy/"
WWW_PATH			= "www-py/"
WWW_DEFAULT_PAGE 		= CURRENT_PATH+WWW_PATH+"index.html"
WWW_DEFAULT_DOWLOAD_PATH 	= CURRENT_PATH+"download/"
########################################################################
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