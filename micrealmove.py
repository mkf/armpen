# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.real import real
from moduly.wartosci.kat import kat
from nxt.sensors import PORT_1,PORT_2,Touch,Sound
blah = raw_input('Podłącz czujniki do 1,2 przy kostce alfa i wciśnij enter')
am = float(raw_input('daj współczynnik alpha '))
bm = float(raw_input('daj współczynnik beta '))
assert am!=0 and bm!=0,str('%s,%s' % (str(am),str(bm)))
with real() as arm:
	touch = Touch(arm.stera,PORT_1)
	sound = Sound(arm.stera,PORT_2)
	while True:
		dzw = sound.get_sample()
		if am!=0 and bm!=0 and dzw!=0:
			if touch.get_sample(): arm.chamskonasilnik(alpha=am*dzw,beta=bm*dzw)
		elif bm!=0 and dzw!=0:
			if touch.get_sample(): arm.chamskonasilnik(beta=bm*dzw)
		elif am!=0 and dzw!=0:
			if touch.get_sample(): arm.chamskonasilnik(alpha=am*dzw)
