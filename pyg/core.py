from pygame import *
from pygame.locals import *
import pygame.gfxdraw as gfx
import time, os

FLIP_H = 1
FLIP_V = 2
FLIP_BOTH = 3

_running = True
_keys = [False] * 512
_keyDownCnt = 0
_mouse = {"pos":[0,0], "button":[False]*3, "click":[False]*3 }
_size = {"real":[128,128],"disp":[384,384],"margin":[20,20]}
_screen = {"offset":[0,0]}
_waitTime = 0.016
_mode = SWSURFACE #HWSURFACE | DOUBLEBUF
_fullscreen = False
screen = None
surface = None
Event = None

def setSize( real, disp=None, margin=None ):
	_size["real"] = real
	if disp != None:
		_size["disp"] = disp
	else:
		_size["disp"] = real
	if margin != None:
		_size["margin"] = margin

def dispMouseCursor(val):
	mouse.set_visible(val)

def setTitle(val):
	display.set_caption(val)

def setWaitTime(val=0.016):
	global _waitTime
	_waitTime = val

def setOffset(offset):
	global _screen
	_screen["offset"] = offset

def isKeyDown(key):
	return _keys[ord(key)]

def isKeySownCode(key):
	return _keys[key]

def isAnyKeyDown():
	return _keyDownCnt != 0

def getMousePos():
	wa = _size["real"][0] / _size["disp"][0]
	ha = _size["real"][1] / _size["disp"][1]
	mx = _mouse["pos"][0] - _size["margin"][0]
	my = _mouse["pos"][1] - _size["margin"][1]
	return ( int(mx * wa), int(my * ha) )

def isClick(button=0):
	return _mouse["click"][button]

def isPress(button=0):
	return _mouse["button"][button]

def clear():
	fill((0,0,0,0),surface)
	fill((0,0,0),screen)

def fill( color=(0,0,0,0), surf=None ):
	if surf == None:
		surf = surface
	surf.fill(color)

def loadImage(path):
	return image.load(path).convert_alpha()

def createImage(size):
	return Surface(size, _mode | SRCALPHA, 32)

def getEvent():
	return Event

def getSurface():
	return surface

def getGfx():
	return gfx

def putImage(img, pos, rect=None, flip=None, rotate=None, surf=None, scale=None, center=False):
	if surf == None:
		surf = surface

	if rect == None:
		imgrect = ( img.get_width(), img.get_height())
	else:
		imgrect = (rect[2], rect[3])
	surfTemp = Surface( imgrect, _mode | SRCALPHA, 32 )
	surfTemp.blit(img,(0,0))

	if flip != None:
		if flip == FLIP_H:
			surfTemp = transform.flip(surfTemp, True, False)
		elif filp == FLIP_V:
			surfTemp = transform.flip(surfTemp, False,True)
		elif flip == FLIP_BOTH:
			surfTemp = transform.flip(surfTemp, True,True)
	
	if rotate != None:
		rotate = (360 - rotate) % 360
		st2 = transform.rotate(surfTemp, rotate)
		w = surfTemp.get_width()
		h = surfTemp.get_height()
		dw = int((w - st2.get_width()))>>1
		dh = int((h - st2.get_height()))>>1
	else:
		st2 = surfTemp
		dw = 0
		dh = 0 
		w = surfTemp.get_width()
		h = surfTemp.get_height()
	
	if scale != None:
		sc = (int(st2.get_width()*scale[0]), int(st2.get_height()*scale[1]))
		if (scale[0]>1) | (scale[1]>1):
			st3 = transform.scale(st2, sc)
		else:
			st3 = transform.smoothscale(st2, sc)
	else:
		st3 = st2

	if center:
		surf.blit(st3,(pos[0]+dw-(w>>1), pos[1]+dh-(h>>1)))
	else:
		surf.blit(st3,(pos[0]+dw, pos[1]+dh))
		
def _init():
	mixer.pre_init( 44100, -16, 2, 1024 )
	mixer.init()
	init()
	os.environ["SDL_VIDEO_CENTERED"] = "1"

def _setupDisplay(fullscreen=False):
	global screen, surface
	dispW = _size["disp"][0] + (_size["margin"][0] * 2)
	dispH = _size["disp"][1] + (_size["margin"][1] * 2)
	screen  = display.set_mode( (dispW, dispH), _mode)
	surface = Surface(_size["real"], _mode | SRCALPHA , 32 )
	if fullscreen:
		display.toggle_fullscreen()
	dispMouseCursor(False)

def _update():
	us = Surface(_size["real"], _mode | SRCALPHA, 32)
	us.blit(surface, _screen["offset"] )
	screen.blit(transform.scale(us, _size["disp"]) , _size["margin"])
	display.update()

def _process():
	global _running, _mouse, _keys, _keyDownCnt, Event, _fullscreen
	st = time.time()
	_procWait = True
	_mouse["click"] = [False] * 3
	Event = None
	while _procWait:
		time.sleep(0.001)
		for e in event.get():
			Event = e
			_key = -1

			if e.type == QUIT:
				_running = False

			if e.type == KEYDOWN:
				_key = e.key
				if _key < 512:
					if _keys[_key] == False:
						_keyDownCnt += 1
						_keys[_key] = True

			if e.type == KEYUP:
				_key = e.key
				if _key < 512:
					if _keys[_key]:
						_keyDownCnt -= 1
						_keys[_key] = False
				if _key == 292:
					if _fullscreen:
						_fullscreen = False
						_setupDisplay()
					else:
						_fullscreen = True
						_setupDisplay(True)
				if _key == 27:
					_running = False

			if e.type == MOUSEMOTION:
				_mouse["pos"] = (e.pos[0], e.pos[1])

			if e.type == MOUSEBUTTONDOWN:
				_mouse["button"] = mouse.get_pressed()

			if e.type == MOUSEBUTTONUP:
				for i in range(3):
					if _mouse["button"][i]:
						_mouse["click"][i] = True
					_mouse["button"] = [False] * 3

		if time.time() - st > _waitTime:
			_update()
			_procWait = False

def run(main):
	d = set(dir(main))

	if len(d & {"setup"} ) == 1:
		main.setup()

	_setupDisplay()

	if len(d & {"loop"} ) == 1:
		while _running:
			main.loop()
			_process()

	quit()

_init()
_setupDisplay()

