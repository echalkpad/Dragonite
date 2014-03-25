#-*- encoding: utf-8 -*-
'''
Created on 2014-03-16 16:45:45

@author: quake0day
'''

import os
import subprocess
import sys
from PIL import Image
import imagehash

matchProgram = "/Users/quake0day/Dragonite/contour/match"
imageSets = "/Users/quake0day/new/wholedavis3rd_short_1/path1_1/"
imageSets1 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_2/"
imageSets2 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_3/"
imageSets3 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_4/"
imageSets4 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_5/"
imageSets5 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_6/"
imageSets6 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_7/"
imageSets7 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_8/"
imageSets8 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_9/"
imageSets9 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_10/"
imageSets10 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_11/"
imageSets11 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_12/"
imageSets12 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_13/"
imageSets13 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_14/"
imageSets14 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_15/"
imageSets15 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_16/"
imageSets16 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_17/"
imageSets17 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_18/"
imageSets18 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_19/"
imageSets19 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_20/"
imageSets20 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_21/"
imageSets21 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_22/"
imageSets22 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_23/"
imageSets23 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_24/"
imageSets24 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_25/"
imageSets25 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_26/"
imageSets26 = "/Users/quake0day/new/wholedavis3rd_short_1/path1_27/"

image = "./frame395.jpg"
def matchingImages(image, imageSets):
	match_list = []
	for fileitem in os.listdir(imageSets):
		try:
			if fileitem.split(".")[1] == 'jpg':
				match_list.append(fileitem)
		except:
			pass
	res = 0
	hash_res1 = imagehash.average_hash(Image.open(image))
	for item in match_list:
		try:
			hash_res2 = imagehash.average_hash(Image.open(imageSets+item))
			try:
				if (hash_res1 - hash_res2) <= 15:
					print  hash_res1 - hash_res2
					res+=1
					res += match2Image(image, imageSets+item)
			except:
				pass
		except:
			pass
	print "TOTAL MATCH IN" + imageSets
	print res
	#	else:
	#		i = i + 1

def match2Image(image1, image2):
	#command = matchProgram + " " + image1 + " " + image2
	command = [matchProgram, image1, image2]
	process = subprocess.Popen(command, stdout=subprocess.PIPE)
	out, err = process.communicate()
	print image1,image2
	res = out.split(" ")
	GoodMatch = 0
	if len(res) == 3:
		image1_features = int(res[1])
		image2_features = int(res[2])
		match_features = int(res[0])
		if min(image1_features,image2_features) > 1000:
			if match_features > min(image1_features,image2_features)*0.45:
				if match_features > 2400:
					print image1_features, image2_features, match_features
					print "Good Match!"
					return 1
	return 0


# matchingImages(image, imageSets)
# matchingImages(image, imageSets1)
# matchingImages(image, imageSets2)
# matchingImages(image, imageSets3)
# matchingImages(image, imageSets4)
# matchingImages(image, imageSets5)
# matchingImages(image, imageSets6)
# matchingImages(image, imageSets7)
# matchingImages(image, imageSets8)
# matchingImages(image, imageSets9)
# matchingImages(image, imageSets10)
# matchingImages(image, imageSets11)
# matchingImages(image, imageSets12)
# matchingImages(image, imageSets13)
# matchingImages(image, imageSets14)
# matchingImages(image, imageSets15)
# matchingImages(image, imageSets16)
# matchingImages(image, imageSets17)
# matchingImages(image, imageSets18)
# matchingImages(image, imageSets19)
# matchingImages(image, imageSets20)
# matchingImages(image, imageSets21)
# matchingImages(image, imageSets22)
# matchingImages(image, imageSets23)
# matchingImages(image, imageSets24)
matchingImages(image, imageSets25)
#matchingImages(image, imageSets26)

