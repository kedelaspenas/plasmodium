from os.path import join, isfile
import cv2, numpy as np, os
from os import listdir, mkdir

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

try:
  os.mkdir('out64')
except:
  pass
data = list_files('out')
for d in data:
  img = cv2.imread('out/' + d)
  scaled = cv2.resize(img, (64,64), interpolation=cv2.INTER_CUBIC)
  cv2.imwrite('out64/' + d, scaled)
