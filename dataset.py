from os import listdir, mkdir
from os.path import join, isfile
import re, os

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

try:
	mkdir('falciparum')
	mkdir('non-falciparum')
except:
	pass

falci = ['']

with open('falci') as f:
	rx = [l.strip().split('-') for l in f.readlines()]
	rx = [re.compile('(IMG_)?' + r[0] + '.JPG-' + r[1] + '[-\.].*') for r in rx]
	rot = re.compile('(IMG_)?[\d]+[\w]?\.JPG-[\d]+\.jpg')
	for l in list_files('out64'):
		#print l
		matched = False
		for r in rx:
			if r.match(l):
				matched = True
				os.system('cp out299/'+l+' falciparum/'+l)
				break
		if not matched and rot.match(l):
			os.system('cp out299/'+l+' non-falciparum/'+l)
