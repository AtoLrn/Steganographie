#!/usr/bin/python3.7

import cgi
import cgi_bin.function
import os

########################################################################


def route_get(URI):
    if URI == "/":
        data = bytes(open("template/index.html", "r").read(), "utf-8")
        return {"code": 200, "file": data, "type": "text/html"}
    else:
        return {"code": 404}


def route_post(URI):
    form = cgi.FieldStorage()
    image = form['img']
    ext = os.path.splitext(image)
    if URI == "/stegano":
        msg = form['msg']
        pwd = form['pwd']

        if ext == ".bmp":
            #traitement fonction bmp
            return {"code": 200, "file": image, "type": "image/bmp"}

        else if ext == ".png":
            #traitement fonction png
            return {"code": 200, "file": image, "type": "image/png"}

        else:
            return {"code": 404}

    else if URI == "/stegano_reverse":
        img = form['img']
        pwd = form['pwd']

        if ext == ".bmp":
            #traitement fonction bmp
            return {"code": 200, "file": msg, "type": "text/html"}

        else if ext == ".png":
            msg = function.decodePng(image)
            return {"code": 200, "file": msg, "type": "text/html"}

        else:
            return {"code": 404}

    else:
        return {"code": 404}