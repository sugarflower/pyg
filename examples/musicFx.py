#!/usr/bin/python3
import pyg

pyg.begin((80,80),(300,300))
pyg.setTitle("music and Fx")


"""
load music and play infinity
"""
pyg.mixer.music.load("res/music.xm")
pyg.mixer.music.play(-1)

"""
load fx sound
"""
fx = pyg.mixer.Sound("res/a.wav")


kd = False

f = pyg.TinyFont()
f.print("HIT'A'KEY: PLAYFX",(6,36))

while pyg._running:
	pyg.process()

	"""
	press a key, play fx
	"""
	if pyg.isKeyDown("a") & (kd==False):
		fx.play()
		kd = True
	elif (pyg.isKeyDown("a") == False) & kd:
		kd = False

pyg.quit()
