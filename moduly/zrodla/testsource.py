# -*- coding: utf-8 -*-
from moduly.obiekty import rysowania
from moduly.wartosci.pos import pos

class testsource:
	def __init__(self,co): self.co = co
	def __enter__(self): print "start",self.co ; return self
	def __exit__(self, exc_type, exc_val, exc_tb): print "bye",self.co
	def daj(self):
		i = 1
		while i<10:
			toprosta = rysowania.prosta(pos({'x':float(i)/float(10),'y':0.1}), pos({'x':float(i)/float(10),'y':0.7}))
			yield toprosta
			#yield rysowania.

			i+=1
			print toprosta
			print self.co