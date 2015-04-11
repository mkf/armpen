# -*- coding: utf-8 -*-
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat


class fake(maszyna):
	def __init__(self):
		l1 = 20
		l2 = 10
		# temporarily givin' up the elbow direction
		# maybe even forever
		maxalphafromzero = kat(180,"deg")
		minalphafromzero = -self.maxalphafromzero
		maxbeta = kat(90,"deg")
		minbeta = -maxbeta
		alphaprecision = kat(0.01,"deg")
		betaprecision = kat(0.01,"deg")
		self.drawarea = lambda pozy: True



		maszyna.__init__(self,l1,l2,maxalphafromzero,minalphafromzero,maxbeta,minbeta,alphaprecision,betaprecision)

	def podnies_pioro(self): print "Podniesiono"
	def opusc_pioro(self): print "Opuszczono"
	def movealpha(self,ruch): print ruch
	def movebeta(self,ruch): print ruch
	def syncedmove(self,a,b): print a,b
