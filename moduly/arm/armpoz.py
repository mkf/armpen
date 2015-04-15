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
		pos.__init__(self,dict(poz))
		self.arm = arm
		wyprost = self.r==arm.l1+arm.l2
		if not (arm.l1+arm.l2>self.r or wyprost):
			print "Nie starcza ramion"
			assert arm.l1+arm.l2>self.r or wyprost, "Nie starcza ramion"
		if not (arm.l1-arm.l2<self.r):
			print "Za blisko![by lengths]",arm.l1,arm.l2,self.r
		assert arm.l1-arm.l2<self.r, "Za blisko![by lengths]"
		#print "l1",arm.l1,'l2',arm.l2,'r',self.r  #debug
		cosalphaodr = (arm.l1/(2*self.r))+(self.r/(2*arm.l1))-(arm.l2*arm.l2/(2*self.r*arm.l1))  # dla przykładowych wyszło ~1.04 — ale to chyba było za blisko po prostu
		cosbeta = (arm.l1/(2*arm.l2))+(arm.l2/(2*arm.l1))-(self.r*self.r/(2*arm.l1*arm.l2))
		try:
			self.alphaodr = arctrig(cosalphaodr,'cos')
			self.beta = arctrig(cosbeta,'cos')
		except ValueError:
			print "cosalphaodr",cosalphaodr,"cosbeta",cosbeta
			raise AssertionError("cosalphaodr",cosalphaodr,"cosbeta",cosbeta,"nie da się z tego wyliczyć arccos")
		#if not (arm.maxbeta >= self.beta >= arm.minbeta):
		#	print "maxbeta"+str(arm.maxbeta)+"beta"+str(self.beta)+"minbeta"+str(arm.minbeta)
		#	assert arm.maxbeta >= self.beta >= arm.minbeta, "maxbeta"+str(arm.maxbeta)+"beta"+str(self.beta)+"minbeta"+str(arm.minbeta)
		if arm.maxbeta<self.beta:
			print "MAXBETA"+str(arm.maxbeta)+"BETA"+str(self.beta)
			assert arm.maxbeta>=self.beta,"MAXBETA"+str(arm.maxbeta)+"BETA"+str(self.beta)
		if arm.minbeta>self.beta:
			print "MINBETA"+str(arm.minbeta)+"BETA"+str(self.beta)
			assert arm.minbeta<=self.beta,"MINBETA"+str(arm.minbeta),+"BETA"+str(self.beta)
		#self.alphaodzera = self.phival+self.alphaodr if (self.alphaodr.w==0 or self.phival+self.alphaodr<arm.maxalphafromzero) else self.phival-self.alphaodr if self.phival-self.alphaodr>arm.minalphafromzero else 'err'
		self.alphaodzera=(self.phi+self.alphaodr).naplaszczyznie['katnaplaszczyznie']
		if isinstance(self.alphaodzera,str) and self.alphaodzera=='err':
			print "self.alphaodzera=='err'"
			assert self.alphaodzera != 'err'
	def __add__(self, other):
		adddict = other
		if 'r' in adddict.keys() or 'phi' in adddict.keys():
			newr = self.r+adddict['r'] if 'r' in adddict else self.r
			newphi = self.phi+adddict['phi'] if 'phi' in adddict else self.phi
			return armpoz({'r':newr,'phi':newphi},self.arm)
		elif 'x' in adddict.keys() or 'y' in adddict.keys():
			newx = self.x+adddict['x'] if 'x' in adddict else self.xval
			newy = self.y+adddict['y'] if 'y' in adddict else self.yval
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
		except AttributeError: pass
		arm=self.arm
		beta=self.beta
		alph=self.alphaodzera
		from math import sqrt  #,acos
		radi = sqrt(arm.l1*arm.l1+(arm.l2*arm.l2)-(2*arm.l1*arm.l2*beta.cos))
		alodr=arctrig((arm.l1-(arm.l2*beta.cos))/radi,'cos')
		# elbow direction temporarily given up
		pozd = {'r':radi,'phi':(alph-alodr).naplaszczyznie['katnaplaszczyznie']}
		self.armpozy = armpozy = armpoz(pozd,self.arm)
		return armpozy
	def __add__(self,other):
		saoz=dict(self)['alphaodzera']+dict(other)['alphaodzera']
		sbet=dict(self)['beta']+dict(other)['beta']
		return gdzieramiona(saoz,sbet,self.arm)
