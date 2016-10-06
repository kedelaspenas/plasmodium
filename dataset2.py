from os import listdir, mkdir
from os.path import join, isfile

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

s = open('trophozoite', 'w')
for l in list_files('out299'):
  s.write(l + ',0\n')

s.close()
