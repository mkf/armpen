# -*- coding: utf-8 -*-
class polar:
	"""Kartezjańskie na biegunowe"""
	def __init__(self): pass
	@staticmethod
	def topolar(x,y): from math import atan2,sqrt;from wartosci.kat import kat;return {'phi':kat(atan2(y,x),"rad"),'r':sqrt((x^2)+(y^2))}
	@staticmethod
	def tokartz(phi,r): return {'x':r*phi.sin,'y':r*phi.cos}