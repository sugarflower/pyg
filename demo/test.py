#!/usr/bin/python3
import pyg
import pyg.font8x8 as font
import random

class main:

	def setup(self):
		pyg.setSize((160,160),(320,320))
		pyg.setTitle("PYG2 Test")	
		
		self.img = pyg.loadImage("res/pic.png")
		
		f = font.Font(pyg)
		self.img_shake = pyg.createImage(48, 8)
		f.printStr("Shake!",surf=self.img_shake, pos=(0,0))

		self.img_flip = pyg.createImage(32,8)
		f.printStr("Flip",surf=self.img_flip, pos=(0,0))

		self.img_rot = pyg.createImage(48,8)
		f.printStr("Rotate",surf=self.img_rot, pos=(0,0))

		self.img_msg = pyg.createImage(160,24)
		f.printStr("Let'sTry MouseMotion", surf=self.img_msg, pos=(0,0))
		f.printStr("[F11] ToggleFullScr.", surf=self.img_msg, pos=(0,8))
		f.printStr("[ESC] Quit App.", surf=self.img_msg, pos=(0,16))

		self.sp = {
			"player":(0,0,8,8),
			"tomato":(8,0,8,8),
			"block":(16,0,8,8),
			}

	def loop(self):
		pyg.clear()
		pyg.fill(pyg.Color(100,0,0))
		

		pyg.putImage(self.img,(0,0))

		pyg.putImage(self.img_flip,(0,16))
		pyg.putImage(self.img, (0,24),  self.sp["tomato"])
		pyg.putImage(self.img, (8,24),  self.sp["tomato"], flip=pyg.FLIP_H)
		pyg.putImage(self.img, (16,24), self.sp["tomato"], flip=pyg.FLIP_V)
		pyg.putImage(self.img, (24,24), self.sp["tomato"], flip=pyg.FLIP_BOTH)

		pyg.putImage(self.img_rot, (0,40))
		pyg.putImage(self.img, (0,48), self.sp["player"], rotate=90)
		pyg.putImage(self.img, (8,48), self.sp["player"], rotate=180)
		pyg.putImage(self.img, (16,48),self.sp["player"], rotate=270)

		pyg.putImage(self.img, pyg.getMousePos(), self.sp["player"])
		
		if pyg.isPress():
			pyg.setOffset((random.randint(0,10)-5,random.randint(0,10)-5))
			pyg.putImage(self.img_shake,(80,80),center=True)
		else:
			pyg.setOffset((0,0))
			

		pyg.putImage(self.img_msg, (0,120))

		"""
		e = p.getEvent()
		if e != None:
			print(e)
			if e.type == 6:
				print(e.button)
		"""

main = main()
pyg.run(main)
