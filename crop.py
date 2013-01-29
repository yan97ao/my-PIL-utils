# -*- coding: gbk -*-
"""
图像分块切割
"""

import Image
import sys

def main():
    fileName = raw_input("文件名")
    w = raw_input("横向大小")
    h = raw_input("纵向大小")    
    
    w = int(w)    
    h = int(h)
    
    im=Image.open(fileName)
    width,height=im.size
    
    numberOfTile_W = width / w
    numberOfTile_H = height / h    
        
    if numberOfTile_W * w != width :
        numberOfTile_W += 1
    if numberOfTile_H * w != height :
        numberOfTile_H += 1   
    fullWidth = numberOfTile_W * w
    fullHeight = numberOfTile_H * h
    
    newIm=Image.new('RGB',(fullWidth, fullHeight),(255,255,255))        
    newIm.paste(im,(0,0,width,height))    

    for i in range(numberOfTile_W) :
        for j in range(numberOfTile_H) :
            box = (i * w,j * h,(i+1) * w,(j+1) * h)            
            tile = newIm.crop(box)
            tile.save(str(i)+'-'+str(j)+'.png')            

if __name__ == '__main__':
    main()