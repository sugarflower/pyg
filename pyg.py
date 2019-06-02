from pygame import *
from pygame.locals import *
import pygame.gfxdraw as gfx 
import os, time, math

FLIP_H = 1
FLIP_V = 2
FLIP_BOTH = 3

def setTitle(title):
	display.set_caption(title)

def begin(real=[128,128], disp=-1, margin=(30,30)):
	global _running, _keys, _keyDownCnt, _size, _event, _mouse, _mouseButton
	global _margin
	global mixer, screen, surface, bg,  mode

	_running = True
	_keys = [False] * 128
	_keyDownCnt = 0
	_event = 0
	_mouse = {"pos":[0,0]}
	_mouseButton = [False] * 3
	_click = [False] * 3
	_margin = margin

	if disp == -1:
		disp = real
	_size = { "real":real, "display":disp }

	mixer = mixer
	mixer.pre_init( 44100, -16, 2, 1024 )
	mixer.init()
	init()

	mode = HWSURFACE #| DOUBLEBUF 
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	screen = display.set_mode((_size["display"][0]+_margin[0]*2,_size["display"][1]+_margin[1]*2),mode)
	surface = Surface(_size["real"], mode | SRCALPHA, 32)

	set_mouseCursorVisible(False)

def process( wait = 0.016 ):
	global _keyDownCnt, _running, _keys, _mouse, _event, screen
	global _margin, surface, bg, _mouseButton, _click
	st = time.time()
	_procWait = True
	_click = [False] * 3
	while _procWait:
		time.sleep(0.01)
		for e in event.get():
			_event = e 
			if e.type == QUIT:
				_running = False

			if e.type == KEYDOWN:
				key = e.key
				if key < 128:
					if _keys[key] == False:
						_keyDownCnt += 1
						_keys[key] = True

			if e.type == KEYUP:
				key = e.key
				if key < 128:
					if _keys[key]:
						_keyDownCnt -= 1
						_keys[key] = False

			if e.type == MOUSEMOTION:
				_mouse["pos"] = (e.pos[0],e.pos[1])

			if e.type == MOUSEBUTTONDOWN:
				_mouseButton = mouse.get_pressed()

			if e.type == MOUSEBUTTONUP:
				for i in range(3):
					if _mouseButton[i]:
						_click[i] = True
				_mouseButton = [False] * 3

		if time.time() - st > wait:
			update()
			_procWait = False

def update():
	global screen, surface,_size,_margin
	screen.blit(transform.scale(surface,_size["display"]),_margin)
	display.update()

def imgLoad(path):
	return image.load(path).convert_alpha()

def isKeyDown(key):
	global _keys
	return _keys[ord(key)]

def isKeyDownCode(key):
	global _keys
	return _keys[key]

def isAnyKeyDown():
	global _keyDownCnt
	return _keyDownCnt != 0

def set_mouseCursorVisible(value):
	mouse.set_visible(value)

def get_mousePos():
	global _size, _mouse
	wa = _size["real"][0] / _size["display"][0]
	ha = _size["real"][1] / _size["display"][1]
	return _mouse["pos"][0] * wa , _mouse["pos"][1] * ha

def isClick(button=0):
	global _click
	return _click[button]

def isPress(button=0):
	global _mouseButton
	return _mouseButton[button]

def createImg(size):
	return Surface(size, mode | SRCALPHA, 32)

def putImg(img,pos, rect=-1 ,flip=-1, rotate=0, center=False, surf=-1):
	global surface,mode
	if surf == -1:
		surf = surface
	if rect == -1:
		r = (img.get_width(),img.get_height())
		surTemp = Surface(r,mode | SRCALPHA, 32)
		surTemp.blit(img,(0,0))
	else:
		r = (rect[2],rect[3])
		surTemp = Surface(r,mode | SRCALPHA, 32)
		surTemp.blit(img,(0,0),rect)

	if flip == FLIP_H:
		surTemp=transform.flip(surTemp,True,False)

	if flip == FLIP_V:
		surTemp=transform.flip(surTemp,False,True)
		
	if flip == FLIP_BOTH:
		surTemp=transform.flip(surTemp,True,True)
	
	rotate = (360 - rotate) % 360
	st2 = transform.rotate(surTemp,rotate)
	w = surTemp.get_width()
	h = surTemp.get_height()
	dw = int((w - st2.get_width()) /2)
	dh = int((h - st2.get_height())/2)
	if center:
		surf.blit(st2,(pos[0]+dw-(w/2), pos[1]+dh-(h/2)))
	else:
		surf.blit(st2,(pos[0]+dw, pos[1]+dh))	
	del st2
	del surTemp

def clear():
	global screen, surface
	fill((0,0,0,0),surface)
	fill((0,0,0),screen)

def fill( color=(0,0,0,0) , surf=-1 ):
	global surface
	if surf==-1:
		surf = surface
	surf.fill((color))


class TinyFont:
	def __init__(self):
		import res.font
		import sys
		self.font = image.frombuffer(res.font.data,(128,24),"RGBA")
		self.currentColor = Color(0,0,0,0xff)
		self.setColor( Color(0xff,0xff,0xff) )
		self.pos = [0, 0]
		sys.modules.pop("res.font")
		del res.font.data

	def setColor( self, color ):
		pix = PixelArray(self.font)
		pix.replace( self.currentColor, color )
		self.currentColor = color
		del pix

	def putChr( self, asc, surf ):
		y = ( math.floor(asc/32) ) * 6
		x = ( asc % 32 ) * 4 
		putImg( self.font, self.pos , (x,y,4,6), surf )
		self.pos[0] += 4

	def print( self, stringVar, pos, surf=-1 ):
		global surface
		if surf==-1:
			surf = surface
		self.pos[0] = pos[0]
		self.pos[1] = pos[1]
		for i in range( len(stringVar) ):
			self.putChr( ord(stringVar[i:i+1]), surf )

