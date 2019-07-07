#!/usr/bin/python3
import pyg
import pyg.font8x8

class main:
	def setup(self):
		pyg.setSize((128,128),(256,256))
		pyg.setTitle("hello world")
		self.img = pyg.createImage(88,8)
		font = pyg.font8x8.Font(pyg)
		font.printStr("Hello World", surf=self.img)
		self.r = 0

	def loop(self):
		pyg.clear()
		pyg.putImage(self.img, (64,64), center=True, rotate=self.r)
		self.r = (self.r + 1) % 360

if __name__ == "__main__":
	m = main()
	pyg.run(m)
