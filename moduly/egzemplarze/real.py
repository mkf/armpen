# -*- coding: utf-8 -*-
from __future__ import division
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat
import nxt.locator
from nxt.motor import Motor,PORT_A,PORT_B,PORT_C,SynchronizedMotors
from nxt.sensor import Touch,PORT_1,PORT_2
#from time import sleep
import Queue,threading

class real(maszyna):
	def __init__(self):
		l1 = 16  #26.58
		l2 = 16  #l1 * (0.426/0.574)
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
		self.stera = nxt.locator.find_one_brick("00:16:53:08:77:37") #Alexa
		self.sterb = nxt.locator.find_one_brick("00:16:53:07:F8:5B") #Kuby
		self.motalph = Motor(self.stera,PORT_A)
		self.motbeta = Motor(self.sterb,PORT_A)
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
		self.emergency()
		if not self.notanymoreabsolut: self.homepos.przemiesc()
		self.emergency()
		#self.ster.play_tone_and_wait(440,1)
	#def czyhome(self): return {'alphaodzera':self.tzeralph.get_sample(),'beta':self.tzerbeta.get_sample()}
	def podnies_pioro(self): 
		#self.motpenc.turn(-100,self.ilepencil)
		print "Podniesiono — kłamstwo"
	def opusc_pioro(self): 
		#self.motpenc.turn(50,self.ilepencil)
		print "Opuszczono — kłamstwo"
	def movealpha(self,ruchc,speed=127):
		ruch = (ruchc.deg if isinstance(ruchc,kat) else ruchc)   #tu minus czy plus?
		if ruch==0: return None
		elif ruch<0: przod=False
		elif ruch>0: przod=True
		motalph = self.motalph
		naszeta = abs(ruch*self.alphaenginemultiplier)
		try:
			motalph.turn(speed if przod else -speed,naszeta)
		except:
			print "struct.error"
			#import pdb
			#pdb.post_mortem()
	def movebeta(self,ruchc,speed=127):
		ruch = -(ruchc.deg if isinstance(ruchc,kat) else ruchc)
		if ruch==0: return None
		elif ruch<0: przod=False
		elif ruch>0: przod=True
		motbeta = self.motbeta
		naszeta = abs(ruch*self.betaenginemultiplier)
		try:
			motbeta.turn(speed if przod else -speed,naszeta)
		except:
			print "struct.error"
			#import pdb
			#pdb.post_mortem()
	def syncedmove(self,ac,bc):
		def dajna(q,mov,ruch,speed):
			q.put(mov(ruch,speed))
		at = (ac.deg if isinstance(ac,kat) else ac)   #tu minus czy plus?
		bt = -(bc.deg if isinstance(bc,kat) else bc)
		a = at*self.alphaenginemultiplier
		b = bt*self.betaenginemultiplier
		q = Queue.Queue()
		if b!=0 and a!=0:
			if abs(b)>=abs(a): speedb=100;speeda=100*(abs(a)/abs(b))
			elif abs(a)>abs(b): speeda=100;speedb=100*(abs(b)/abs(a))
		if b!=0:
			t = threading.Thread(target=dajna, args=(q,self.movebeta,bt,speedb))
			t.daemon = True
			t.start()
		if a!=0:
			t = threading.Thread(target=dajna, args=(q,self.movealpha,at,speeda))
			t.daemon = True
			t.start()
		s=q.get()
		print s
	def emergency(self):
		self.motalph.idle()
		self.motbeta.idle()
		print "IDLING"
	def gdziejestesmaszyno(self): return self.whereami  #tutaj można to zrobić lepiej, ale to później
