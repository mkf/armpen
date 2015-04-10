# -*- coding: utf-8 -*-
from moduly.arm import maszyna
from moduly.wartosci import kat


class fake(maszyna):
	def __init__(self):
		l1 = 20
		l2 = 10
		# temporarily givin' up the elbow direction
		# maybe even forever
		#maxalphafromzero = kat(180,"deg")
		#minalphafromzero = -self.maxalphafromzero
		maxbetafromzero = kat(90,"deg")
		minbetafromzero = -maxbetafromzero
		alphaprecision = kat(0.01,"deg")
		betaprecision = kat(0.01,"deg")



		maszyna.__init__(self,l1,l2,maxbetafromzero,minbetafromzero,alphaprecision,betaprecision)

	def podnies_pioro(self): print "Podniesiono"
	def opusc_pioro(self): print "Opuszczono"
	def movealpha(self,ruch): pass
	def movebeta(self,ruch): pass
