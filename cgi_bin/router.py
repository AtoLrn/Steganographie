import time
import s_function
import re
import os


def route_get(URI):
	match = re.match("/retrieve-([a-zA-Z0-9._-]+)", URI)
	if URI == "/":
		data = bytes(open("../template/index.html", "r").read(), "utf-8")
		return {"code": 200, "file": data, "type": "text/html"}
	elif match is not None:
		filenmame = match.group(1)
		type = filenmame.split('.')
		if type[len(type)-1] == "bmp":
			type = "image/bmp"
		elif type[len(type)-1] == "png":
			type = "image/png"
		else:
			return {"code": "403", "file": bytes("Interdit", "utf-8")}
		if os.path.exists("../img/" + filenmame):
			f = open("../img/" + filenmame, "rb")
			body = f.read()
			f.close()
			os.remove("../img/" + filenmame)
		else:
			return {"code": 404, "file": "Not Found"}
		return {"code": 200, "file": body, "type": type}
	else:
		return {"code": 404, "file": "Not Found"}


def route_post(URI, body):
	if URI == "/stegano":
		value = {}
		for i in range(len(body)):
			value[body[i]["name"]] = body[i]["value"]
			if "filename" in body[i]:
				value["filename"] = body[i]["filename"]
		filename = str(time.time()).replace(".", "_") + value["filename"]
		save_file(filename, "../img/", value["img"])
		message = s_function.encryptage(value["message"].decode("utf-8"), value["password"].decode("utf-8"))
		f = filename.split('.')
		if f[len(f)-1] == "bmp":
			s_function.steganoBMP("../img/" + filename, message, len(message))
		elif f[len(f)-1] == "png":
			s_function.encodePng("../img/" + filename, message)
		else:
			return {"code": "409", "file": "Mauvais type"}
		return {"code": 200, "file": bytes(filename, "utf-8"), "type": "text/plain"}
	elif URI == "/stegano-reverse":
		value = {}
		for i in range(len(body)):
			value[body[i]["name"]] = body[i]["value"]
			if "filename" in body[i]:
				value["filename"] = body[i]["filename"]
		filename = str(time.time()).replace(".", "_") + value["filename"]
		save_file(filename, "../img/", value["img"])
		f = filename.split('.')
		if f[len(f) - 1] == "bmp":
			message = s_function.steganoBMPReverse("../img/" + filename)
		elif f[len(f) - 1] == "png":
			message = s_function.decodePng("../img/" + filename)
		else:
			return {"code": "409", "file": "Mauvais type"}
		message = s_function.decryptage(message, value["password"].decode("utf8"))
		return {"code": 200, "file": bytes(message, "utf-8"), "type": "text/plain"}
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
				i += 2
				while i < len(lines) and lines[i][0] != 45:
					value[len(value)-1] += bytes("\r\n", 'utf-8')+lines[i]
					i += 1
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
	if response['code'] == 200:
		self.send_response(200)
		self.send_header("Content-type", response['type'])
		self.end_headers()
		self.wfile.write(response['file'])
	else:
		self.send_response(response['code'])
		self.send_header("Content-type", 'text/plain')
		self.end_headers()
		self.wfile.write(bytes("", "utf-8"))

