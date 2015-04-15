# -*- coding: utf-8 -*-
from __future__ import division
from moduly.arm.armpoz import gdzieramiona
from moduly.wartosci.kat import kat
class maszyna:
	def __init__(
			self,
			l1,l2,
			maxalphafromzero,minalphafromzero,
			maxbeta,minbeta,
			alphaprecision,
			betaprecision,
	):
		self.homepos = gdzieramiona(kat(0,"deg"),kat(0,"deg"),self)
		self.whereami = self.homepos
		self.l1=l1;self.l2=l2
		self.maxalphafromzero=maxalphafromzero;self.minalphafromzero=minalphafromzero
		self.maxbeta=maxbeta;self.minbeta=minbeta
		self.alphaprecision=alphaprecision;self.betaprecision=betaprecision

		naszefunkcje = dir(self)

		assert 'podnies_pioro' in naszefunkcje
		assert 'opusc_pioro' in naszefunkcje
		assert 'gdziejestesmaszyno' in naszefunkcje
		

		assert 'movealpha' in naszefunkcje
		assert 'movebeta' in naszefunkcje
		assert 'syncedmove' in naszefunkcje

		assert 'drawarea' in naszefunkcje

	def armzakrescheck(self,pozy):
		return self.minalphafromzero<=pozy['alphaodzera']<=self.maxalphafromzero and self.minbeta<=pozy['beta']<=self.maxbeta

	# noinspection PyMethodMayBeStatic
	def dajnasilnik(self,co):
		#print co
		end = False
		gdzie = 0.0
		done = 0.0
		lastalpha = co.startpoz.alphaodzera
		lastbeta = co.startpoz.beta
		while not end:
			ruchalpha = None
			ruchbeta = None
			assert gdzie>=done
			if done==gdzie: gdzie+=co.step
			elif done<gdzie:
				toc = co.funkcja(gdzie)
				to = toc['w']
				if abs(lastalpha-to.alphaodzera)<self.alphaprecision and abs(lastbeta-to.beta)<self.betaprecision:
					gdzie+=co.step
				elif self.armzakrescheck(to) and self.drawarea(to):
					if abs(lastalpha-to.alphaodzera)>=self.alphaprecision:
						ruchalpha=to.alphaodzera-lastalpha
					if abs(lastbeta-to.beta)>=self.betaprecision:
						ruchbeta=to.beta-lastbeta

					if ruchalpha is not None and ruchbeta is not None:
						self.syncedmove(ruchalpha,ruchbeta)
						self.whereami+={'alphaodzera':ruchalpha,'beta':ruchbeta}
						print ruchalpha, ruchbeta  #debug
					elif ruchalpha is None and ruchbeta is not None:
						self.movebeta(ruchbeta)
						self.whereami+={'alphaodzera':kat(0,"deg"),'beta':ruchbeta}
						print ruchbeta  #debug
					elif ruchbeta is None and ruchalpha is not None:
						self.movealpha(ruchalpha)
						self.whereami+={'alphaodzera':ruchalpha,'beta':kat(0,"deg")}
						print ruchalpha  #debug
				else: print "Nie narysowano — poza zakresem: ", str(dict(to))
					

				end = toc['e']
				print "end: %s" % str(end)
		def gdziejestesmaszyno(self):
			return self.whereami

class nasilnik:
	def __init__(self,funkcja,startpoz,step,opis):
		self.funkcja=funkcja;self.startpoz=startpoz;self.step=step
		assert isinstance(opis, str)
		self.__str__ = "Komenda@step%s: %s" % (str(step),opis)
		print self.__str__
