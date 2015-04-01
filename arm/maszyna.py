# -*- coding: utf-8 -*-
class maszyna:
	def __init__(self):
		from wartosci.kat import kat
		self.l1 = 20
		self.l2 = 10
		self.maxalphafromzero = kat(180,"deg")
		self.minalphafromzero = -self.maxalphafromzero
		self.maxbetafromzero = kat(90,"deg")
		self.minbetafromzero = -self.maxbetafromzero
		self.alphaprecision = kat(0.01,"deg")
		self.betaprecision = kat(0.01,"deg")
		self.alphaenginemultiplier = 10
		self.betaenginemultiplier = 20
	def opusc_pioro(self):
		print "Opuszczono pióro"
	def podnies_pioro(self):
		print "Podniesiono pióro"
	def dajnasilnik(self,co,prec,startpoz):
		print co
		end = False
		gdzie = 0.0
		done = 0.0
		lastalpha = startpoz.alphaodzera
		lastbeta = startpoz.beta
		while not end:
			assert gdzie>=done
			if done==gdzie: gdzie+=prec
			elif done<gdzie:
				to = co(gdzie)
				if abs(lastalpha-to.alphaodzera)<self.alphaprecision and abs(lastbeta-to.beta)<self.betaprecision:
					gdzie+=prec
				else: pass

class nasilnik:
	def __init__(self,falpha,fbeta,ilealpha,ilebeta,opis):
		self.falpha=falpha;self.fbeta=fbeta;self.ilealpha=ilealpha;self.ilebeta=ilebeta
	@property
	def __str__(self):
		return "Dajemy %s ilealpha %s ilebeta %s" % (opis,str(ilealpha),str(ilebeta))
