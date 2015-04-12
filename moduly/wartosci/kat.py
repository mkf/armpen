# -*- coding: utf-8 -*-
from __future__ import division
class kat:
	def __init__(self,w,a):
		from math import degrees,radians
		self.defaultaforinterior="deg"  # config: default for internal operations if needed
		self.degOLrad = lambda wart: lambda x,ax: x if a==w else (degrees(x) if w=="deg" else radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
		self.w=w;self.a=a;self.degval=None;self.radval=None;self.sinval=None;self.cosval=None;self.tanval=None
		assert a in ("rad","deg")
		assert isinstance(w,int) or isinstance(w,float) or isinstance(w,long) or isinstance(w,complex)
	@property
	def deg(self):
		if self.w==0: return 0.0
		elif self.degval is None:
			self.degval=self.degOLrad('deg')(self.w,self.a)
			return self.degval
	@property
	def rad(self):
		if self.w==0: return 0.0
		elif self.radval is None:
			self.radval=self.degOLrad("rad")(self.w,self.a)
			return self.radval
	def __mul__(self, other):
		assert isinstance(other,int) or isinstance(other,float) or isinstance(other,long) or (isinstance(other,complex) and other.imag==0)
		if self.w==0: return self
		return kat(self.w*other,self.a)
	def __add__(self, other):
		assert isinstance(other,kat)
		cowkoncu = lambda w,a: w.deg if a=="deg" else w.rad if a=="rad" else None
		return kat(other.w+self.w,self.a) if other.a==self.a else kat(cowkoncu(other,self.defaultaforinterior)+cowkoncu(self,self.defaultaforinterior),self.defaultaforinterior)
	def __neg__(self): return kat(-self.w,self.a)
	def __pos__(self): return self  # redundant, I know.
	def __sub__(self, other): assert isinstance(other,kat); return self.__add__(other.__neg__)
	def signum(self): return 0 if self.w==0 else 1 if self.w>0 else -1 if self.w<0 else None
	def onesign(self): return 1 if self.w>=0 else -1 if self.w<0 else None
	def __abs__(self): return self.__neg__ if self.w<0 else self
	def __truediv__(self, other):
		assert isinstance(other,kat)
		cowkoncu = lambda w,a: w.deg if a=="deg" else w.rad if a=="rad" else None
		return self.w/other.w if other.a==self.a else cowkoncu(self,self.defaultaforinterior)/cowkoncu(other,self.defaultaforinterior)
	@property
	def naplaszczyznie(self):
		print self.a,self.w    #debug
		zdiva=divmod(self.w if (self.a=="deg" or self.a=="rad") else self.deg, float(360) if self.a=="deg" else kat(360,"deg").rad if self.a=="rad" else float(360))
		return {'katnaplaszczyznie': kat(zdiva[1],self.a),'pelnych':int(zdiva[0])}
	@property
	def cwiartka(self):
		zdiva=divmod(self.w,float(90) if self.a=="deg" else kat(90,"deg").rad if self.a=="rad" else None)
		return {'cwiartka':int(zdiva[0]),'ostry':kat(zdiva[1],self.a)}
	def __eq__(self, other): return self.deg==other.deg or self.rad==other.rad
	def __lt__(self, other): return self.deg < other.deg and self.rad<other.rad
	def __le__(self, other): return self.__eq__(other) or self.__lt__(other)
	def __ne__(self, other): return not self.__eq__(other)
	def __gt__(self, other): return self.deg > other.deg and self.rad > other.rad
	def __ge__(self, other): return self.__eq__(other) or self.__gt__(other)
	@property
	def sin(self):
		if self.sinval is not None: return self.sinval
		from math import sin
		self.sinval = sin(self.rad)
		return self.sinval
	@property
	def cos(self):
		if self.cosval is not None: return self.cosval
		from math import cos
		self.cosval = cos(self.rad)
		return self.cosval
	@property
	def tan(self):
		if self.tanval is not None: return self.tanval
		from math import tan
		self.tanval = tan(self.rad)
		return self.tanval
class arctrig(kat):
	def __init__(self,val,trigt):
		assert trigt in ['cos','sin','tan']
		from math import sqrt
		if trigt=='cos': from math import acos as atrig
		elif trigt=='sin': from math import asin as atrig
		elif trigt=='tan': from math import atan as atrig
		kat.__init__(self,atrig(val),'rad')
		if trigt=='cos': self.cosval = val ; self.sinval=sqrt(1-(val**2)) ; self.tanval=sqrt(1-(val**2))/val
		elif trigt=='sin': self.sinval = val ; self.cosval=sqrt(1-(val**2)) ; self.tanval=val/sqrt(1-(val**2))
		elif trigt=='tan': self.tanval = val ; self.sinval=val/sqrt(1+(val**2)) ; self.cosval=1/sqrt(1+(val**2))