# -*- coding: utf-8 -*-
__author__ = 'ArchieT'
from moduly.egzemplarze.real import real
from moduly.wartosci.kat import kat
with real() as arm:
	#arm.chamskonasilnik(kat(-90,"deg"),kat(-90,"deg"))
	#arm.chamskonasilnik(kat(20,"deg"),kat(30,"deg"))
	#arm.chamskonasilnik(alpha=kat(-25,"deg"))
	# tutaj będziemy troche besęsu, z założeniem że jesteśmy w zerze, za pomocą relatywnych narzędzi alternatywnych robić absoluty
	#jesteśmy w zerze
	#def dajbetezalphy(self,alpha):
	#	ade = alpha.deg
	#	fu = lambda a:
	#	funk = lambda al: kat(fu(al),'deg')
	# zrezygnowaliśmy z rysowania prostych, bo to już na jutro
	#zakładamy że ramię wyprostowane
	done = False
	sync = False
	corys = None
	ang = None
	beta = None
	while not done:
		while corys is None:
			co = raw_input('co ruszyć? a/b/s : ' if sync else 'co ruszyć? a/b : ')
			for i in list(co):
				if sync and (i=='a' or i=='b' or i=='s'): corys = i
				elif not sync and (i=='a' or i=='b'): corys = i
				if corys is not None: break
		while ang is None:
			tang = raw_input('podaj kąt alfy ' if corys=='s' and sync else 'podaj kąt ')
			try: ang = float(tang)
			except ValueError: pass
		if sync and corys=='s':
			while beta is None:
				tbet = raw_input('podaj kąt bety ')
				try: beta = float(tbet)
				except ValueError: pass
		if sync and corys=='s': arm.chamskonasilnik(alpha=kat(ang,"deg"),beta=kat(beta,"deg"))
		elif corys=='a': arm.chamskonasilnik(alpha=kat(ang,"deg"))
		elif corys=='b': arm.chamskonasilnik(beta=kat(ang,"deg"))
