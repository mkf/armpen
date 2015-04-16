# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.real import real
from moduly.zrodla.testsource import testsource
with real() as arm:
	with testsource('blah') as src:
		for i in src.daj():
			i.draw(arm,0.1)
			print i,i.__dict__