# -*- coding: utf-8 -*-
from __future__ import division
class kat:
	def __init__(self,w,a):
		from math import degrees,radians
		self.defaultaforinterior="deg"  # config: default for internal operations if needed
		#self.degOLrad = lambda wart: lambda x,ax: x if ax==wart else (degrees(x) if wart=="deg" else radians(x) if wart=="rad" else 'degolradfirsterror') if ax==("deg" if wart=="rad" else "rad" if wart=="deg" else 'degolrad-seconderror') else 'degOLrad-lasterror'
		def degOLrad(radeg):
			def zamiana(xw,xa):
				if xa==radeg or (radeg=="deg" and xa=="deg") or (radeg=="rad" and xa=="rad"):
					return xw
				elif radeg=="deg" and xa=="rad":
					return degrees(xw)
				elif radeg=="rad" and xa=="deg":
					return radians(xw)
				else: 
					print "prob z degOLrad"
					raise ValueError('prob z degOLrad')
			return zamiana
		self.degOLrad = degOLrad		
		self.w=w;self.a=a;self.degval=None;self.radval=None;self.sinval=None;self.cosval=None;self.tanval=None
		assert a in ("rad","deg")
		assert isinstance(w,int) or isinstance(w,float) or isinstance(w,long) or isinstance(w,complex)
	def __str__(self): return str([self.w,self.a])
	@property
	def deg(self):
		if self.w==0: return 0.0
		elif self.degval is None:
			degval=self.degOLrad('deg')(self.w,self.a)
			self.degval = degval
			return degval
		else: return self.degval
	@property
	def rad(self):
		if self.w==0: return 0.0
		elif self.radval is None:
			radval = self.degOLrad("rad")(self.w,self.a)
			self.radval=radval
			return radval
		else: return self.radval
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
	def __eq__(self, other): return self.deg==other.deg #or self.rad==other.rad
	def __lt__(self, other): return self.deg < other.deg #and self.rad<other.rad
	def __le__(self, other): return self.__eq__(other) or self.__lt__(other)
	def __ne__(self, other): return not self.__eq__(other)
	def __gt__(self, other): return self.deg > other.deg #and self.rad > other.rad
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
		if trigt=='cos':
			if val==1: atrig = lambda x: 0 if x==1 else None
			else:from math import acos as atrig
		elif trigt=='sin': from math import asin as atrig
		elif trigt=='tan': from math import atan as atrig
		try:
			kat.__init__(self,atrig(val),'rad')
			naszval = val
			print "Ale tu dobrze liczy!: ",atrig,val
		except ValueError:
			print atrig, val , val*0.9999999999
			if trigt=='sin' or trigt=='cos':
				try:
					kat.__init__(self,atrig(val*0.9999999999),'rad')
					naszval = val*0.9999999999
				except ValueError:
					raise
			else: raise
		if trigt=='cos': self.cosval = naszval ; self.sinval=sqrt(1-(naszval**2)) ; self.tanval=sqrt(1-(naszval**2))/naszval
		elif trigt=='sin': self.sinval = naszval ; self.cosval=sqrt(1-(naszval**2)) ; self.tanval=naszval/sqrt(1-(naszval**2))
		elif trigt=='tan': self.tanval = val ; self.sinval=val/sqrt(1+(val**2)) ; self.cosval=1/sqrt(1+(val**2))
