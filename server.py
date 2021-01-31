#!/usr/bin/python3.7
# coding: utf-8

########################################################################
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi_bin.router

########################################################################
DEFAULT_PORT = 8080
HOSTNAME = ("", DEFAULT_PORT)               #all interfaces on the port listen == ""
WWW_PATH = "/cgi-bin/"


########################################################################
class ServerPY(BaseHTTPRequestHandler):
    def do_GET(self):
        response = cgi_bin.router.route_get(self.path)
        if response['code'] != 404:
            self.send_response(200)
            self.send_header("Content-type", response['type'])
            self.end_headers()
            self.wfile.write(response['file'])
        else:
            self.send_response(404)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("Introuvable", "utf-8"))

    def do_POST(self):
        response_post = cgi_bin.router.route_post(self.path)
        if response_post['code'] != 404:
            self.send_response(200)
            self.send_header("Content-type", response_post['type'])
            self.end_headers()
            self.wfile.write(response_post['file'])
        else:
            self.send_response(404)
            self.send_header("Content-type", 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("Introuvable2", "utf-8"))


#########################################################################
handler = ServerPY                                      #classe du gestionnaire de requetes
handler.cgi_directories = [WWW_PATH]
httpd = HTTPServer(HOSTNAME, handler)                   #instancie le serveur (addr + gestionnaire)

########################################################################
print(time.asctime(), "Server Starts - %s:%s" % (HOSTNAME, DEFAULT_PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print(time.asctime(), "Server Stop %s:%s" % (HOSTNAME, DEFAULT_PORT))
