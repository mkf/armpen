# -*- coding: utf-8 -*-
class rastrimg:
	def __init__(self,file):
		from obiekty import rysowania
		from wartosci.pos import pos
		import potrace
		import numpy as np
		from PIL import Image
		im = Image.open(file)
		data = np.array(im)
		bmp = potrace.Bitmap(data)
		path = bmp.trace()
		for curve in path:
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