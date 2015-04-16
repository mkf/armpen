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
		self.betaenginemultiplier = 56
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
	def __exit__(self, exc_type, exc_val, exc_tb):
		self.motalph.idle()
		self.motbeta.idle()
		self.ster.play_tone_and_wait(440,1)
	#def czyhome(self): return {'alphaodzera':self.tzeralph.get_sample(),'beta':self.tzerbeta.get_sample()}
	def podnies_pioro(self): 
		#self.motpenc.turn(-100,self.ilepencil)
		print "Podniesiono — kłamstwo"
	def opusc_pioro(self): 
		#self.motpenc.turn(50,self.ilepencil)
		print "Opuszczono — kłamstwo"
	def movealpha(self,ruchc):
		ruch = (ruchc.deg if isinstance(ruchc,kat) else ruchc)   #tu minus czy plus?
		if ruch==0: return None
		elif ruch<0: przod=False
		elif ruch>0: przod=True
		motalph = self.motalph
		motalph.turn(100 if przod else -100,abs(ruch*self.alphaenginemultiplier))
	def movebeta(self,ruchc):
		ruch = -(ruchc.deg if isinstance(ruchc,kat) else ruchc)
		if ruch==0: return None
		elif ruch<0: przod=False
		elif ruch>0: przod=True
		motbeta = self.motbeta
		motbeta.turn(100 if przod else -100,abs(ruch*self.betaenginemultiplier))
	def syncedmove(self,ac,bc):
		a = (ac.deg if isinstance(ac,kat) else ac)   #tu minus czy plus?
		b = -(bc.deg if isinstance(bc,kat) else bc)
		#1: leader w sync porusza się lepiej, beta zachowuje się jak przyczepka na lekko sprężystym sznurku,
		#   regularnie podbija, dogania gwałtownie
		#2: ale przy ratio bliskim 50 beta zachowuje się brzydko
		#
		#na razie wolimy ratio dalsze ze względu na 2
		if a==0: self.movebeta(b) ; cont = False
		elif b==0: self.movealpha(a) ; cont = False
		elif a<0 and b<0: przod = False;przeciwne = False ; cont = True
		elif a<0 and b>0: przod = None; przeciwne = True ; cont = True ; doprzodu = 'b'
		elif a>0 and b<0: przod = None; przeciwne = True ; cont = True ; doprzodu = 'a'
		elif a>0 and b>0: przod = True; przeciwne = False ; cont = True
		else: raise ValueError("bez sensu w syncedmove")
		if cont:
			if not przeciwne:
				adb = (a/b)*(self.alphaenginemultiplier/self.betaenginemultiplier)
				bda = (b/a)*(self.betaenginemultiplier/self.alphaenginemultiplier)
				if bda>=adb: ratva = bda ; lead = 'b'
				else: ratva = adb ; lead = 'a'
				ratvf = 50-(50*ratva)
			elif przeciwne:
				adb = abs((a/b)*(self.alphaenginemultiplier/self.betaenginemultiplier))
				bda = abs((b/a)*(self.betaenginemultiplier/self.alphaenginemultiplier))
				if bda>=adb: ratva = bda ; lead = 'b'
				else: ratva = adb ; lead = 'a'
				if doprzodu==lead: przod = True
				else: przod = False
				ratvf = 50+(50*ratva)
			if lead=='a': leader = self.motalph ; follower = self.motbeta ; distlead = abs(a*self.alphaenginemultiplier)
			elif lead=='b': leader = self.motbeta ; follower = self.motalph ; distlead = abs(b*self.betaenginemultiplier)
			motsync = SynchronizedMotors(leader,follower,ratvf)
			if przod: motsync.turn(100,distlead)
			elif not przod: motsync.turn(-100,distlead)

	def gdziejestesmaszyno(self): return self.whereami  #tutaj można to zrobić lepiej, ale to później
