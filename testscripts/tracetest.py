# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from sys import argv
from moduly.zrodla.rastrimg import rastrimg

a = rastrimg(argv[1])
for i in a: print i