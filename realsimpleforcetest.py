# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.real import real
from moduly.wartosci.kat import kat
with real() as arm:
	#arm.chamskonasilnik(kat(-90,"deg"),kat(-90,"deg"))
	#arm.chamskonasilnik(kat(20,"deg"),kat(30,"deg"))
	arm.chamskonasilnik(alpha=kat(-25,"deg"))