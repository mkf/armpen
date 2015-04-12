# -*- coding: utf-8 -*-
from moduly.wartosci.kat import kat
class pos:
	def __init__(self,coordicti):
		debugg = False  # debug boolean
		self.debugg = debugg
		if debugg: print coordicti # debug
		coordict = dict(coordicti)
		if debugg: print coordict
		assert (('phi' in coordict or 'theta' in coordict) and 'r' in coordict) or ('x' in coordict and 'y' in coordict),coordict
		self.xval=None;self.yval=None;self.phival=None;self.rval=None
		if 'x' in coordict and 'y' in coordict:
			self.xval = coordict['x'] ; self.yval=coordict['y'] ; self.typ='k'
			if debugg: print self.xval , self.yval, self.typ
		if ('phi' in coordict or 'theta' in coordict) and 'r' in coordict:
			self.phival = coordict['phi'] if 'phi' in coordict else coordict['theta'] if 'theta' in coordict else None
			self.rval=coordict['r'] ; self.typ='p'
			if debugg: print self.phival, self.rval,self.typ
		if debugg: print "__init__: phi,r,x,y ",self.phival,self.rval,self.xval,self.yval
		assert (self.xval is not None and self.yval is not None) or (self.phival is not None and self.rval is not None)
	@property
	def dict(self):
		di = {}
		if self.debugg:
			print "__dict__"
			print self.phival,self.rval,self.xval,self.yval
		if self.phival is not None:
			di.update({'phi':self.phival})
			if self.debugg: print "di.update({'phi':self.phival})"
		if self.rval is not None:
			di.update({'r':self.rval})
			if self.debugg: print "di.update({'r':self.rval})"
		if self.xval is not None:
			di.update({'x':self.xval})
			if self.debugg: print "di.update({'x':self.xval})"
		if self.yval is not None:
			di.update({'y':self.yval})
			if self.debugg: print "di.update({'y':self.yval})"
		assert ('phi' in di and 'r' in di) or ('x' in di and 'y' in di),di
		return di
	def __dict__(self): return self.dict
	def __str__(self): return str(self.dict)
	def __getitem__(self, item): return self.dict[item]
	def __contains__(self, item): return item in self.dict
	def keys(self): return self.dict.keys()
	def __iter__(self): return iter(self.dict)
	def __repr__(self): return repr(self.dict)
	@property
	def r(self):
		if self.rval is not None: return self.rval
		elif self.xval is not None and self.rval is not None:
			from math import sqrt
			self.rval = sqrt((self.xval*self.xval)+(self.yval*self.yval))
			return self.rval
		else: print "self.xval",self.xval,'self.yval',self.yval,dict(self)
	@property
	def phi(self):
		if self.phival is not None: return self.phival
		elif self.xval is not None and self.yval is not None:
			from math import atan2
			self.phival = kat(atan2(self.y,self.x),"rad")
			return self.phival
		else: print "self.xval",self.xval,'self.yval',self.yval,dict(self)
	@property
	def po(self): return {'phi':self.phi,'r':self.r}
	@property
	def x(self):
		if self.xval is not None: return self.xval
		else: self.xval=self.r*self.phi.sin ; return self.xval
	@property
	def y(self):
		if self.yval is not None: return self.yval
		else: self.yval=self.r*self.phi.cos ; return self.yval
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