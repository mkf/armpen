# -*- coding: utf-8 -*-
class kat:
	degOLrad = lambda w: lambda x,a: x if a==w else (math.degrees(x) if w=="deg" else math.radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
	def __init__(self,w,a):
		self.w=w;self.a=a;self.degval=None;self.radval=None
		assert a in ("rad","deg")
	@property
	def deg(self):
		if self.w==0: return 0
		if self.degval is None: self.degval=self.degOLrad("deg")(self.w,self.a)
		return self.degval
	@property
	def rad(self):
		if self.w==0: return 0
		if self.radval is None: self.radval=self.degOLrad("rad")(self.w,self.a)
		return self.radval
	def skalar(self,czynnik):
		if self.w==0: return self
		return kat(w*czynnik,a)
	def dodajinny(self,inny,wczymifnotsame):
		return kat(inny.w+self.w,self.a) if inny.a==self.a else kat(inny.eval(wczymifnotsame)+self.eval(wczymifnotsame),wczymifnotsame)
	@property
	def ujemny(self): return kat(-self.w,self.a)
	@property
	def naplaszczyznie(self):
		zdiva=divmod(self.w,kat(360,"deg").eval(self.a))
		return {'katnaplaszczyznie': kat(zdiva[1],self.a),'pelnych':int(zdiva[0])}
	@property
	def cwiartka(self):
		zdiva=divmod(self.w,kat(90,"deg").eval(self.a))
		return {'cwiartka':int(zdiva[0]),'ostry':kat(zdiva[1],self.a)}
	def porownaj(self,inny):
		return (self.deg==inny.deg or self.rad==inny.rad)
	@property
	def sin(self):
		from math import sin
		return sin(self.rad)
	@property
	def cos(self):
		from math import cos
		return cos(self.rad)
	@property
	def tan(self):
		from math import tan
		return tan(self.rad)