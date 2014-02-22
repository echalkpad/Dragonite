import urllib2
import cv2
import numpy as np
from matplotlib import pyplot as plt

URL="http://maps.google.com/maps/api/staticmap?center=43.0027342,-78.78751&zoom=19&size=2000x2000&sensor=true"
def create_image(url):
	f = urllib2.urlopen(url)
	img = open("./temp/temp.png",'w')
	print "writing image to file..."
	img.write(f.read())


def write_image(path, img):
	cv2.imwrite(path,img)

def edge_detection(image):
	img = cv2.imread(image,0)
	edges = cv2.Canny(img,10,10)
	#plt.subplot(122)
	write_image('./temp/temp1.png',edges)
	#plt.imshow(edges,cmap = 'gray')
	#plt.show()



def erode_and_dilate(image):
	img = cv2.imread(image,0)
	size = np.size(img)
	skel = np.zeros(img.shape,np.uint8)

	#ret,img = cv2.threshold(img,)
	element = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
	done = False
	while (not done):
		eroded = cv2.erode(img,element)
		temp = cv2.dilate(eroded,element)
		skel = cv2.bitwise_or(skel,temp)
		img = eroded.copy()

		zeros = size - cv2.countNonZero(img)
		if zeros == size:
			done = True
	plt.imshow(skel,cmap = 'gray')
	plt.show()
	#cv2.imshow("skel",skel)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

create_image(URL)
edge_detection('./temp/temp.png')
erode_and_dilate('./temp/temp1.png')