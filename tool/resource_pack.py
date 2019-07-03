#!/usr/bin/python3
import argparse, os

p = argparse.ArgumentParser(description="usage: ./pack_resource.py inDir [-o outFile]")
p.add_argument("inDir", help="asset directory" )
p.add_argument("--outFile","-o", default="out.dat", help="output binary file name")
args = p.parse_args()
assetDir = args.inDir
outFile  = args.outFile
if outFile == "":
	outFile = "out.dat"

d = os.listdir(assetDir)
h = {}
binCount = 0
for i in d:
	if os.path.isfile(assetDir + os.sep + i):
		size = os.stat(assetDir + os.sep + i)[6]
		h[i] = (binCount,size)
		binCount += size

headBin = str(h).encode()
value = len(headBin)
headSize = bytes([ value & 0xff , (value & 0xff00) >> 8 ])

with open(outFile,"wb") as f:
	f.write(headSize)
	f.write(headBin)
	for i in d:
		if os.path.isfile(assetDir + os.sep + i):
			with open(assetDir + os.sep + i,"rb") as f2:
				data = f2.read()
				f.write(data)

