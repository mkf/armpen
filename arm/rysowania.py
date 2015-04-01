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

class specramiona:
	def __init__(self,startAlpha,startBeta,): pass

class rysunek:
	def __init__(self,startPhi,startR):
		assert (startR<1 or startR==1)
		self.startPhi=startPhi
		self.startR=startR

class krzywa(rysunek):
	def __init__(self,startPhi,startR): rysunek.__init__(self,startPhi,startR)

class punkt(rysunek):
	def __init__(self,startPhi,startR): rysunek.__init__(self,startPhi,startR)
	def draw(self,maszyna):
		maszyna.przemiesc(self.startPhi,self.startR)
		maszyna.opusc_pioro()

class bezier(krzywa):
	def __init__(self,startPhi,startR,c1Phi,c1R,c2Phi,c2R,endPhi,endR):
		krzywa.__init__(self,startPhi,startR)
		self.c1Phi=c1Phi
		self.c1R=c1R
		self.c2Phi=c2Phi
		self.c2R=c2R
	def draw(self,maszyna):
		maszyna.przemiesc(self.startPhi,self.startR)
		maszyna.opusc_pioro()
		# dalej

class prosta(bezier):
	def __init__(self,startPhi,startR,endPhi,endR):
		bezier.__init__(self,startPhi,startR,startPhi,startR,endPhi,endR,endPhi,endR)
	def draw(self,maszyna):
		maszyna.przemiesc(self.startPhi,self.startR)
		maszyna.opusc_pioro()
		# dalej

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
