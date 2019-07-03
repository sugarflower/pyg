#!/usr/bin/python
from pyg import *
import pyg.font8x8 as font
import random

setSize((160,160),(320,320))
setTitle("PYG2 Test")	
img = loadImage("res/pic.png")

def loop():
	clear()
	fill(Color(100,0,0))
	font.setPos(20,80)
	font.printStr("hello world")
	putImage(img,(50,50))
	putImage(img,(0,0))
	setOffset((random.randint(0,10)-5,random.randint(0,10)-5))

	"""
	e = getEvent()
	if e != None:
		print(e)
		if e.type == 6:
			print(e.button)
	"""
run()

