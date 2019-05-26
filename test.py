#!/usr/bin/python3
import pyg 

"""
pyg.init
set real picture size and display size
"""
pyg.begin( (80,80), (320,320) )
pyg.setTitle("*pyg test*")

"""
get resource and initialize for application
"""
img = pyg.imgLoad("res/pic.png")
pos = [0, 0] 
r = 0

"""
define for sprite sheet
"name" : ( pos x, pos y , width , height )
"""
sp = {
	"player":(0, 0, 8, 8), 
	"tomato":(8, 0, 8, 8),
	"block":(16,0,8,8),
}

"""
Level design Sample
create "bg" and drow it.
"""
map = (
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	0,0,0,0,0,0,0,0,0,0,
	1,0,0,0,0,0,0,0,0,0,
	1,0,0,0,0,0,0,0,0,1,
	1,0,0,0,0,1,0,0,0,1,
	1,0,0,0,0,0,0,1,0,1,
	1,1,1,1,1,1,1,1,1,1,
)

bg = pyg.createImg((80,80))
for y in range(10):
	for x in range(10):
		idx = y*10+x
		if map[idx] == 1:
			pyg.putImg(img, (x*8, y*8), sp["block"],surf=bg)


"""
font
"""
f = pyg.TinyFont()

"""
main loop
"""
while pyg._running:
	pyg.process(0.016)
	pyg.fill((0,0,0,32))

	pyg.putImg(bg, (40,40), rotate=r, center=True ) #draw bg
	r = (r + 2) % 360

	pyg.putImg(img, (0,0))

	pyg.putImg(img, (0,16), sp["tomato"])
	pyg.putImg(img, (8,16), sp["tomato"], flip = pyg.FLIP_H)
	pyg.putImg(img, (16,16),sp["tomato"], flip = pyg.FLIP_V)
	pyg.putImg(img, (24,16),sp["tomato"], flip = pyg.FLIP_BOTH)

	pyg.putImg(img, (0,24), sp["player"], rotate = 90 )
	pyg.putImg(img, (8,24), sp["player"], rotate = 180)
	pyg.putImg(img, (16,24),sp["player"], rotate = 270)

	pyg.putImg(img,pyg.get_mousePos(), sp["player"])

	f.print("PYG TEST",(4,36))
	f.print("by SUGARFLOWER",(20,42))


	if pyg.isKeyDownCode(27): #ESC key
		pyg._running = False
	
	if pyg.isKeyDown("a"):
		print("true")
	
	if pyg.isAnyKeyDown():
		print("any")

	if pyg.isClick():
		print("click")
	if pyg.isClick(1):
		print("click 1")
	if pyg.isClick(2):
		print("click 2")

	if pyg.isPress():
		print("press")
	if pyg.isPress(1):
		print("press 1")
	if pyg.isPress(2):
		print("press 2")
"""
end app
"""
pyg.quit()

