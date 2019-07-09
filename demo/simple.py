#!/usr/bin/python3
import pyg

class main:
	def setup(self):
		pyg.setSize((128,128))
		pyg.setTitle("Simple")

	def loop(self):
		pass

if __name__ == "__main__":
	m = main()
	pyg.run(m)
