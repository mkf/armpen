# -*- coding: utf-8 -*-
class kat:
	degOLrad = lambda w: lambda x,a: x if a==w else (math.degrees(x) if w=="deg" else math.radians(x) if w=="rad" else None) if a==("deg" if w=="rad" else "rad" if w=="deg" else None) else None
	def __init__(self,w,a): self.w=w;self.a=w;self.degval=None;self.radval=None
	@property
	def deg(self):
		if self.w==0: return 0
		if self.degval is None: self.degval=self.degOLrad("deg")(self.w,self.a)
		return self.degval
	@property
	def rad(self):
		if self.w==0: return 0
		if self.radval is None: self.radval=self.degOLrad("rad")(self.w,self.a)
		return self.radval