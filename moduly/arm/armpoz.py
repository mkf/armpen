# -*- coding: utf-8 -*-
from __future__ import division
from moduly.wartosci.pos import pos
from moduly.wartosci.kat import arctrig

# noinspection PyClassHasNoInit
class MovingMixIn:
	def przemiesc(self):
		from moduly.arm.maszyna import nasilnik
		naszaf = lambda x: {'w':self,'e':x>0}
		last = self.arm.gdziejestesmaszyno()
		dajemy = nasilnik(naszaf,last,1,"Przemieszczenie na %s" % str(dict(self)))
		arm = self.arm
		arm.podnies_pioro()
		arm.dajnasilnik(dajemy)

class armpoz(MovingMixIn,pos):
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
		assert arm.maxbetafromzero >= self.beta >= arm.minbetafromzero
		#self.alphaodzera = self.phival+self.alphaodr if (self.alphaodr.w==0 or self.phival+self.alphaodr<arm.maxalphafromzero) else self.phival-self.alphaodr if self.phival-self.alphaodr>arm.minalphafromzero else 'err'
		self.alphaodzera=(self.phival+self.alphaodr).naplaszczyznie['katnaplaszczyznie']
		assert self.alphaodzera != 'err'
	def __add__(self, other):
		adddict = other
		if 'r' in adddict.keys() or 'phi' in adddict.keys():
			newr = self.rval+adddict['r'] if 'r' in adddict else self.rval
			newphi = self.phival+adddict['phi'] if 'phi' in adddict else self.phival
			return armpoz({'r':newr,'phi':newphi},self.arm)
		elif 'x' in adddict.keys() or 'y' in adddict.keys():
			_ = self.ka
			newx = self.xval+adddict['x'] if 'x' in adddict else self.xval
			newy = self.yval+adddict['y'] if 'y' in adddict else self.yval
			return armpoz({'x':newx,'y':newy},self.arm)
		elif 'alpha' in adddict.keys() or 'beta' in adddict.keys():
			newaoz = self.alphaodzera+adddict['alpha'] if 'alpha' in adddict else self.alphaodzera
			newbet = self.beta+adddict['beta'] if 'alpha' in adddict else self.beta
			return gdzieramiona(newaoz,newbet,self.arm).dajpoz

class gdzieramiona(MovingMixIn):
	def __init__(self,alphaodzera,beta,arm):
		self.alphaodzera=alphaodzera
		self.beta=beta
		self.arm=arm
		self.__dict__={'alphaodzera':alphaodzera,'beta':beta,'arm':arm}
	@property
	def dajpoz(self):
		try: return self.armpozy
		except NameError: pass
		arm=self.arm
		beta=self.beta
		alph=self.alphaodzera
		from math import sqrt  #,acos
		radi = sqrt(arm.l1*arm.l1+(arm.l2*arm.l2)-(2*arm.l1*arm.l2*beta.cos))
		alodr=arctrig((arm.l1-(arm.l2*beta.cos))/radi,'cos')
		# elbow direction temporarily given up
		pozd = {'r':radi,'phi':(alph-alodr).naplaszczyznie['katnaplaszczyznie']}
		self.armpozy = armpoz(pozd,self.arm)
		return self.armpozy
	def __add__(self,other):
		saoz=self['alphaodzera']+other['alphaodzera']
		sbet=self['beta']+other['beta']
		return gdzieramiona(saoz,sbet,self.arm)
