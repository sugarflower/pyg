#!/usr/bin/python3
from PIL import Image
import argparse

p = argparse.ArgumentParser()
p.add_argument("inputFilePath")
p.add_argument("outputFilePath")
args = p.parse_args()

inputFileName = args.inputFilePath
outputFileName = args.outputFilePath

img = Image.open(inputFileName)
print( "size: " , img.size )
print( "mode: " , img.mode )

if img.mode == "RGBA":
	f = open(outputFileName,"wb")
	for y in range( img.height ):
		for x in range( img.width ):
			pix = img.getpixel((x,y))
			f.write(bytes([pix[0],pix[1],pix[2],pix[3]]))
	f.close()
else:
	print("Currently only RGBA format suppoted")

print("done")
