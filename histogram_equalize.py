#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#        Author: yan97ao
#                magictao[AT]gmail.com
#       License: GPL V3	
#Python Version: Python 2.7.1 
"""
实现直方图均衡化处理
"""
import sys
import operator
import Image
import matplotlib.pyplot as plt

def equalize(h):
	lut = []
	step = reduce(operator.add, h[0:256]) / 255
	n = 0
	for i in range(256):
		lut.append(n / step)
		n = n + h[i]
	return lut

def main():
	if len(sys.argv) != 2 :
		print "Usage: ./histogram_equalize.py filename"
		quit()
	
	ifile = sys.argv[1]
	im = Image.open(ifile).convert("L")
	im.show()
	#im.load()
	x=range(0,256)
	
	fig=plt.figure(0)
	ax=fig.add_subplot(2,1,1)
	his=im.histogram()
	ax.plot(x,his)
	ax.set_title("Original Histogram",fontsize=18)
	ax.set_xlim(0,255)
	ax.grid(True)
	
	lut=equalize(im.histogram())
	im=im.point(lut)
	im.show()
	bx=fig.add_subplot(2,1,2)
	his=im.histogram()
	bx.plot(x,his)
	bx.set_title("Equalized Histogram",fontsize=18)
	bx.set_xlim(0,255)
	bx.grid(True)
	plt.show()

if __name__ == "__main__":
	main()
#- EOF -
