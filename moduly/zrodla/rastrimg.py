# -*- coding: utf-8 -*-
from moduly.obiekty import rysowania
from moduly.wartosci.pos import pos

class rastrimg:
	def __init__(self,plik):
		self.plik = plik
	def __enter__(self):
		import potrace
		import numpy as np
		from PIL import Image
		im = Image.open(self.plik)
		data = np.array(im)
		bmp = potrace.Bitmap(data)
		self.path = bmp.trace()
		return self
	def __exit__(self, exc_type, exc_val, exc_tb): print "Przetworzono obraz"
	def daj(self):
		for curve in self.path:
			curvestartx,curvestarty = curve.start_point
			startx=None
			starty=None
			for segment in curve:
				if startx is None: startx=curvestartx
				if starty is None: starty=curvestarty
				start = pos({'x':startx,'y':starty})
				endx,endy=segment.end_point
				end = pos({'x':endx,'y':endy})
				if segment.is_corner:
					cx,cy=segment.c
					c = pos({'x':cx,'y':cy})
					yield rysowania.prosta(start,c)
					yield rysowania.prosta(c,end)
				else:
					c1x,c1y=segment.c1
					c1 = pos({'x':c1x,'y':c1y})
					c2x,c2y=segment.c2
					c2 = pos({'x':c2x,'y':c2y})
					yield rysowania.cubicbezier(start,c1,c2,end)
				startx=endx;starty=endy
