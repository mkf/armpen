# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
class soft:
	def __init__(self,sr,sph):
		self.arc = arc
		self.proste = proste
	def posmodif(self,sr,sph):
		self.sr = sr
		self.sph = sph
class arc:
	def __init__(self,l,tz,azim,sr,sph,ta="deg",spha="deg",azima="deg"):
		import math
		self.l = l
		self.sr = sr
		self.sph = sph
		self.t = t = abs(tz)
		self.tz = tz
		self.clkw=clkw=math.s
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
class proste(arc):
	def __init__(self,l,azim,sr,sph,spha="deg",azima="deg"):
		arc.__init__(self,l,0,azim,sr,sph,spha=spha,azima=azima)
		self.r=r=float('inf')
