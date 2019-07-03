#!/usr/bin/python3

class Resource:

	def __init__(self,res=""):
		if res !="":
			self._resFile = res
			with open(self._resFile,"rb") as f:
				data = f.read(2)
				self._size = int((data[1] << 8) | data[0])
				head = f.read(self._size)
				self._index = eval(head.decode())

	def get(self,resName):
		_idx,_size = self._index[resName]
		_idx += self._size + 2
		with open(self._resFile,"rb") as f:
			f.seek(_idx)
			data = f.read(_size)
		return data

	def exec(self,resName):
		exec( self.get(resName).decode() )
