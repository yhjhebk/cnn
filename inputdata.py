#!/usr/bin/python
#-*- coding: ASCII -*-
import cv2
import numpy as np
import os
def ImageToIn(rootdir,outputfile):
	output=open(outputfile,"wb")
	for parent, dirs, files in os.walk(rootdir):
		cout=1
		for image in files:
			#if cout>1:
			#	output.write('\n')
			img=cv2.imread(rootdir+"/"+image)
			b = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
			g = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
			r = np.zeros((img.shape[0],img.shape[1]), dtype=img.dtype)
			b[:,:] = img[:,:,0]
			g[:,:] = img[:,:,1]
			r[:,:] = img[:,:,2]
			#output.write(str(img.shape[0])+" "+str(img.shape[1]))
	    	#output.write('\n')
			rcount=0
			rtemp=0
			for rRow in r:
				for rvalue in rRow:
					if rtemp==rvalue :
						rcount+=1
					else:
						if rcount > 0:
							output.write(chr(rtemp))
							output.write(chr(rcount))
						rcount=1
						rtemp=rvalue
					if rcount==255:
						output.write(chr(rtemp))
						output.write(chr(rcount))
						rcount=0
			if rcount>0:
				output.write(chr(rtemp))
				output.write(chr(rcount))
			#output.write('\n')
			gcount=0
			gtemp=0
			for gRow in g:
				for gvalue in gRow:
					if gtemp==gvalue:
						gcount+=1
					else:
						if gcount>0:
							output.write(chr(gtemp))
							output.write(chr(gcount))
						gcount=1
						gtemp=gvalue
					if gcount==255:
						output.write(chr(gtemp))
						output.write(chr(gcount))
						gcount=0
			if gcount>0:
				output.write(chr(gtemp))
				output.write(chr(gcount))
			#output.write('\n')
			bcount=0
			btemp=0
			for bRow in b:
				for bvalue in bRow:
					if btemp==bvalue:
						bcount+=1
					else:
						if bcount>0:
							output.write(chr(btemp))
							output.write(chr(bcount))
						bcount=1
						btemp=bvalue
					if bcount==255:
						output.write(chr(btemp))
						output.write(chr(bcount))
						bcount=0
			if bcount>0:
				output.write(chr(btemp))
				output.write(chr(gcount))
			#np.savetxt("data.r",r,fmt=['%s']*r.shape[1],newline='\n')
			#np.savetxt("data.g",g,fmt=['%s']*g.shape[1],newline='\n')
			#np.savetxt("data.b",b,fmt=['%s']*b.shape[1],newline='\n')
	output.close()
	return 0
ImageToIn("../data/image","data.test")
