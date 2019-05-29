#!/usr/bin/python3

import pyg
import math


def rot2d(pos, r):
	x = pos[0]
	y = pos[1]
	xd = x * math.cos(math.radians(r)) - y * math.sin(math.radians(r))
	yd = -x * math.sin(math.radians(r)) + y * math.cos(math.radians(r))
	return (round(xd), round(yd))

pyg.begin((128,128),(128*3,128*3))
txt = pyg.TinyFont()
r = 0

while pyg._running:
	pyg.process()
	pyg.clear()

	p = rot2d( (0, 100), r)
	r = (r + 1) % 360

	pyg.gfx.line(pyg.surface, 0,64, 128,64, pyg.Color(0,50,0))
	pyg.gfx.line(pyg.surface, 64,0, 64,128, pyg.Color(0,50,0))
	pyg.gfx.line(pyg.surface, 64, 64, 64+p[0], 64+p[1], pyg.Color(100,255,255))
	txt.print("X :" + str(p[0]), (0,0))
	txt.print("Y :" + str(p[1]), (0,6))

	rd = math.atan2(-p[0],p[1])
	txt.print("DEGREE:" + str(rd*180/math.pi+180),(0,12))
pyg.quit()
