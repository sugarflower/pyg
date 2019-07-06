import pyg as p
import pyg.font as font

f = font.Font(p)
p.setSize((200,200),(400,400))
f.setScale(1,1)

def loop():
	f.setPos(0,80)
	f.putChar(33)
	f.putChar(34)
	f.putChar(35)
	f.putChar(36)

p.run()

