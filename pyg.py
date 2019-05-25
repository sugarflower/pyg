from pygame import *
from pygame.locals import *
import os, time

FLIP_H = 1
FLIP_V = 2
FLIP_BOTH = 3

def setTitle(title):
	display.set_caption(title)

def begin(real=[128,64],disp=-1):
	global _running, _keys, _keyDownCnt, _size, _event, _mouse
	global mixer, screen, surface, bg,  mode

	_running = True
	_keys = [False] * 128
	_keyDownCnt = 0
	_event = 0
	_mouse = {"pos":[0,0]}

	if disp == -1:
		disp = real
	_size = { "real":real, "display":disp }

	mixer = mixer
	mixer.pre_init( 44100, -16, 2, 1024 )
	mixer.init()
	init()

	mode = HWSURFACE | DOUBLEBUF 
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	screen = display.set_mode(_size["display"], mode)
	surface = Surface(_size["real"], mode | SRCALPHA, 32)

	set_mouseCursorVisible(False)

def process( wait = 0.03 ):
	global _keyDownCnt, _running, _keys, _mouse, _event, screen, surface, bg
	st = time.time()
	_procWait = True
	while _procWait:
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

		if time.time() - st > wait:
			screen.blit(transform.scale(surface,_size["display"]),(0,0))
			display.update()
			surface.fill((0,0,0,0))
			screen.fill((0,0,0))
			_procWait = False

def end():
	quit()

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

