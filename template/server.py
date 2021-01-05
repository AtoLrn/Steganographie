#!/usr/bin/python3
#coding:utf-8
import http.server
#################################
CURRENT_PATH = "/webpy"
WWW_DEFAULT_PORT = 8080
WWW_DEFAULT_IP = ("", WWW_DEFAULT_PORT)             #all interfaces on the port listen == ""
WWW_PATH = "/www_cgi-bin"

########################################################################
server = http.server.HTTPServer                     #classe du serveur HTTP
handler = http.server.CGIHTTPRequestHandler         #classe du gestionnaire de requetes
handler.cgi_directories = [WWW_PATH]
httpd = server(WWW_DEFAULT_IP, handler)             #instancie le serveur (addr + gestionnaire)

#######################################

print("serving at port", WWW_DEFAULT_PORT)
httpd.serve_forever()

