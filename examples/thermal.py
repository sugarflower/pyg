#!/usr/bin/python3
import pyg
import subprocess

pyg.begin((320,200))

myFont = pyg.font.Font(None,30)
img1 = pyg.imgLoad("res/bluedot.png")
img2 = pyg.imgLoad("res/glaydot.png")
thermal = "cat /sys/class/thermal/thermal_zone0/temp"

blk = True

while pyg._running:
  pyg.process(0.2)
  pyg.clear()

  vTemp = subprocess.check_output(thermal, shell=True)
  vTemp = int(vTemp) / 1000.0
  tempText = myFont.render("Temp: " + str(vTemp),1,(255,255,255))

  if blk:
    pyg.putImg(img1,(14,83) )
    blk = False
  else:
    pyg.putImg(img2,(14,83) )
    blk = True

  pyg.putImg( tempText, (48,89) )

pyg.quit()
