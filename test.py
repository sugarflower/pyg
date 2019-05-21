#!/usr/bin/python3
import pyg

pyg.init((80,80),(320,320))
pyg.setTitle("test")
imgPath="res/pic.png"
img = pyg.imgload(imgPath)
img2 = pyg.imgload("res/pygame_tiny.png")

pos = [0] * 2 
r = 0

while pyg._running:
	pyg.process(0.016)

	pyg.putImg(img2,(64,64),flip=pyg.FLIP_H,rotate=r,center=True)
	r = (r + 5)%360
	
	pyg.putImg(img,(0,0))
	pyg.putImg(img,(0,8),(0,0,8,8))
	pyg.putImg(img,(4,8),[0,0,8,8],pyg.FLIP_H)

	pyg.putImg(img,(0,16),[8,0,8,8])
	pyg.putImg(img,(8,16),[8,0,8,8],pyg.FLIP_H)
	pyg.putImg(img,(16,16),[8,0,8,8],pyg.FLIP_V)
	pyg.putImg(img,(24,16),[8,0,8,8],pyg.FLIP_BOTH)

	pyg.putImg(img,(0,24),[0,0,8,8],rotate=90)
	pyg.putImg(img,(8,24),[0,0,8,8],rotate=180)
	pyg.putImg(img,(16,24),[0,0,8,8],rotate=270)

	pyg.putImg(img,pyg.get_mousePos(),(0,0,8,8))

	if pyg.isKeyDownCode(27):
		pyg._running = False
	
	if pyg.isKeyDown("a"):
		print("true")
	
	if pyg.isAnyKeyDown():
		print("any")

pyg.quit()
