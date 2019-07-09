import pyg
import math

class main:

	def faceVect(self,p):
		v1 = (p[1][0] - p[0][0], p[1][1] - p[0][1], p[1][2] - p[0][2])
		v2 = (p[2][0] - p[0][0], p[2][1] - p[0][1], p[2][2] - p[0][2])
		n0 = v1[1] * v2[2] - v1[2] * v2[1]
		n1 = v1[2] * v2[0] - v1[0] * v2[2]
		n2 = v1[0] * v2[1] - v1[1] * v2[0]
		ln = math.sqrt(n0**2 + n1**2 + n2**2)
		if ln != 0:
			n0 = n0 / ln
			n1 = n1 / ln
			n2 = n2 / ln
		return (n0,n1,n2)

	def cl(self,p):
		a = (p[1][0] - p[0][0]) * (p[2][1] - p[0][1])
		b = (p[1][1] - p[0][1]) * (p[2][0] - p[0][0])
		return a > b

	def rotate(self, points, rx, ry, rz):
		b = math.radians(ry)
		a = math.radians(rx)
		g = math.radians(rz)
		p2 = [0]*len(points)
		lc = int(len(points)/3)
		for i in range(lc):
			idx = i * 3
			x0 = points[idx]
			y0 = points[idx+1]
			z0 = points[idx+2]
			x1 = x0 * math.cos(b) + z0 * math.sin(b)
			z1 =-x0 * math.sin(b) + z0 * math.cos(b)
			y2 = y0 * math.cos(a) - z1 * math.sin(a)
			z2 = y0 * math.sin(a) + z1 * math.cos(a)
			x3 = x1 * math.cos(g) - y2 * math.sin(g)
			y3 = x1 * math.sin(g) + y2 * math.cos(g)
			p2[idx] = x3
			p2[idx+1] = y3
			p2[idx+2] = z2
		return p2

	def trans(self, points, rx, ry, rz):
		p2 = [[0,0,0]] * 3
		c = 0	
		for p in points:
			x = p[0] / ( 10 + p[2] ) * 500
			y = p[1] / ( 10 + p[2] ) * 500
			z = p[2]
			p2[c] = (x+160,y+160,z)
			c += 1
		return p2

	def light(self,vec):
		light = (0,0,-1) 
		a = vec[0] * light[0]
		b = vec[1] * light[1]
		c = vec[2] * light[2]
		return abs(a+b+c)

	def getTri(self, data, link):
		idx = link[0] * 3
		a = (data[idx],data[idx+1],data[idx+2])
		idx = link[1] * 3
		b = (data[idx],data[idx+1],data[idx+2])
		idx = link[2] * 3
		c = (data[idx],data[idx+1],data[idx+2])
		return (a,b,c)

	def setup(self):
		pyg.setSize((320,320))
		pyg.setTitle("polygon")
		self.rx = 0
		self.ry = 0
		self.rz = 0
		self.p = (-1,1,1, 1,1,1, 1,-1,1, -1,-1,1, -1,1,-1, 1,1,-1, 1,-1,-1, -1,-1,-1)
		self.link = (
			(0,1,2),(0,2,3), (1,5,6),(1,6,2),
			(5,4,7),(5,7,6), (4,0,3),(4,3,7),
			(4,1,0),(4,5,1), (3,2,6),(3,6,7))

	def loop(self):
		pyg.clear()

		p1 = self.rotate(self.p, self.rx, self.ry, self.rz)
		for l in self.link:
			t = self.getTri(p1,l)
			v = self.faceVect(t)
			p2=self.trans(t,self.rx,self.ry,self.rz)
			if self.cl(p2):
				lv = self.light(v)
				cl = math.floor(64 * lv + 190)
				color = pyg.Color(cl,cl,cl)
				pyg.getGfx().filled_polygon(pyg.getSurface(), p2, color)

		if pyg.isKeyDownCode(273):
			self.rx = (self.rx - 5) % 360
		if pyg.isKeyDownCode(274):
			self.rx = (self.rx + 5) % 360
		if pyg.isKeyDownCode(275):
			self.ry = (self.ry - 5) % 360
		if pyg.isKeyDownCode(276):
			self.ry = (self.ry + 5) % 360

m = main()
pyg.run(m)
