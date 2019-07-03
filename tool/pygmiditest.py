#!/usr/bin/python3
import pyg
import pygmidi
import time

pyg.begin((200,200))

m = pygmidi.midiObj()
m2 = pygmidi.midiObj()

print( m.midiDevices() )
midiout = m.openByName("NSX-39 MIDI 1", "OUTPUT")
midiin  = m2.openByName("NSX-39 MIDI 1", "INPUT")

while pyg._running:
    pyg.process()
    
    data = m2.event()
    if data != 0:
        for d in data:
            channel = d[0] & 0x0f
            if (d[0] & 0xf0) == 0x90:
                print("note on")
                print("Channel:",channel)
                print("Note No:", d[1])
                print("Velocity:", d[2])
            if (d[0] & 0xf0) == 0x80:
                print("note off")

"""
midiout.note_on(60,100,1)
time.sleep(2)
midiout.note_off(60,0,1)
"""
m.quit()
pyg.quit()
