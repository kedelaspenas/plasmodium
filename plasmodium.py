from os import listdir, mkdir
from os.path import join, isfile
import cv2, numpy as np

inputfolder = 'data3'
outputfolder = 'out'
outstats = open("stats.out", "w")

def list_files(foldername):
	return [f for f in listdir(foldername) if isfile(join(foldername, f))]

def process_image(path):
	img = cv2.imread(path)
	rows, cols, channels = img.shape
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	sat = hsv[:,:,1]
	Io = cv2.morphologyEx(sat, cv2.MORPH_OPEN, se)
	Ic = cv2.morphologyEx(Io, cv2.MORPH_CLOSE, se)
	mean, stdDev = cv2.meanStdDev(Ic)
	Ic = np.array(Ic - mean - stdDev, np.float32)
	Ic[Ic < 0] = 0
	v,bw = cv2.threshold(Ic, 20, 255, cv2.THRESH_BINARY)
	bw = np.array(bw, dtype=np.uint8)
	im2, contours, hierarchy = cv2.findContours(bw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	idx = 0
	for c in contours:
		imgc = img.copy()

		# bounding box and convex hull
		x,y,w,h = cv2.boundingRect(c)
		hull = cv2.convexHull(c)
		hull_area = cv2.contourArea(hull)

		# compute contour properties
		area = cv2.contourArea(c)
		perimeter = cv2.arcLength(c, True)
		aspect_ratio = w/h
		extent = float(area)/(w*h)
		try:
			solidity = area/hull_area
		except:
			continue
		equiv_diameter = np.sqrt(4*area/np.pi)
		try:
			(x_el, y_el), (major_axis_length, minor_axis_length), orientation = cv2.fitEllipse(c)
		except:
			continue
		# write properties to file
		properties = [area, perimeter, aspect_ratio, extent, solidity, equiv_diameter, major_axis_length, minor_axis_length, orientation]
		outstats.write(path + "," + str(idx) + "," + ",".join([str(p) for p in properties]) + '\n')

		# draw bounding box
		dd = max(w,h)
		startx = x if x + w < cols else cols - dd - 1
		starty = y if y + h < rows else rows - dd - 1

		if area >= 5000:
			# draw image
			cv2.imwrite(join(outputfolder, f + '-' + str(idx) + '.jpg'), img[starty:starty+dd,startx:startx+dd,:])

			for z in range(15,360,15):
				M = cv2.getRotationMatrix2D((startx + dd/2, starty + dd/2),z,1)
				rot = cv2.warpAffine(img,M,(cols, rows))
				cv2.imwrite(join(outputfolder, f + '-' + str(idx) + '-' + str(z) + '.jpg'), rot[starty:starty+dd,startx:startx+dd,:])
		#cv2.rectangle(imgc, (startx, starty), (startx+dd, starty+dd), (255,0,0),5)
		#cv2.imwrite(join(outputfolder, f + '-b-' + str(idx) + '.jpg'), imgc)
		#cv2.imwrite(join(outputfolder, f + '-' + str(idx) + '.jpg'), img[starty:starty+dd,startx:startx+dd,:])
		idx = idx + 1



#############################################################

# 					GODDAMMIT STARTS HERE					#

#############################################################
files = list_files(inputfolder)
try:
	mkdir(outputfolder)
except:
	print "cannot create folder"

se = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (19,19))
print se
for f in files:
	path = join(inputfolder, f)
	process_image(path)

outstats.close()
