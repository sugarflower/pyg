#!/usr/bin/python3
import pyg 

"""
pyg.init
set real picture size and display size
"""
pyg.init( (80,80), (320,320) )
pyg.setTitle("*pyg test*")


"""
get resource and initialize for application
"""
img = pyg.imgload("res/pic.png")
img2 = pyg.imgload("res/pygame_tiny.png")
pos = [0] * 2 
r = 0

"""
define for sprite sheet
"name" : ( pos x, pos y , width , height )
"""
sp = {
	"player":(0, 0, 8, 8), 
	"tomato":(8, 0, 8, 8)
}


"""
main loop
"""
while pyg._running:
	pyg.process(0.016)

	pyg.putImg(img2,(64,64),flip=pyg.FLIP_H,rotate=r,center=True)
	r = (r + 5)%360
	
	pyg.putImg(img, (0,0))
	pyg.putImg(img, (0,8),  sp["player"])
	pyg.putImg(img, (4,8),  sp["player"], pyg.FLIP_H)

	pyg.putImg(img, (0,16), sp["tomato"])
	pyg.putImg(img, (8,16), sp["tomato"], pyg.FLIP_H)
	pyg.putImg(img, (16,16),sp["tomato"], pyg.FLIP_V)
	pyg.putImg(img, (24,16),sp["tomato"], pyg.FLIP_BOTH)

	pyg.putImg(img, (0,24), sp["player"], rotate=90 )
	pyg.putImg(img, (8,24), sp["player"], rotate=180)
	pyg.putImg(img, (16,24),sp["player"], rotate=270)

	pyg.putImg(img,pyg.get_mousePos(), sp["player"])

	if pyg.isKeyDownCode(27): #ESC key
		pyg._running = False
	
	if pyg.isKeyDown("a"):
		print("true")
	
	if pyg.isAnyKeyDown():
		print("any")

"""
end app
"""
pyg.quit()

