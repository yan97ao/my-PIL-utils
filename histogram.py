#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#        Author: yan97ao
#                magictao[AT]gmail.com
#       License: GPL V3	
#Python Version: Python 2.7.1 
"""
实现直方图显示
"""
import sys
import Image
import matplotlib.pyplot as plt


def main():
	if len(sys.argv) != 2 :
		print "Usage: ./histogram_equalize.py filename"
		quit()
	
	ifile = sys.argv[1]
	im = Image.open(ifile).convert("L")
	im.load()
	x=range(0,256)
	
	fig=plt.figure(0)
	ax=fig.add_subplot(1,1,1)
	his=im.histogram()
	print his
	ax.plot(x,his)
	ax.set_xlim(0,255)
	ax.grid(True)
	
	#plt.show()

if __name__ == "__main__":
	main()

__revision__ = '0.1'
#- EOF -
