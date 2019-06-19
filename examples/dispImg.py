#!/usr/bin/python3
import pyg as p

p.begin((128, 128), (324, 324))
img = p.imgLoad("res/girl.png")
f = p.TinyFont()

while p._running:
	p.process()
	p.fill( p.Color(50, 50, 80) )	
	p.putImg(img,(0, 0))
	f.print("ENJOY! PyGame with PYG", (16, 64))

p.quit()

