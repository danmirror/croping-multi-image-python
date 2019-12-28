import os
import cv2
import numpy

from os import listdir
from os.path import isfile, join


pixelx1 = 256
pixely1 = 256
pixelx2 = 149
pixely2 = 149
row = 0
column = 0

mypath='colony_p1'
folder_new = "p1_colony"
os.mkdir(folder_new)

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
     images[n] = cv2.imread( join(mypath,onlyfiles[n]) )
     name =os.path.splitext( onlyfiles[n])[0]
     print(name)

     os.mkdir(folder_new+"/"+name)
     os.mkdir(folder_new+"/"+name+"/"+"256x256")
     os.mkdir(folder_new+"/"+name+"/"+"149x149")
     folder_write1 = join(folder_new+"/"+name+"/"+"256x256")
     folder_write2 = join(folder_new+"/"+name+"/"+"149x149")

     h,w,_ =  images[n] .shape
     for y in range (0,h,pixelx1):
          row+=1
          column = 0
          for x in range(0,w,pixely1):
               column+=1
               # print(x,y)
               width =x+pixelx1
               height = y+pixely1
               # print("w= "+str(width)+" == h="+str(height))

               cropped = images[n] [y:height, x:width]
               cv2.imwrite(folder_write1+"/"+name+"--"+str(row)+"x"+str(column)+"cropped.jpg", cropped)
     row = 0
     for y in range (0,h,pixelx2):
          row+=1
          column = 0
          for x in range(0,w,pixely2):
               column+=1
               # print(x,y)
               width =x+pixelx2
               height = y+pixely2
               cropped =  images[n] [y:height, x:width]
               cv2.imwrite(folder_write2+"/"+name+"--"+str(row)+"x"+str(column)+"cropped.jpg", cropped)
     row = 0
cv2.waitKey(0)