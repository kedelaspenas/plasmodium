from os import listdir, mkdir
from os.path import join, isfile
import re, os
from random import shuffle

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

try:
	mkdir('train')
	mkdir('test')
	mkdir('train/falciparum')
	mkdir('test/falciparum')
	mkdir('train/non-falciparum')
	mkdir('test/non-falciparum')
except:
	pass

positives = list_files('falciparum')
negatives = list_files('non-falciparum')

shuffle(positives)
shuffle(negatives)

p = len(positives)
n = len(negatives)

for i in range(int(p*0.60)):
	os.system('cp falciparum/'+positives[i] + ' train/falciparum/' + positives[i])

for i in range(int(p*0.60),p,1):
	os.system('cp falciparum/'+positives[i] + ' test/falciparum/' + positives[i])

for i in range(int(n*0.60)):
	os.system('cp non-falciparum/'+negatives[i] + ' train/non-falciparum/' + negatives[i])

for i in range(int(n*0.60),n,1):
	os.system('cp non-falciparum/'+negatives[i] + ' test/non-falciparum/' + negatives[i])
