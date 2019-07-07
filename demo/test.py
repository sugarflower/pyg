#!/usr/bin/python3
import pyg as p
import pyg.font8x8 as font
import random

class main:

	def setup(self):
		p.setSize((160,160),(320,320))
		p.setTitle("PYG2 Test")	
		
		self.img = p.loadImage("res/pic.png")
		
		f = font.Font(p)
		f.setPos(0,0)
		msg = "Shake!"
		self.fontImg = p.createImage(len(msg)*8, 8)
		f.printStr(msg,surf=self.fontImg)

	def loop(self):
		p.clear()
		p.fill(p.Color(100,0,0))
		p.putImage(self.fontImg,(80,80),center=True)
		p.putImage(self.img,(50,50))
		p.putImage(self.img,(0,0))
		p.setOffset((random.randint(0,10)-5,random.randint(0,10)-5))

		"""
		e = p.getEvent()
		if e != None:
			print(e)
			if e.type == 6:
				print(e.button)
		"""

main = main()
p.run(main)
