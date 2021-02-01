import time
from http.server import BaseHTTPRequestHandler, HTTPServer
import router

hostname = "localhost"
hostPort = 8443


class MyServer(BaseHTTPRequestHandler):
	def do_GET(self):
		response = router.route_get(self.path)
		router.send_rep(self, response)

	def do_POST(self):
		length = int(self.headers['Content-Length'])
		body = self.rfile.read(length)
		fields = router.parse_post(body)
		response = router.route_post(self.path, fields)
		router.send_rep(self, response)


myServer = HTTPServer((hostname, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostname, hostPort))

try:
	myServer.serve_forever()
except KeyboardInterrupt:
	pass

myServer.server_close()
print(time.asctime(), "Server Stop %s:%s" % (hostname, hostPort))
