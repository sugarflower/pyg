#!/usr/bin/python3
import pyg
import argparse

p = argparse.ArgumentParser()
p.add_argument("inputFile")
p.add_argument("outputFile")
args = p.parse_args()

fileName = args.inputFile
outFileName = args.outputFile

pyg.begin((128,128),(256,256))
f = pyg.TinyFont()
f.print("load img:" + fileName,(0,0))
pyg.update()

img = pyg.imgLoad(fileName)
pyg.putImg(img,(0,6))
pyg.update()

f.print("WIDTH   : " + str(img.get_width()),(0,6))
f.print("HEIGHT  : " + str(img.get_height()),(0,12))
pyg.update()

buf = img.get_buffer()
rawData = buf.raw

f.print("dataSize: " + str(len(rawData)),(0,18))

fp = open(outFileName,"w")
fp.write("data=bytes([\n\t")
lineCount = 0
for d in rawData:
	fp.write( hex(d) + "," )
	lineCount += 1
	if lineCount == 8:
		lineCount = 0
		fp.write("\n\t")

fp.write("])\n")
fp.close()

f.setColor((255,0,0))
f.print("..Done",(0,24))

while pyg._running:
	pyg.process()

pyg.quit()

