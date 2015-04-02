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
		#self.alphaodzera = self.phival+self.alphaodr if (self.alphaodr.w==0 or self.phival+self.alphaodr<arm.maxalphafromzero) else self.phival-self.alphaodr if self.phival-self.alphaodr>arm.minalphafromzero else 'err'
		self.alphaodzera=(self.phival+self.alphaodr).naplaszczyznie['katnaplaszczyznie']
		assert self.alphaodzera != 'err'
	def przemiesc(self):
		from maszyna import maszyna, nasilnik
		naszaf = lambda x: {'w':self,'e':x==1}
		last = maszyna.gdziejestesmaszyno()
		dajemy = nasilnik(naszaf,last,"Przemieszczenie na %s" % str(dict(self)))
		maszyna().dajnasilnik(dajemy,1)

class gdzieramiona:
	def __init__(self,alphaodzera,beta,arm):
		self.alphaodzera=alphaodzera
		self.beta=beta
		self.arm=arm
	@property
	def dajpoz(self):
		try: return self.armpozy
		except NameError: pass
		arm=self.arm
		beta=self.beta
		alph=self.alphaodzera
		from math import acos,sqrt
		radi = sqrt(arm.l1**2+(arm.l2**2)-(2*arm.l1*arm.l2*beta.cos))
		alodr=arctrig((arm.l1-(arm.l2*beta.cos))/radi,'cos')
		# elbow direction temporarily given up
		pozd = {'r':radi,'phi':(alph-alodr).naplaszczyznie['katnaplaszczyznie']}
		self.armpozy = armpoz(pozd,self.arm)
		return self.armpozy