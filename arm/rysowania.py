# -*- coding: utf-8 -*-

from wartosci.kat import kat

class rysowania:
	def __init__(self):
		self.funkcja = krzywa
		self.specramiona=specramiona
		self.bezier = bezier
		self.prosta = prosta
		self.plot = plot
		self.plotxy = plotxy
		self.plotrphi = plotrphi
		self.protrphiFromZero=plotrphiFromZero
	"""
		self.stozkowa = stozkowa
		self.arc = arc
		self.arccentrZero = arccentrZero
		self.arccentrArmOneRArmTwoOrLess = arccentrArmOneRArmTwoOrLess
		self.arccentrArmOneRArmTwoExactly = arccentrArmOneRArmTwoExactly
		self.parabola = parabola
		self.hiperbola = hiperbola
		self.fragelipsy = fragelipsy
		self.elipsa = elipsa
		self.fragelpisyFZero = fragelipsyFZero
		self.okrag = okrag
		self.okragcentrArmOneRArmTwoOrLess = okragcentrArmOneRArmTwoOrLess
		self.okragcentrArmOneRArmTwoExactly = okragcentrArmOneRArmTwoExactly
"""

class rysunek:
	def __init__(self,start):self.start=start

class krzywa(rysunek):
	def __init__(self,start): rysunek.__init__(self,start)

class punkt(rysunek):
	def __init__(self,gdzie): rysunek.__init__(self,gdzie);self.gdzie=gdzie
	def draw(self,maszyna):
		self.gdzie.przemiesc()
		maszyna.opusc_pioro()

class prosta(cubicbezier):
	def __init__(self,start,end): cubicbezier.__init__(self,start,start,end,end)

class quadrbezier(krzywa):    # fragment paraboli
	def __init__(self,start,c,end):
		krzywa.__init__(self,start)
		self.c=c
	def draw(self):

class cubicbezier(krzywa):
	def __init__(self,start,c1,c2,end):
		krzywa.__init__(self,start)
		self.c1=c1
		self.c2=c2
	def draw(self,maszyna):
		from armpoz import armpoz
		armpoz(self.start,maszyna).przemiesc
		maszyna.opusc_pioro()
		funk = lambda t: {'w':,'e':t>=1}

class plot(krzywa):
	def __init__(self,zeroPhi,zeroR): krzywa.__init__(self,zeroPhi,zeroR)
class plotxy(plot):
	def __init__(self,fFromX,zeroPhi,zeroR,oneXzeroYPhi,oneXzeroYR,oneYzeroXPhi,oneYzeroXR):
		plot.__init__(self,zeroPhi,zeroR)
		self.oneXzeroYPhi=oneXzeroYPhi;self.oneXzeroYR=oneXzeroYR;self.oneYzeroXPhi=oneYzeroXPhi;self.oneYzeroXR=oneYzeroXR
		self.fFromX=fFromX
class plotrphi(plot):
	def __init__(self,fFromPhi,zeroPhi,zeroR,minR,maxR,minPhi,maxPhi,phiZero):
		plot.__init__(self,zeroPhi,zeroR)
		self.fFromPhi=fFromPhi
		self.minR=minR
		self.maxR=maxR
		self.phiZero=phiZero
class plotrphiFromZero(plotrphi):
	def __init__(self,fFromPhi,minR,maxR,minPhi,maxPhi,phiZero): plotrphi.__init__(self,fFromPhi,kat(0,"deg"),0,minR,maxR,minPhi,maxPhi,phiZero)
class arcfromzero(plotrphiFromZero):
	def __init__(self,r,minPhi,maxPhi):
		plotrphiFromZero.__init__(self,lambda x:r,r,r,minPhi,maxPhi,kat(0,"deg"))
		self.r=r;self.minPhi=minPhi;self.maxPhi=maxPhi
	def draw(self,arm):