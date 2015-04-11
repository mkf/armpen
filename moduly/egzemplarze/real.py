# -*- coding: utf-8 -*-
from __future__ import division
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat
import nxt.locator
from nxt.motor import *

class real(maszyna):
	def __init__(self):
		l1 = 26.58
		l2 = l1 * (0.426/0.574)
		# temporarily givin' up the elbow direction
		# maybe even forever
		maxalphafromzero = kat(180,"deg")
		minalphafromzero = -self.maxalphafromzero
		maxbeta = kat(90,"deg")
		minbeta = -maxbeta
		alphaprecision = kat(0.01,"deg")
		betaprecision = kat(0.01,"deg")
		self.alphaenginemultiplier = 168
		self.betaenginemultiplier = 168   # jeszcze nie wiadomo
		self.drawarea = lambda pozy: True

		maszyna.__init__(self,l1,l2,maxalphafromzero,minalphafromzero,maxbeta,minbeta,alphaprecision,betaprecision)
		#self.progfile = open('rysprog.py','w')
		#self.linprog('def main():',0)
	#def linprog(self,tresc,sintend): self.progfile.write(('    '*sintend)+tresc+"\n")
	def __enter__(self):
		pass
		return self
	def __exit__(self, exc_type, exc_val, exc_tb): pass
	def podnies_pioro(self): 
		#self.linprog('#costam motor C podnies',1)
		print "Podniesiono"
	def opusc_pioro(self): 
		#self.linprog('#costam motor C opusc',1)
		print "Opuszczono"
	def movealpha(self,ruch): pass #self.linprog('#costam motor A rusz o tyle',1)
	def movebeta(self,ruch): pass #self.linprog('#costam motor B rusz o tyle',1)
	def syncedmove(self,a,b): pass #self.linprog('#costam synced move motor A z synced motor B',1)
