# -*- coding: utf-8 -*-
from moduly.obiekty import rysowania
from moduly.wartosci.pos import pos

class testsource:
	def __init__(self): pass
	def daj(self):
		i = 1
		while i<10:
			yield rysowania.prosta(pos({'x':float(i)/float(10),'y':0.1}), pos({'x':float(i)/float(10),'y':0.7}))
			#yield rysowania.

			i+=1