# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.fake import fake
from moduly.wartosci.kat import kat
with fake() as arm:
	arm.chamskonasilnik(kat(10,"deg"),kat(10,"deg"))
	arm.chamskonasilnik(kat(20,"deg"),kat(30,"deg"))