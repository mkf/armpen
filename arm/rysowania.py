# -*- coding: utf-8 -*-

from wartosci.kat import kat

class rysunek:
	def __init__(self,start):self.start=start

class punkt(rysunek):
	def __init__(self,gdzie): rysunek.__init__(self,gdzie);self.gdzie=gdzie
	def draw(self,maszyna):
		self.gdzie.przemiesc()
		maszyna.opusc_pioro()

class krzywa(rysunek):
	def __init__(self,start,funkcjadefiniujaca):
		rysunek.__init__(self,start);self.funkcjadefiniujaca=funkcjadefiniujaca;self.step=step
	def draw(self,maszyna,step):
		self.funkcja=funkcja=self.funkcjadefiniujaca(maszyna)
		from armpoz import armpoz
		from maszyna import nasilnik
		armpoz(self.start.maszyna).przemiesc()
		maszyna.opusc_pioro()
		ruch = nasilnik(self.funkcja,self.start,step,str(self))

class prosta(krzywa):     #      prosta(cubicbezier):
	def __init__(self,start,end):   #cubicbezier.__init__(self,start,start,end,end)
		ks = start.ka;ke = end.ka; dx=ke['x']-ks['x'] ; dy=ke['y']-ks['y']
		from armpoz import armpoz
		funkdef = lambda arm: lambda t: {'w':armpoz({'x':(t*dx)+ks['x'],'y':(t*dy)+ks['y']},arm),'e':t>=1}
		krzywa.__init__(self,start,funkdef)
		self.end=end

class quadrbezier(krzywa):    # fragment paraboli
	def __init__(self,start,c,end):
		self.c=c;self.end=end;from armpoz import armpoz
		adfunk = lambda u,t: ((1-t)*(1-t)*start.ka[u])+(2*(1-t)*t*c.ka[u])+(t*t*end.ka[u])
		funkdef=lambda arm:lambda t:{
			'w':armpoz({
				'x': adfunk('x',t),
				'y': adfunk('y',t)
			},arm),
			'e':t>=1
		}
		krzywa.__init__(self,start,funkdef)

class cubicbezier(krzywa):
	def __init__(self,start,c1,c2,end):
		from armpoz import armpoz
		adfunk = lambda u,t: ((1-t)*(1-t)*(1-t)*start.ka[u])+(3*(1-t)*(1-t)*t*c1.ka[u])+(3*(1-t)*t*t*c2.ka[u])+(t*t*t*end.ka[u])
		funkcjadefiniujaca = lambda arm: lambda t: {'w':armpoz({
			'x':adfunk('x',t),
			'y':adfunk('y',t)
		},arm),'e':t>=1}
		krzywa.__init__(self,start,funkcjadefiniujaca)
		self.c1=c1;self.c2=c2;self.end=end

class plotxy(krzywa):
	def __init__(self,fFromX,zero,oneXzeroY,oneYzeroX): # one will be the maximum — you have to divide the values appropiately
		self.oneXzeroY=oneXzeroY;self.oneYzeroX=oneYzeroX;self.fFromX=fFromX
		from armpoz import armpoz
		#fdef=lambda arm:lambda x:{'w':armpoz({
		#	'x':x,
		#	'y':min(sorted([]))
		#})}
		def fdef(arm):
			def tocos(x):
				kolej = [0,fFromX(x),1];kolej.remove(min(kolej));kolej.remove(max(kolej))
				#tymczasowo będzie jechało po ramce jak wartość poza zakresem, później się to zmieni
				return {'w': armpoz({
					'x':x,
					'y':kolej[0],
				},arm),'e':x>=1}

class plotrphi(plot):
	def __init__(self,fFromPhi,zeroPhi,zeroR,minR,maxR,minPhi,maxPhi,phiZero):
		plot.__init__(self,zeroPhi,zeroR)
		self.fFromPhi=fFromPhi
		self.minR=minR
		self.maxR=maxR
		self.phiZero=phiZero
class plotrphiFromZero(plotrphi):
	def __init__(self,fFromPhi,minR,maxR,minPhi,maxPhi,phiZero): plotrphi.__init__(self,fFromPhi,kat(0,"deg"),0,minR,maxR,minPhi,maxPhi,phiZero)
class arcfromzero(plotrphiFromZero):
	def __init__(self,r,minPhi,maxPhi):
		plotrphiFromZero.__init__(self,lambda x:r,r,r,minPhi,maxPhi,kat(0,"deg"))
		self.r=r;self.minPhi=minPhi;self.maxPhi=maxPhi
	def draw(self,arm):