
from os import listdir, mkdir
from os.path import join, isfile
import os

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

def run_inference_on_image(imagePath, f):
    bazel = ['tensorflow-src/bazel-bin/tensorflow/examples/label_image/label_image', '--graph=output_graph.pb', '--labels=output_labels.txt', '--output_layer=final_result', '--image='+imagePath]
    os.system(' '.join(bazel) + ' > ' + f)

files = list_files('/home/kristofer/Documents/malaria-mask/test/falciparum/')
tp = 0
fn = 0
for f in files:
    ans = run_inference_on_image('/home/kristofer/Documents/malaria-mask/test/falciparum/' + f, f)
    if ans == 'falciparum':
        tp = tp + 1
    else:
        fn = fn + 1


files = list_files('/home/kristofer/Documents/malaria-mask/test/non-falciparum/')
tn = 0
fp = 0
for f in files:
    ans = run_inference_on_image('/home/kristofer/Documents/malaria-mask/test/non-falciparum/' + f, f)
    if ans == 'non-falciparum':
        tn = tn + 1
    else:
        fp = fp + 1

print tn, tp, fn. fp
