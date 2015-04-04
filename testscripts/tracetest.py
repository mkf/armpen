# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from sys import argv,path
path.insert(0,'..')
from moduly.zrodla.rastrimg import rastrimg

a = rastrimg(argv[1])
for i in a: print i