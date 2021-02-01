import time
import function


def route_get(URI):
	if URI == "/":
		data = bytes(open("index.html", "r").read(), "utf-8")
		return {"code": 200, "file": data, "type": "text/html"}
	elif URI == "/test":
		return {"code": 200, "file": bytes("TEST", "utf-8"), "type": "text/plain"}
	else:
		return {"code": 404}


def route_post(URI, body):
	if URI == "/stegano":
		value = {}
		for i in range(len(body)):
			value[body[i]["name"]] = body[i]["value"]
			if "filename" in body[i]:
				value["filename"] = body[i]["filename"]
		filename = str(time.time()) + value["filename"]
		save_file(filename, "./", value["img"])
		return {"code": 200, "file": bytes("RECEIVED", "utf-8"), "type": "text/plain"}
	elif URI == "/stegano-reverse":
		value = {}
		for i in range(len(body)):
			value[body[i]["name"]] = body[i]["value"]
			if "filename" in body[i]:
				value["filename"] = body[i]["filename"]
		filename = str(time.time()) + value["filename"]
		save_file(filename, "./", value["img"])
		return {"code": 200, "file": bytes("RECEIVED", "utf-8"), "type": "text/plain"}
	else:
		return {"code": 404}


def save_file(name, path, data):
	f = open(path + name, "wb")
	f.write(data)
	f.close()


def parse_post(body):
	lines = []
	temp = []
	value = []
	fields = []
	i = 0
	while i < len(body):
		if i < len(body) - 1 and body[i] == 13 and body[i + 1] == 10:
			lines.append(bytes(temp))
			temp.clear()
			i += 2
			continue
		if i < len(body):
			temp.append(body[i])
		i += 1
	for i in range(len(lines)):
		try:
			if len(lines[i]) == 0:
				value.append(lines[i + 1])
			data = lines[i][:20].decode("utf-8")
			if data == "Content-Disposition:":
				line = lines[i].decode("utf-8")
				temp = line.split(":")[1].split(";")
				temp.pop(0)
				field = {}
				for temp2 in temp:
					a, b = temp2.split("=")
					field[a.strip()] = b
				fields.append(field)
		except UnicodeDecodeError:
			pass
	for i in range(len(fields)):
		fields[i]["name"] = fields[i]["name"][1:-1]
		try:
			fields[i]["filename"] = fields[i]["filename"][1:-1]
		except KeyError:
			pass
		fields[i]["value"] = value[i]
	return fields


def send_rep(self, response):
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

