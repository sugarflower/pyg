#!/usr/bin/python3

import pyg
pyg.begin((128,128),(384,384))
pyg.setTitle("joystick Test")

pyg.joystick.init()
jc = pyg.joystick.get_count()

print( "number of joystick: " , jc )
j = pyg.joystick.Joystick(0)
j.init()

txt = pyg.TinyFont()



while pyg._running:
	pyg.process()	
	pyg.clear()

	txt.print(j.get_name(),(0,0))
	
	bt = j.get_numbuttons()
	txt.print("BUTTONS: "+str(bt),(0,12))
	for i in range( bt ):
		if j.get_button(i) == 1:
			c = pyg.Color(200,100,100)
		else:
			c = pyg.Color(50,50,50)
		pyg.gfx.box( pyg.surface, (i*4, 18, 3, 6), c)

	txt.print("HAT    : ",(0,30))
	txt.print(str(j.get_hat(0)) , (40,30))

	ax = j.get_numaxes()
	txt.print("AXES   : " + str(ax), (0,42) )
	for i in range( ax ):
		axv = j.get_axis(i) * 64 + 64
		pyg.gfx.box( pyg.surface, (0, i*6+58 ,axv, 4), pyg.Color(50,50,200) )
		pyg.gfx.rectangle( pyg.surface, (0,i*6+58,128,4), pyg.Color(20,20,20) )

pyg.quit()

