#!/usr/bin/python3.7
# coding: utf-8

########################################################################
import http.server
import urllib.parse
import os #permet ainsi de gérer l’arborescence des fichiers

########################################################################
CURRENT_PATH = "/home/stegano/"
WWW_DEFAULT_PORT = 8080
SERVER = ("", WWW_DEFAULT_PORT)             #all interfaces on the port listen == ""
WWW_PATH = "cgi-bin/"
WWW_DEFAULT_PAGE = "index.py"

########################################################################
class CGIHTTPRequestHandlerPY(http.server.CGIHTTPRequestHandler):
    def is_cgi(self):
        #Teste si self.path correspond à un script CGI
        collapsed_path = http.server._url_collapse_path(self.path)
        if collapsed_path == '//':
            self.path = '/index.py'
            collapsed_path = http.server._url_collapse_path(self.path)
        dir_sep = collapsed_path.find('/', 1)
        head, tail = collapsed_path[:dir_sep], collapsed_path[dir_sep + 1:]
        if head in self.cgi_directories:
            self.cgi_info = head, tail
            return True
        return False

    def send_head(self):
        path = self.ajouterIndexPY()
        if os.path.exists(path):
            if self.is_python(path): #Teste si le chemin argument est un script Python
                return http.server.CGIHTTPRequestHandler.send_head(self)
        return http.server.SimpleHTTPRequestHandler.send_head(self)

    def do_POST(self):
        self.ajouterIndexPY()
        http.server.CGIHTTPRequestHandler.do_POST(self)

    def ajouterIndexPY(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for file in CURRENT_PATH+WWW_PATH+WWW_DEFAULT_PAGE:
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
handler.cgi_directories = [CURRENT_PATH+WWW_PATH]
httpd = server(SERVER, handler)                     #instancie le serveur (addr + gestionnaire)

########################################################################
httpd.serve_forever()
