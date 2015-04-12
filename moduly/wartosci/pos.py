# -*- coding: utf-8 -*-
from moduly.wartosci.kat import kat
class pos:
	def __init__(self,coordict):
		self.xval=None;self.yval=None;self.phival=None;self.rval=None
		if 'x' in coordict and 'y' in coordict:
			self.xval = coordict['x'] ; self.yval=coordict['y'] ; self.typ='k'
		if ('phi' in coordict or 'theta' in coordict) and 'r' in coordict:
			self.phival = coordict['phi'] if 'phi' in coordict else coordict['theta'] if 'theta' in coordict else None
			self.rval=coordict['r'] ; self.typ='p'
	def __dict__(self):
		di = {}
		if self.phival is not None: di.update({'phi':self.phival})
		if self.rval is not None: di.update({'r':self.rval})
		if self.xval is not None: di.update({'x':self.xval})
		if self.yval is not None: di.update({'y':self.yval})
		return di
	def __getitem__(self, item):
		if item in self.__dict__: return self.__dict__[item]
		else: raise IndexError
	@property
	def r(self):
		if self.rval is not None: return self.rval
		else:
			from math import sqrt
			self.rval = sqrt((self.xval^2)+(self.yval^2))
			return self.rval
	@property
	def phi(self):
		if self.phival is not None: return self.phival
		else:
			from math import atan2
			self.phival = kat(atan2(self.yval,self.xval),"rad")
			return self.phival
	@property
	def po(self): return {'phi':self.phi,'r':self.r}
	@property
	def x(self):
		if self.xval is not None: return self.xval
		else: self.xval=self.rval*self.phival.sin ; return self.xval
	@property
	def y(self):
		if self.yval is not None: return self.yval
		else: self.yval=self.rval*self.phival.cos ; return self.yval
	@property
	def ka(self): return {'x': self.x,'y':self.y}
	def __add__(self, other):
		adddict=other
		if 'r' in adddict.keys() or 'phi' in adddict.keys():
			newr = self.r+adddict['r'] if 'r' in adddict else self.r
			newphi = self.phi+adddict['phi'] if 'phi' in adddict else self.phi
			return pos({'r':newr,'phi':newphi})
		elif 'x' in adddict.keys() or 'y' in adddict.keys():
			newx = self.x+adddict['x'] if 'x' in adddict else self.x
			newy = self.y+adddict['y'] if 'y' in adddict else self.y
			return pos({'x':newx,'y':newy})
	def __sub__(self, other):
		"""Będzie nam to dawało przesunięcie, jakie trzeba zrobić, żeby z other przenieść się na self"""
		return {'x':self.x-other.x,'y':self.y-other.y}