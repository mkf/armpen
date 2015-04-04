# -*- coding: utf-8 -*-
from __future__ import division
class maszyna:
	def __init__(self):
		from wartosci.kat import kat
		import armpoz
		self.l1 = 20
		self.l2 = 10
		# temporarily givin' up the elbow direction
		# maybe even forever
		#self.maxalphafromzero = kat(180,"deg")
		#self.minalphafromzero = -self.maxalphafromzero
		self.maxbetafromzero = kat(90,"deg")
		self.minbetafromzero = -self.maxbetafromzero
		self.alphaprecision = kat(0.01,"deg")
		self.betaprecision = kat(0.01,"deg")
		self.alphaenginemultiplier = 10
		self.betaenginemultiplier = 20

	# noinspection PyMethodMayBeStatic
	def opusc_pioro(self):
		print "Opuszczono pióro"
	def podnies_pioro(self):
		print "Podniesiono pióro"

	def gdziejestesmaszyno(self):
		from armpoz import gdzieramiona;from wartosci.kat import kat
		return gdzieramiona(kat(20,"deg"),kat(40,"deg"),self)  # dummy, to be replaced by real location
	def dajnasilnik(self,co):
		print co
		end = False
		gdzie = 0.0
		done = 0.0
		lastalpha = co.startpoz.alphaodzera
		lastbeta = co.startpoz.beta
		while not end:
			ruchalpha = None
			ruchbeta = None
			syncmultforbetafromalpha = None
			assert gdzie>=done
			if done==gdzie: gdzie+=co.step
			elif done<gdzie:
				toc = co.funkcja(gdzie)
				to = toc['w']
				if abs(lastalpha-to.alphaodzera)<self.alphaprecision and abs(lastbeta-to.beta)<self.betaprecision:
					gdzie+=co.step
				else:
					if abs(lastalpha-to.alphaodzera)>=self.alphaprecision:
						ruchalpha=to.alphaodzera-lastalpha
					if abs(lastbeta-to.beta)>=self.betaprecision:
						ruchbeta=to.beta-lastbeta
					if ruchalpha is not None and ruchbeta is not None:
						syncmultforbetafromalpha=ruchbeta/ruchalpha
						print syncmultforbetafromalpha, ruchalpha, ruchbeta  #debug
					elif ruchalpha is None and ruchbeta is not None:
						print ruchbeta  #debug
					elif ruchbeta is None and ruchalpha is not None:
						print ruchalpha  #debug
				end = toc['e']
				print "end: %s" % str(end)

class nasilnik:
	def __init__(self,funkcja,startpoz,step,opis):
		self.funkcja=funkcja;self.startpoz=startpoz;self.step=step
		assert isinstance(opis, str)
		self.__str__ = "Komenda@step%s: %s" % (str(step),opis)