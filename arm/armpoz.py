# -*- coding: utf-8 -*-
from __future__ import division
from wartosci.kat import kat,arctrig
from wartosci.pos import pos
class armpoz(pos):
	def __init__(self,poz,arm):
		pos.__init__(self,poz)
		self.arm = arm
		wyprost = poz.r==arm.l1+arm.l2
		assert arm.l1+arm.l2>poz.r or wyprost, "Nie starcza ramion"
		_ = self.po
		cosalphaodr = (arm.l1/(2*self.rval))+(self.rval/(2*arm.l1))-(arm.l2**2/(2*self.rval*arm.l1))
		cosbeta = (arm.l1/(2*arm.l2))+(arm.l2/(2*arm.l1))-(self.rval**2/(2*arm.l1*arm.l2))
		self.alphaodr = arctrig(cosalphaodr,'cos')
		self.beta = arctrig(cosbeta,'cos')
		assert self.beta<=arm.maxbetafromzero and self.beta>=arm.minbetafromzero
		self.alphaodzera = self.phival+self.alphaodr if (self.alphaodr.w==0 or self.phival+self.alphaodr<arm.maxalphafromzero) else self.phival-self.alphaodr if self.phival-self.alphaodr>arm.minalphafromzero else 'err'
		assert self.alphaodzera != 'str'
class zarmpoz(armpoz):
	def __init__(self,alphaodzera,beta):
		pass