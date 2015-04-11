# -*- coding: utf-8 -*-
class convtopnm:
	def __init__(self,inplik,outplik):
		from PIL import Image
		im = Image.open(inplik)
		outfile = open(outplik,mode='w')
		im.save(outfile,format="PPM")
from sys import argv
convtopnm(argv[1],argv[2])