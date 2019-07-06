#!/usr/bin/python3
import pyg, pyg.font8x8, math
from operator import itemgetter


class main:

	def setup(self):
		pyg.setSize((256,128),(512,256))
		pyg.setTitle("3D Demo")
		self.ball = pyg.loadImage("res/ball.png")
		font = pyg.font8x8.Font(pyg)

		msg = "Welcome to pyg!"
		msg2 ="pyg is an easy-to-use solution"
		msg3 ="for PyGame."
		self.msgImg = pyg.createImage((len(msg2)*8,25))
		font.setPos(1,1)
		font.setColor(pyg.Color(0,0,0))
		font.printStr(msg,surf=self.msgImg)
		font.setPos(1,9)
		font.printStr(msg2,surf=self.msgImg)
		font.setPos(1,17)
		font.printStr(msg3,surf=self.msgImg)

		font.setPos(0,0)
		font.setColor(pyg.Color(255,255,255))
		font.printStr(msg,surf=self.msgImg)
		font.setPos(0,8)
		font.printStr(msg2,surf=self.msgImg)
		font.setPos(0,16)
		font.printStr(msg3,surf=self.msgImg)

		self.ra = 0
		self.rb = 0
		
		self.b=[[0,0,0]]*5*5*5
		for z in range(5):
			for y in range(5):
				for x in range(5):
					self.b[z*25+y*5+x] = [(x-2)*2,(y-2)*2,(z-2)*2]


	def rot(self, w, h, r):
		dw = w * math.cos(math.radians(r)) - h * math.sin(math.radians(r))
		dh = w * math.sin(math.radians(r)) + h * math.cos(math.radians(r)) 
		return dw,dh

	def loop(self):
		pyg.clear()
		bb = [[0,0,0]]*5*5*5
		for z in range(5):
			for y in range(5):
				for x in range(5):
					p = self.b[z*25+y*5+x]
					px,py,pz = p[0],p[1],p[2]
					xx,yy = self.rot(px,py,self.ra) #z
					xx,zz = self.rot(xx,pz,self.rb) #y
					zz = zz + 20 
					xx = int(xx * zz/3 ) + 128
					yy = int(yy * zz/3 ) + 64

					bb[z*25+y*5+x] = [xx,yy,zz]

		bb = sorted(bb, key=itemgetter(2) )			

		for i in range(125):
			p = bb[i]
			zv = p[2] / 15 
			pyg.putImage(self.ball,(p[0],p[1]), scale=(zv,zv), center=True)

		self.ra = (self.ra + 4)%360
		self.rb = (self.rb + 0.5)%360

		pyg.putImage(self.msgImg,(128,64),center=True)

main = main()
pyg.run(main)

