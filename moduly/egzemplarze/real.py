# -*- coding: utf-8 -*-
from __future__ import division
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat
import nxt.locator
from nxt.motor import Motor,PORT_A,PORT_B,PORT_C,SynchronizedMotors
from nxt.sensor import Touch,PORT_1,PORT_2
#from time import sleep

class real(maszyna):
	def __init__(self):
		l1 = 26.58
		l2 = l1 * (0.426/0.574)
		# temporarily givin' up the elbow direction
		# maybe even forever
		maxalphafromzero = kat(180,"deg")
		minalphafromzero = -maxalphafromzero
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
		self.ster = nxt.locator.find_one_brick()
		self.motalph = Motor(self.ster,PORT_A)
		self.motbeta = Motor(self.ster,PORT_B)
		#self.motpenc = Motor(self.ster,PORT_C)
		#self.tzeralph = Touch(self.ster,PORT_1)
		#self.tzerbeta = Touch(self.ster,PORT_2)
		#self.motpenc.reset_position()
		#self.motpenc.run(power=10)
		#sleep(5)
		#self.motpenc.idle()
		#odczytaj ile przejechał
		#wez wartosc i uzywaj do późniejszych podnoszeń i opuszczeń
		#self.ilepencil = self.motpenc.get_tacho()  #tu nie będzie jedynki tylko ta wartosc
		return self
	def __exit__(self, exc_type, exc_val, exc_tb): pass
	#def czyhome(self): return {'alphaodzera':self.tzeralph.get_sample(),'beta':self.tzerbeta.get_sample()}
	def podnies_pioro(self): 
		#self.motpenc.turn(-100,self.ilepencil)
		print "Podniesiono — kłamstwo"
	def opusc_pioro(self): 
		#self.motpenc.turn(50,self.ilepencil)
		print "Opuszczono — kłamstwo"
	def movealpha(self,ruchc):
		if isinstance(ruchc,kat): ruch = ruchc.deg
		else: ruch = ruchc
		motalph = self.motalph
		from numpy import sign
		motalph.turn(sign(ruch*self.alphaenginemultiplier),abs(ruch*self.alphaenginemultiplier))
	def movebeta(self,ruchc):
		if isinstance(ruchc,kat): ruch = ruchc.deg
                else: ruch = ruchc
		motbeta = self.motbeta
		from numpy import sign
		motbeta.turn(sign(ruch*self.betaenginemultiplier),abs(ruch*self.betaenginemultiplier))
	def syncedmove(self,ac,bc):
		if isinstance(ac,kat): a = ac.deg
                else: a = ac
		if isinstance(bc,kat): b = bc.deg
                else: b = bc
		if a*self.alphaenginemultiplier<=b*self.betaenginemultiplier:
			pie = b*self.betaenginemultiplier
			dru = a*self.alphaenginemultiplier
			mpie = self.motbeta
			mdru = self.motalph
		else:
			pie = a*self.alphaenginemultiplier
			dru = b*self.betaenginemultiplier
			mpie = self.motalph
			mdru = self.motbeta
		ratio = dru/pie
		motsync = SynchronizedMotors(mpie,mdru,ratio)
		from numpy import sign
		motsync.turn(sign(dru)*100,abs(pie))

	def gdziejestesmaszyno(self): return self.whereami  #tutaj można to zrobić lepiej, ale to później
