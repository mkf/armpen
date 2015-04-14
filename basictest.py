# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.fake import fake
from moduly.zrodla.testsource import testsource
with fake() as arm:
	with testsource('blah') as src:
		for i in src.daj():
			i.draw(arm,0.01)
			print i,i.__dict__