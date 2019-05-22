import pygame
from pygame.locals import *
import os, time

FLIP_H = 1
FLIP_V = 2
FLIP_BOTH = 3
R90  = 90 
R180 = 180
R270 = 270


def setTitle(title):
	pygame.display.set_caption(title)

def init(real=[128,64],disp=-1):
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

	mixer = pygame.mixer
	mixer.pre_init( 44100, -16, 2, 1024 )
	mixer.init()
	pygame.init()

	mode = pygame.HWSURFACE | pygame.DOUBLEBUF 
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	screen = pygame.display.set_mode(_size["display"], mode)
	surface = pygame.Surface(_size["real"], mode | pygame.SRCALPHA, 32)

	set_mouseCursorVisible(False)

def process( wait = 0.03 ):
	global _keyDownCnt, _running, _keys, _mouse, _event, screen, surface, bg
	st = time.time()
	_procWait = True
	while _procWait:
		for event in pygame.event.get():
			_event = event 
			if event.type == pygame.QUIT:
				_running = False

			if event.type == pygame.KEYDOWN:
				key = event.key
				if key < 128:
					if _keys[key] == False:
						_keyDownCnt += 1
						_keys[key] = True

			if event.type == pygame.KEYUP:
				key = event.key
				if key < 128:
					if _keys[key]:
						_keyDownCnt -= 1
						_keys[key] = False

			if event.type == pygame.MOUSEMOTION:
				_mouse["pos"] = (event.pos[0],event.pos[1])

		if time.time() - st > wait:
			screen.blit(pygame.transform.scale(surface,_size["display"]),(0,0))
			pygame.display.update()
			surface.fill((0,0,0,0))
			screen.fill((0,0,0))
			_procWait = False

def quit():
	pygame.quit()

def imgload(path):
	return pygame.image.load(path).convert_alpha()

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
	pygame.mouse.set_visible(value)

def get_mousePos():
	global _size, _mouse
	wa = _size["real"][0] / _size["display"][0]
	ha = _size["real"][1] / _size["display"][1]
	return _mouse["pos"][0] * wa , _mouse["pos"][1] * ha

def createImg(size):
	return pygame.Surface(size, mode | pygame.SRCALPHA, 32)

def putImg(img,pos, rect=-1 ,flip=-1, rotate=0, center=False, surf=-1):
	global surface,mode
	if surf == -1:
		surf = surface
	if rect == -1:
		r = (img.get_width(),img.get_height())
		surTemp = pygame.Surface(r,mode | pygame.SRCALPHA, 32)
		surTemp.blit(img,(0,0))
	else:
		r = (rect[2],rect[3])
		surTemp = pygame.Surface(r,mode | pygame.SRCALPHA, 32)
		surTemp.blit(img,(0,0),rect)

	if flip == FLIP_H:
		surTemp=pygame.transform.flip(surTemp,True,False)

	if flip == FLIP_V:
		surTemp=pygame.transform.flip(surTemp,False,True)
		
	if flip == FLIP_BOTH:
		surTemp=pygame.transform.flip(surTemp,True,True)
	
	if rotate != 0:
		rotate = rotate % 360
		st2 = pygame.transform.rotate(surTemp,rotate)
		w = surTemp.get_width()
		h = surTemp.get_height()
		dw = int((w - st2.get_width()) /2)
		dh = int((h - st2.get_height())/2)
		if center:
			surf.blit(st2,(pos[0]+dw-(w/2),pos[1]+dh-(h/2)))
		else:
			surf.blit(st2,(pos[0]+dw,pos[1]+dh))	
		del st2
	else:	
		surf.blit(surTemp,pos)
	
	del surTemp

