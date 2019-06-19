#!/usr/bin/python3
import pyg as p
import urllib.request as net
import io

p.begin((256, 128))

imgAddr = "https://www.python.org/static/img/python-logo.png"
res = net.urlopen( imgAddr ).read()
imgfile = io.BytesIO(res)
img = p.imgLoad(imgfile)

while p._running:
	p.process()
	p.fill( p.Color(50, 50, 80) )	
	p.putImg(img,(0, 0))

p.quit()

