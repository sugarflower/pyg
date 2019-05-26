#!/usr/bin/python3
import pyg

pyg.begin((128,64),(384,192))
pyg.setTitle("bitmapFont Test")

f = pyg.TinyFont()

f.setColor( pyg.Color(0xff,0xff,0xff))
f.print("HELLO PYG",(0,0))
f.setColor( pyg.Color(0,255,0) )
f.print("ENJOY PyGame with Python :)",(4,6))
f.setColor( pyg.Color(0,0,255) )
f.print("ABCDEFGHIJKLMNOPQRSTUVWXYZ",(0,12))
f.print("abcdefghijklmnopqrstuvwxyz",(0,18))
f.print("0123456789!!#$%&'()@`[]{}:*;+<>,.?/\_",(0,24))

while pyg._running:
	pyg.process()

pyg.quit()
