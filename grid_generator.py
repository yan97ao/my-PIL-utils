# -*- coding: gbk -*-
import Image,ImageDraw
import sys

def main():
	if len(sys.argv) !=6 :
		print "Usage: ./wxy.py ��� �߶� X��� Y��� �����ļ���"
		quit()
	
	width=int(sys.argv[1])
	height=int(sys.argv[2])
	intervalX=int(sys.argv[3])
	intervalY=int(sys.argv[4])
	savename=sys.argv[5]
	
	im=Image.new('RGB',(width, height),(255,255,255))    
	draw = ImageDraw.Draw(im	)

	for i in range(0,width,intervalX):
		draw.line(((i,0),(i,height)),fill=(0,0,0))
	for j in range(0,height,intervalY):
		draw.line(((0,j),(width,j)),fill=(0,0,0))		
	
	#im.show()
	im.save(savename)

if __name__ == "__main__":
	main()