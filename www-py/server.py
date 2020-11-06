#!/usr/bin/python3
# #coding:utf-8

########################################################################
import http.server

########################################################################
CURRENT_PATH = "/webpy"
WWW_DEFAULT_PORT = 8080
WWW_DEFAULT_IP = ("51.178.50.244", WWW_DEFAULT_PORT)
WWW_DEFAULT_PAGE = "index.py"
WWW_PATH = "/www-py"
WWW_DEFAULT_DOWLOAD_PATH = CURRENT_PATH+"download/"
STEGANO = CURRENT_PATH+""

########################################################################
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = [CURRENT_PATH+WWW_PATH]

httpd = server(address, handler)

print("serving at port", WWW_DEFAULT_PORT)
httpd.serve_forever()

