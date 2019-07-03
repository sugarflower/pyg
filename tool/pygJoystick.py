#!/usr/bin/python3
from pyg.core import *
import pyg.font8x8 as font

setSize((256,256),(384,384))
setTitle("joystick Test")

joystick.init()
jc = joystick.get_count()

print( "number of joystick: " , jc )
j = joystick.Joystick(0)
j.init()


def loop():
	clear()

	font.setPos(0,0)
	font.printStr(j.get_name())

	bt = j.get_numbuttons()
	font.setPos(0,12)
	font.printStr("BUTTONS: "+str(bt))
	for i in range( bt ):
		if j.get_button(i) == 1:
			c = Color(200,100,100)
		else:
			c = Color(50,50,50)
		gfx.box( getSurface(), (i*4, 18, 3, 6), c)

	font.setPos(0,30)
	font.printStr("HAT    : ")
	font.setPos(40,30)
	font.printStr(str(j.get_hat(0)))

	ax = j.get_numaxes()
	font.setPos(0,42)
	font.printStr("AXES   : " + str(ax))
	for i in range( ax ):
		axv = j.get_axis(i) * 64 + 64
		gfx.box( getSurface(), (0, i*6+58 ,axv, 4), Color(50,50,200) )
		gfx.rectangle( getSurface(), (0,i*6+58,128,4), Color(20,20,20) )

run()

