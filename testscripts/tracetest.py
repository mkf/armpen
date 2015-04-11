# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from sys import argv,path
path.insert(0,'..')
from moduly.zrodla.rastrimg import rastrimg

with rastrimg(argv[1]) as a:
	for i in a: print i