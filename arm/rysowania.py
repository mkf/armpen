# -*- coding: utf-8 -*-

class rysowania:
	def __init__(self):pass
	"""
		self.funkcja = funkcja
		self.bezier = bezier
		self.prosta = prosta
		self.plot = plot
		self.plotxy = plotxy
		self.plotrphi = plotrphi
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
	def __init__(self,startPhi,startR): assert (startR<1 or startR==1);self.startPhi=startPhi;self.startR=startR

class punkt(rysunek):
	def __init__(self,startPhi,startR): rysunek.__init__(self,startPhi,startR)
	def draw(self,maszyna):
		maszyna.przemiesc(self.startPhi,self.startR)
		maszyna.opusc_pioro()

class funkcja(rysunek):
	def __init__(self,startPhi,startR): rysunek.__init__(self,startPhi,startR)

class bezier(funkcja):
	def __init__(self,startPhi,startR,c1Phi,c1R,c2Phi,c2R,endPhi,endR):
		funkcja.__init__(self,startPhi,startR)
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

class plot(funkcja):
	def __init__(self,zeroPhi,zeroR): funkcja.__init__(self,zeroPhi,zeroR)
class plotxy(plot):
	def __init__(self,zeroPhi,zeroR,maxXzeroYPhi,maxXzeroYR,maxYzeroXPhi,maxYzeroXR): plot.__init__(self,zeroPhi,zeroR)