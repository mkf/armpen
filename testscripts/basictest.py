# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.fake import fake
from moduly.zrodla.testsource import testsource
with testsource('blah') as src:
	for i in src.daj(): print i
