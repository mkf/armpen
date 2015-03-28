# -*- coding: utf-8 -*-
class soft:
	def __init__(self,sr,sph):
		self.bezier = bezier
		self.arc = arc
		self.proste = proste
		self.sr = sr
		self.sph = sph
	def posm(self,sr,sph):
		self.sr = sr
		self.sph = sph
class polar:
	"""Kartezjańskie na biegunowe"""
	def __init__(self): self.degOLrad = lambda w: lambda x,a: x if a==w else (math.degrees(x) if w=="deg" else math.radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
	@staticmethod
	def fkartz(x,y): import math;return {'phi':math.atan2(y,x),'phia':'rad','r':math.sqrt((x^2)+(y^2))}
	@staticmethod
	def tkartz(phi,r,phia="rad"): import math;return {'x':r*math.sin(self.degOLrad("rad")(phi,phia)),'y':r*math.cos(self.degOLrad("rad")(phi,phia))}
class bezier:
	"""Krzywa Beziera"""
	def __init__(self,sph,sr,c1ph,c1r,c2ph,c2r,eph,er):
		pass
class arc:
	"""Łuk"""
	def __init__(self,l,tz,azim,sr,sph,ta="deg",spha="deg",azima="deg"):
		import math
		import numpy
		self.l = l
		self.sr = sr
		self.sph = sph
		self.t = t = abs(tz)
		self.tz = tz
		self.clkw=clkw=float(numpy.sign(tz))
		self.ta = ta
		self.spha = spha
		self.azim = azim
		self.azima=azima
		for aexampel in (ta,spha,azima): assert aexampel=="deg" or aexampel=="rad"
		degOLrad = lambda w: lambda x,a: x if a==w else (math.degrees(x) if w=="deg" else math.radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
		self.deg=deg=degOLrad("deg")(t,ta)
		self.rad=rad=degOLrad("rad")(t,ta)
		self.sphdeg=sphdeg=degOLrad("deg")(sph,spha)
		self.sphrad=sphrad=degOLrad("rad")(sph,spha)
		self.azimdeg=azimdeg=degOLrad("deg")(azim,azima)
		self.azimrad=azimrad=degOLrad("rad")(azim,azima)
		self.czyproste=czyproste=t==0
		self.r=r = float(l)/float(rad) if not czyproste else float('inf')
	def draw(self):
		pass
class arccentr(arc):
class proste(arc):
	"""Prosta jako odmiana łuku"""
	def __init__(self,l,azim,sr,sph,spha="deg",azima="deg"):
		arc.__init__(self,l,0,azim,sr,sph,spha=spha,azima=azima)
		self.r=r=float('inf')
class punkt:
	def __init__(self,r,ph,pha="deg"):
		import math
		degOLrad = lambda w: lambda x,a: x if a==w else (math.degrees(x) if w=="deg" else math.radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
		self.r=r
		self.ph=ph
		self.phdeg=phdeg=degOLrad("deg")(ph,pha)
		self.phrad=phrad=degOLrad("rad")(ph,pha)
	def draw(self):
		pass