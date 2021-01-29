#!/usr/bin/python3.7
# coding: utf-8

########################################################################
import cgi

########################################################################
CURRENT_PATH = "/webpy/"
#WWW_PATH = "template/"
WWW_DEFAULT_PAGE = CURRENT_PATH+"index.html"

########################################################################
def index():
	f=open(WWW_DEFAULT_PAGE, "r")
	print(f.read())
	f.close()
 
#traitement functions.py, bmp.py, png.py
#def datas(form):

########################################################################
form = cgi.FieldStorage()
if form.getvalue('id') == None:
	print("Content-type: text/html; charset=utf-8\n")
	index()
#else:
	#datas(form)


"""
print(<!DOCTYPE html>
<html>
    <head>
        <title>Mon super site en Python </title>
    </head>
     <body>
          <p>Vous êtes jaloux, hein ?</p>
     </body>
</html> )
"""