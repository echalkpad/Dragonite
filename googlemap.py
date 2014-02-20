import urllib2
import cv2
import numpy as numpy
from matplotlib import pyplot as plt

URL="http://maps.google.com/maps/api/staticmap?center=43.0027342,-78.78751&zoom=19&size=2000x2000&sensor=true"
def create_image(url):
	f = urllib2.urlopen(url)
	img = open("./temp/temp.png",'w')
	print "writing image to file..."
	img.write(f.read())


def edge_detection(image):
	img = cv2.imread(image,0)
	edges = cv2.Canny(img,10,10)
	#plt.subplot(122)
	plt.imshow(edges,cmap = 'gray')
	plt.show()

create_image(URL)
edge_detection('./temp/temp.png')