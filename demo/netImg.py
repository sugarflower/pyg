#!/usr/bin/python3
import pyg
import urllib.request as net
import io

class main:
	def setup(self):
		pyg.setSize((512,256))
		imgAddr = "https://www.python.org/static/img/python-logo.png"
		res = net.urlopen( imgAddr ).read()
		imgfile = io.BytesIO( res )
		self.img = pyg.loadImage( imgfile )
	
	def loop(self):
		pyg.fill( pyg.Color(50,50,80) )
		pyg.putImage( self.img, (256,128), center=True )

m = main()
pyg.run(m)

