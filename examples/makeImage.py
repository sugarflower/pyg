#!/usr/bin/python3
import pyg

pyg.init((5,3),(300,300))
pyg.setTitle("Make Image")

# G B A R 
b = bytes([
	0x00, 0x00, 0xff, 0xFF,
	0xff, 0x00, 0xff, 0x00,
	0x00, 0xff, 0xff, 0x00,
])
img = pyg.pygame.image.frombuffer(b,(3,1),"ARGB" )

while pyg._running:
	pyg.process()
	
	pyg.putImg(img,(1,1))

