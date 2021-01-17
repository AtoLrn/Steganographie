#!/usr/bin/python3.7
# coding: utf-8

########################################################################
import http.server

#from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import os


########################################################################
CURRENT_PATH = "/webpy"
WWW_DEFAULT_PORT = 8080
SERVER = ("", WWW_DEFAULT_PORT)             #all interfaces on the port listen == ""
WWW_PATH = "/"
#WWW_DEFAULT_PAGE = "index.py"

########################################################################
class CGIHTTPRequestHandlerPY(http.server.CGIHTTPRequestHandler):
    def is_cgi(self):
        collapsed_path = http.server._url_collapse_path(urllib.parse.unquote(self.path))
        dir_sep = collapsed_path.find('/', 1)
        self.cgi_info = collapsed_path[:dir_sep], collapsed_path[dir_sep + 1:]
        return True

    def send_head(self):
        path = self.ajouterIndexPY()
        if os.path.exists(path):
            if self.is_python(path):
                return http.server.CGIHTTPRequestHandler.send_head(self)
        return http.server.SimpleHTTPRequestHandler.send_head(self)

    def do_POST(self):
        self.ajouterIndexPY()
        http.server.CGIHTTPRequestHandler.do_POST(self)

    def ajouterIndexPY(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for file in "index.py",:
                path = os.path.join(path, file)
                if os.path.exists(path):
                    if not self.path.rstrip().endswith('/'):
                        self.path += '/'
                    self.path += file
                    break
        return path


#########################################################################
server = http.server.HTTPServer                     #classe du serveur HTTP
handler = CGIHTTPRequestHandlerPY         #classe du gestionnaire de requetes
handler.cgi_directories = [WWW_PATH]
httpd = server(SERVER, handler)                     #instancie le serveur (addr + gestionnaire)

########################################################################
httpd.serve_forever()

