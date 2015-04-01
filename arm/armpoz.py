# -*- coding: utf-8 -*-
from wartosci.kat import kat,arctrig
from wartosci.pos import pos
from math import acos
from __future__ import division
class armpoz(pos):
	def __init__(self,poz,arm):
		pos.__init__(self,poz)
		self.arm = arm
		wyprost = poz.r==arm.l1+arm.l2
		assert arm.l1+arm.l2>poz.r or wyprost, "Nie starcza ramion"
		selfpo = self.po
		cosalpha = (arm.l1/(2*self.rval))+(self.rval/(2*arm.l1))-(arm.l2**2/(2*self.rval*arm.l1))
		cosbeta = (arm.l1/(2*arm.l2))+(arm.l2/(2*arm.l1))-(self.rval**2/(2*arm.l1*arm.l2))
		self.alpha = arctrig(cosalpha,'cos')
		self.beta = arctrig(cosbeta,'cos')