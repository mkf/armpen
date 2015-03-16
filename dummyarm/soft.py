# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class soft:
	def __init__(self):
		self.arc = arc
class arc:
	def __init__(self,l,t,azim,x,y,a="deg"):
		import math
		self.l = l
		self.deg = deg = t if a=="deg" else math.degrees(t) if a=="rad" else None
		self.rad = rad = t if a=="rad" else math.radians(t) if a=="deg" else None
		self.pera = pera
		self.perl = perl
		self.r = float(l)/float(rad) if t!=0 else None

	def draw(self):
		pass
class proste(arc):
	def __init__(self,l,taz,x,y):
		arc.__init__(self,l,0,taz,x,y)
		#self.