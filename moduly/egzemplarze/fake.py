# -*- coding: utf-8 -*-
from __future__ import division
from moduly.arm.maszyna import maszyna
from moduly.wartosci.kat import kat
import pygame
from time import sleep

class fake(maszyna):
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
		self.drawarea = lambda pozy: True
		self.pioro = False
		self.ostat = self.whereami

		maszyna.__init__(self,l1,l2,maxalphafromzero,minalphafromzero,maxbeta,minbeta,alphaprecision,betaprecision)
	def __enter__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((640,480))
		self.image = pygame.image.load("testimage.png")

		return self
	def __exit__(self, exc_type, exc_val, exc_tb):sleep(1000)
	def podnies_pioro(self): print "Podniesiono";self.pioro=False
	def opusc_pioro(self):
		print "Opuszczono";self.pioro=True
		self.screen.blit(self.image,(int(self.ostat.dajpoz().ka['x']),int(self.ostat.dajpoz().ka['y'])))
	def movealpha(self,ruch):
		print ruch
		stepdivid = ruch*(1/100)
		def czesci():
			i = 0
			while i<100:
				yield self.ostat+{'alpha':i*stepdivid}
				i+=1
		for o in czesci():
			self.screen.blit(self.image,(int(o.ka['x']),int(o.ka['y'])))
			pygame.display.flip()
		self.ostat = self.whereami
	def movebeta(self,ruch):
		print ruch
		stepdivid = ruch*(1/100)
		def czesci():
			i = 0
			while i<100:
				yield self.ostat+{'beta':i*stepdivid}
				i+=1
		for o in czesci():
			self.screen.blit(self.image,(int(o.ka['x']),int(o.ka['y'])))
			pygame.display.flip()
		self.ostat = self.whereami
	def syncedmove(self,a,b):
		print a,b
		sda = a*(1/100)
		sdb = b*(1/100)
		def czesci():
			i = 0
			while i<100:
				yield self.ostat+{'alpha':i*sda,'beta':i*sdb}
				i+=1
		for o in czesci():
			self.screen.blit(self.image,(int(o.ka['x']),int(o.ka['y'])))
			pygame.display.flip()
		self.ostat = self.whereami
