from os import listdir, mkdir
from os.path import join, isfile
import re

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

falci = ['']
count = 0
files = 0
with open('falci') as f:
	rx = [l.strip().split('-') for l in f.readlines()]
	#for r in rx:
	#	print r[0] + '.JPG-' + r[1] + '(.)*'
	rx = [re.compile('(IMG_)?' + r[0] + '.JPG-' + r[1] + '[-\.].*') for r in rx]
	rx_m = {}
	print len(rx)
	with open('labels', 'w') as f:
		for l in list_files('out'):
			matched = False
			files = files + 1
			for r in rx:
				if r.match(l):
					#print l
					rx_m[r] = True
					f.write(l + ',1' + '\n')
					matched = True
					count = count + 1
					break
			if not matched:
				f.write(l + ',0' + '\n')
	for r in rx:
		try:
			if not rx_m[r]:
				pass
		except:
			print r.pattern
print count, files
