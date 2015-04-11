# -*- coding: utf-8 -*-
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat
import nxt.locator
from nxt.motor import *

class real(maszyna):
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
		self.alphaenginemultiplier = 10
		self.betaenginemultiplier = 20
		self.drawarea = lambda pozy: True
		
		#TODO: w domu zrobic to z with, bo to w sumie bedzie zapis do pliku ostatecznie - zrobic to z __enter__ i __exit__
		#w sumie moze jednak nie
		
		maszyna.__init__(self,l1,l2,maxalphafromzero,minalphafromzero,maxbeta,minbeta,alphaprecision,betaprecision)
		#self.progfile = open('rysprog.py','w')
		#self.linprog('def main():',0)
	#def linprog(self,tresc,sintend): self.progfile.write(('    '*sintend)+tresc+"\n")
	def podnies_pioro(self): 
		#self.linprog('#costam motor C podnies',1)
		print "Podniesiono"
	def opusc_pioro(self): 
		#self.linprog('#costam motor C opusc',1)
		print "Opuszczono"
	def movealpha(self,ruch): pass #self.linprog('#costam motor A rusz o tyle',1)
	def movebeta(self,ruch): pass #self.linprog('#costam motor B rusz o tyle',1)
	def syncedmove(self,a,b): pass #self.linprog('#costam synced move motor A z synced motor B',1)
