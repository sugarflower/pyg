#!/usr/bin/python3
import pygame.midi as midi

class midiObj:

    def __init__(self):
        midi.init()
        self.midi = midi
        self.devices = []
        for i in range(midi.get_count()):
            self.devices.append(self.decodeInfo(i, midi.get_device_info(i)))

    def quit(self):
        midi.quit()
    
    def decodeInfo(self, devNo, inf):
        if inf[2] == 1:
            direction = "INPUT"
        elif inf[3] == 1:
            direction = "OUTPUT"
        else:
            direction = "???"
        if inf[4] == 1:
            opened = "OPEN"
        else:
            opened = "CLOSE"
        return {"device":devNo,"interface":inf[0].decode(),"name":inf[1].decode(),"direction":direction,"open":opened}

    def midiDevices(self):
        return self.devices

    def openByName(self, name, direction ):
        for dev in self.devices:
            if (dev["name"] == name) & (dev["direction"] == direction):
                if direction == "OUTPUT":
                    self.midiDevice = midi.Output(dev["device"])
                if direction == "INPUT":
                    self.midiDevice = midi.Input(dev["device"])
        return self.midiDevice

    def openById(self, id):
        dev = self.devices[id]
        if dev["direction"] == "OUTPUT":
            self.midiDevice = midi.Output(dev["device"])
        if dev["direction"] == "INPUT":
            self.midiDevice = midi.Input(dev["device"])
        return self.midiDevice    

    def event(self):
        if self.midiDevice.poll():
            data = []
            for me in self.midiDevice.read(512):
                d, ts = me
                data.append(d)
            return data
        else:
            return 0
