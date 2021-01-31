#!/usr/bin/python3.7

########################################################################

def route_get(URI):
    if URI == "/":
        data = bytes(open("template/index.html", "r").read(), "utf-8")
        return {"code": 200, "file": data, "type": "text/html"}
    else:
        return {"code": 404}


def route_post(URI):
    if URI == "/stegano":
        img = bytes(open("template/test.html", "r").read(), "utf-8")
        return {"code": 200, "file": img, "type": "text/html"}
    else:
        return {"code": 404}

