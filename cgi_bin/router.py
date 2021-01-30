#!/usr/bin/python3.7

########################################################################

def route_get(URI):
    if URI == "/":
        data = bytes(open("index.html", "r").read(), "utf-8")
        return {"code": 200, "file": data, "type": "text/html"}
    elif URI == "/bonjour":
        return {"code": 200, "file": bytes("TEST", "utf-8"), "type": "text/plain"}
    else:
        return {"code": 404}