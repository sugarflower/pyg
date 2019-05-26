#!/usr/bin/python3
import pyg
import math

pyg.begin((128,64),(384,192))
pyg.setTitle("bitmapFont Test")

class TinyFont:
	def __init__(self):
		self.font = pyg.imgLoad("res/tom-thumb-original.png")
		self.currentColor = pyg.Color(0,0,0,0xff)
		self.setColor( pyg.Color(0xff,0xff,0xff) )
		self.pos = [0, 0]

	def setColor( self, color ):
		pix = pyg.PixelArray(self.font)
		pix.replace( self.currentColor, color )
		self.currentColor = color
		del pix

	def putChr( self, asc ):
		y = ( math.floor(asc/32) ) * 6
		x = ( asc % 32 ) * 4 
		pyg.putImg( self.font, self.pos , (x,y,4,6) )
		self.pos[0] += 4

	def print( self, stringVar, pos ):
		self.pos[0] = pos[0]
		self.pos[1] = pos[1]
		for i in range( len(stringVar) ):
			self.putChr( ord(stringVar[i:i+1]))

f = TinyFont()

while pyg._running:
	pyg.process()
	f.setColor( pyg.Color(0xff,0xff,0xff))
	f.print("HELLO PYG",(0,0))
	f.setColor( pyg.Color(0,255,0) )
	f.print("ENJOY PyGame with Python :)",(4,6))
	f.setColor( pyg.Color(0,0,255) )
	f.print("ABCDEFGHIJKLMNOPQRSTUVWXYZ",(0,12))
	f.print("abcdefghijklmnopqrstuvwxyz",(0,18))
	f.print("0123456789!!#$%&'()@`[]{}:*;+<>,.?/\_",(0,24))

pyg.end()
