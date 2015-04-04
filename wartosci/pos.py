# -*- coding: utf-8 -*-
class pos:
	def __init__(self,coordict):
		if 'x' in coordict and 'y' in coordict: self.x = coordict['x'] ; self.y=coordict['y'] ; self.typ='k'
		if ('phi' in coordict or 'theta' in coordict) and 'r' in coordict:
			self.phival = coordict['phi'] if 'phi' in coordict else coordict['theta'] if 'theta' in coordict else None
			self.rval=coordict['r'] ; self.typ='p'
	def __dict__(self):
		di = {}
		if self.phival is not None: di.update({'phi':self.phival})
		if self.rval is not None: di.update({'r':self.rval})
		if self.x is not None: di.update({'x':self.x})
		if self.y is not None: di.update({'y':self.y})
		return di
	def __getitem__(self, item):
		if item in self.__dict__: return self.__dict__[item]
		else: raise IndexError
	@property
	def po(self):
		if self.typ=='p' or (self.phival is not None and self.rval is not None): return {'phi': self.phival, 'r':self.rval}
		if self.typ=='k':
			from math import atan2,sqrt;from wartosci.kat import kat
			self.phival=kat(atan2(self.y,self.x),"rad") ; self.rval=sqrt((self.x^2)+(self.y^2))
			return {'phi':self.phival,'r':self.rval}
	@property
	def ka(self):
		if self.typ=='k' or (self.x is not None and self.y is not None): return {'x': self.x, 'y':self.y}
		if self.typ=='p':
			self.x=self.rval*self.phival.sin ; self.y=self.rval*self.phival.cos
			return {'x': self.x,'y':self.y}
	def __add__(self, other):
		adddict=other
		if 'r' in adddict.keys() or 'phi' in adddict.keys():
			_ = self.po
			newr = self.rval+adddict['r'] if 'r' in adddict else self.rval
			newphi = self.phival+adddict['phi'] if 'phi' in adddict else self.phival
			return pos({'r':newr,'phi':newphi})
		elif 'x' in adddict.keys() or 'y' in adddict.keys():
			_ = self.ka
			newx = self.x+adddict['x'] if 'x' in adddict else self.x
			newy = self.y+adddict['y'] if 'y' in adddict else self.y
			return pos({'x':newx,'y':newy})
	def __sub__(self, other):
		"""Będzie nam to dawało przesunięcie, jakie trzeba zrobić, żeby z other przenieść się na self"""
		return {'x':self.ka['x']-other.ka['x'],'y':self.ka['y']-other.ka['y']}
