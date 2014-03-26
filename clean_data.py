import os
import subprocess
import sys
from PIL import Image
import imagehash 
t = 0
imageSets = []
PATH = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_"
while t <= 45:
    imageSets.append(PATH+str(t))
    t += 1
#newTrace = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5"
def clean_set(newTrace):
	match_list = []
	image_hash = {}
	for fileitem in os.listdir(newTrace):
	    try:
	        if fileitem.split(".")[1] == 'jpg':
	            hash_res = imagehash.average_hash(Image.open(newTrace+"/"+fileitem))
	            image_hash[hash_res] = newTrace+"/"+fileitem
	        else:
	        	os.remove(newTrace+"/"+fileitem)
	    except:
	        pass

	for item in image_hash.keys():
	    if len(match_list) == 0:
	        match_list.append(item)
	    else:
	        if item - match_list[-1] > 65:
	            match_list.append(item)
	        else:
	            os.remove(image_hash[item])
for item in imageSets:
    clean_set(item)