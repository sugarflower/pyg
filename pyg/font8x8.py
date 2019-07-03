#!/usr/bin/python3
import inspect

font8x8_basic = (
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x18, 0x3C, 0x3C, 0x18, 0x18, 0x00, 0x18, 0x00),   
	( 0x36, 0x36, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x36, 0x36, 0x7F, 0x36, 0x7F, 0x36, 0x36, 0x00),   
	( 0x0C, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x0C, 0x00),   
	( 0x00, 0x63, 0x33, 0x18, 0x0C, 0x66, 0x63, 0x00),   
	( 0x1C, 0x36, 0x1C, 0x6E, 0x3B, 0x33, 0x6E, 0x00),   
	( 0x06, 0x06, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x18, 0x0C, 0x06, 0x06, 0x06, 0x0C, 0x18, 0x00),   
	( 0x06, 0x0C, 0x18, 0x18, 0x18, 0x0C, 0x06, 0x00),   
	( 0x00, 0x66, 0x3C, 0xFF, 0x3C, 0x66, 0x00, 0x00),   
	( 0x00, 0x0C, 0x0C, 0x3F, 0x0C, 0x0C, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x06),   
	( 0x00, 0x00, 0x00, 0x3F, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x0C, 0x0C, 0x00),   
	( 0x60, 0x30, 0x18, 0x0C, 0x06, 0x03, 0x01, 0x00),   
	( 0x3E, 0x63, 0x73, 0x7B, 0x6F, 0x67, 0x3E, 0x00),   
	( 0x0C, 0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x3F, 0x00),   
	( 0x1E, 0x33, 0x30, 0x1C, 0x06, 0x33, 0x3F, 0x00),   
	( 0x1E, 0x33, 0x30, 0x1C, 0x30, 0x33, 0x1E, 0x00),   
	( 0x38, 0x3C, 0x36, 0x33, 0x7F, 0x30, 0x78, 0x00),   
	( 0x3F, 0x03, 0x1F, 0x30, 0x30, 0x33, 0x1E, 0x00),   
	( 0x1C, 0x06, 0x03, 0x1F, 0x33, 0x33, 0x1E, 0x00),   
	( 0x3F, 0x33, 0x30, 0x18, 0x0C, 0x0C, 0x0C, 0x00),   
	( 0x1E, 0x33, 0x33, 0x1E, 0x33, 0x33, 0x1E, 0x00),   
	( 0x1E, 0x33, 0x33, 0x3E, 0x30, 0x18, 0x0E, 0x00),   
	( 0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x00),   
	( 0x00, 0x0C, 0x0C, 0x00, 0x00, 0x0C, 0x0C, 0x06),   
	( 0x18, 0x0C, 0x06, 0x03, 0x06, 0x0C, 0x18, 0x00),   
	( 0x00, 0x00, 0x3F, 0x00, 0x00, 0x3F, 0x00, 0x00),   
	( 0x06, 0x0C, 0x18, 0x30, 0x18, 0x0C, 0x06, 0x00),   
	( 0x1E, 0x33, 0x30, 0x18, 0x0C, 0x00, 0x0C, 0x00),   
	( 0x3E, 0x63, 0x7B, 0x7B, 0x7B, 0x03, 0x1E, 0x00),   
	( 0x0C, 0x1E, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x00),   
	( 0x3F, 0x66, 0x66, 0x3E, 0x66, 0x66, 0x3F, 0x00),   
	( 0x3C, 0x66, 0x03, 0x03, 0x03, 0x66, 0x3C, 0x00),   
	( 0x1F, 0x36, 0x66, 0x66, 0x66, 0x36, 0x1F, 0x00),   
	( 0x7F, 0x46, 0x16, 0x1E, 0x16, 0x46, 0x7F, 0x00),   
	( 0x7F, 0x46, 0x16, 0x1E, 0x16, 0x06, 0x0F, 0x00),   
	( 0x3C, 0x66, 0x03, 0x03, 0x73, 0x66, 0x7C, 0x00),   
	( 0x33, 0x33, 0x33, 0x3F, 0x33, 0x33, 0x33, 0x00),   
	( 0x1E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
	( 0x78, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E, 0x00),   
	( 0x67, 0x66, 0x36, 0x1E, 0x36, 0x66, 0x67, 0x00),   
	( 0x0F, 0x06, 0x06, 0x06, 0x46, 0x66, 0x7F, 0x00),   
	( 0x63, 0x77, 0x7F, 0x7F, 0x6B, 0x63, 0x63, 0x00),   
	( 0x63, 0x67, 0x6F, 0x7B, 0x73, 0x63, 0x63, 0x00),   
	( 0x1C, 0x36, 0x63, 0x63, 0x63, 0x36, 0x1C, 0x00),   
	( 0x3F, 0x66, 0x66, 0x3E, 0x06, 0x06, 0x0F, 0x00),   
	( 0x1E, 0x33, 0x33, 0x33, 0x3B, 0x1E, 0x38, 0x00),   
	( 0x3F, 0x66, 0x66, 0x3E, 0x36, 0x66, 0x67, 0x00),   
	( 0x1E, 0x33, 0x07, 0x0E, 0x38, 0x33, 0x1E, 0x00),   
	( 0x3F, 0x2D, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
	( 0x33, 0x33, 0x33, 0x33, 0x33, 0x33, 0x3F, 0x00),   
	( 0x33, 0x33, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00),   
	( 0x63, 0x63, 0x63, 0x6B, 0x7F, 0x77, 0x63, 0x00),   
	( 0x63, 0x63, 0x36, 0x1C, 0x1C, 0x36, 0x63, 0x00),   
	( 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x0C, 0x1E, 0x00),   
	( 0x7F, 0x63, 0x31, 0x18, 0x4C, 0x66, 0x7F, 0x00),   
	( 0x1E, 0x06, 0x06, 0x06, 0x06, 0x06, 0x1E, 0x00),   
	( 0x03, 0x06, 0x0C, 0x18, 0x30, 0x60, 0x40, 0x00),   
	( 0x1E, 0x18, 0x18, 0x18, 0x18, 0x18, 0x1E, 0x00),   
	( 0x08, 0x1C, 0x36, 0x63, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFF),   
	( 0x0C, 0x0C, 0x18, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x1E, 0x30, 0x3E, 0x33, 0x6E, 0x00),   
	( 0x07, 0x06, 0x06, 0x3E, 0x66, 0x66, 0x3B, 0x00),   
	( 0x00, 0x00, 0x1E, 0x33, 0x03, 0x33, 0x1E, 0x00),   
	( 0x38, 0x30, 0x30, 0x3e, 0x33, 0x33, 0x6E, 0x00),   
	( 0x00, 0x00, 0x1E, 0x33, 0x3f, 0x03, 0x1E, 0x00),   
	( 0x1C, 0x36, 0x06, 0x0f, 0x06, 0x06, 0x0F, 0x00),   
	( 0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x1F),   
	( 0x07, 0x06, 0x36, 0x6E, 0x66, 0x66, 0x67, 0x00),   
	( 0x0C, 0x00, 0x0E, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
	( 0x30, 0x00, 0x30, 0x30, 0x30, 0x33, 0x33, 0x1E),   
	( 0x07, 0x06, 0x66, 0x36, 0x1E, 0x36, 0x67, 0x00),   
	( 0x0E, 0x0C, 0x0C, 0x0C, 0x0C, 0x0C, 0x1E, 0x00),   
	( 0x00, 0x00, 0x33, 0x7F, 0x7F, 0x6B, 0x63, 0x00),   
	( 0x00, 0x00, 0x1F, 0x33, 0x33, 0x33, 0x33, 0x00),   
	( 0x00, 0x00, 0x1E, 0x33, 0x33, 0x33, 0x1E, 0x00),   
	( 0x00, 0x00, 0x3B, 0x66, 0x66, 0x3E, 0x06, 0x0F),   
	( 0x00, 0x00, 0x6E, 0x33, 0x33, 0x3E, 0x30, 0x78),   
	( 0x00, 0x00, 0x3B, 0x6E, 0x66, 0x06, 0x0F, 0x00),   
	( 0x00, 0x00, 0x3E, 0x03, 0x1E, 0x30, 0x1F, 0x00),   
	( 0x08, 0x0C, 0x3E, 0x0C, 0x0C, 0x2C, 0x18, 0x00),   
	( 0x00, 0x00, 0x33, 0x33, 0x33, 0x33, 0x6E, 0x00),   
	( 0x00, 0x00, 0x33, 0x33, 0x33, 0x1E, 0x0C, 0x00),   
	( 0x00, 0x00, 0x63, 0x6B, 0x7F, 0x7F, 0x36, 0x00),   
	( 0x00, 0x00, 0x63, 0x36, 0x1C, 0x36, 0x63, 0x00),   
	( 0x00, 0x00, 0x33, 0x33, 0x33, 0x3E, 0x30, 0x1F),   
	( 0x00, 0x00, 0x3F, 0x19, 0x0C, 0x26, 0x3F, 0x00),   
	( 0x38, 0x0C, 0x0C, 0x07, 0x0C, 0x0C, 0x38, 0x00),   
	( 0x18, 0x18, 0x18, 0x00, 0x18, 0x18, 0x18, 0x00),   
	( 0x07, 0x0C, 0x0C, 0x38, 0x0C, 0x0C, 0x07, 0x00),   
	( 0x6E, 0x3B, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00),   
	( 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))

_size = { "x":8, "y":8 }
_position=(0,0)
_color = (255,255,255,255)

def _getFontData(asc,color):
	buf = bytearray(256)
	dat = font8x8_basic[asc]
	for j in range(8):
		for i in range(8):
			idx = ((j<<3)+i)<<2
			if (dat[j] >> i) & 1 != 0:
				buf[idx]   = color[1]
				buf[idx+1] = color[2]
				buf[idx+2] = color[3]
				buf[idx+3] = color[0]                               
	return buf

def getParent():
	s=inspect.stack()
	return inspect.getmodule(s[len(s)-2][0])

def setPos(x, y):
	global _position
	_position = (x, y)

def getPos():
	global _position
	return _position

def setColor(color):
	global _color
	_color = color

def getColor():
	global _color
	return _color

def putChr(asc, pos=None, surf=None, _parent=None):
	if _parent == None:
		_parent = getParent()
	buf = _getFontData(asc,getColor())
	if pos == None:
		pos = getPos()
	if surf == None:
		surf = _parent.surface
	img = _parent.image.frombuffer(buf, (_size["x"],_size["y"]), "ARGB")
	_parent.putImage(img, pos, surf=surf)

def printStr(strvar):
	p = getParent()
	b = strvar.encode()
	for s in b:
		putChr(s, _parent=p)
		pos=getPos()
		setPos(pos[0]+_size["x"],pos[1])
