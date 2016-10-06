from os import listdir, mkdir
from os.path import join, isfile
import cv2, numpy as np, os

outputfolder = 'border_full'
def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

try:
	mkdir(outputfolder)
except:
	print "cannot create folder"

nf = list_files('border')
nf.sort()
labels2 = open('labels2','w')
#for f in nf:
	# names = f.split('-')
	# n = '-b-'.join(names)
	# os.system('mv border/'+n+' '+outputfolder+'/'+n)
labels2.write(',0\n'.join(nf))
