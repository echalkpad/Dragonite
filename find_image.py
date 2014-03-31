import cv2
import numpy
import os
import collections
import operator
from pprint import pprint
import hashlib
# Used for timing
import time

files = []
matcher = None

def get_image(image_path):
	return cv2.imread(image_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)

def get_image_features(image):
	# Workadound for missing interfaces
	surf = cv2.FeatureDetector_create("SURF")
	surf.setInt("hessianThreshold", 100)
	surf_extractor = cv2.DescriptorExtractor_create("SURF")
	# Get keypoints from image
	keypoints = surf.detect(image, None)
	# Get keypoint descriptors for found keypoints
	keypoints, descriptors = surf_extractor.compute(image, keypoints)
	return keypoints, numpy.array(descriptors)

def train_index_new(filelists):
	# Prepare FLANN matcher
	flann_params = dict(algorithm = 1, trees = 4)
	matcher = cv2.FlannBasedMatcher(flann_params, {})

	# Train FLANN matcher with descriptors of all images
	for f in filelists:
		#print "Processing " + f
		image = get_image(f)
		keypoints, descriptors = get_image_features(image)
		try:
			matcher.add([descriptors])
			files.append(f)
		except:
			pass

	print "Training FLANN."
	matcher.train()
	print "Done."
	return matcher

def train_index():
	# Prepare FLANN matcher
	flann_params = dict(algorithm = 1, trees = 4)
	matcher = cv2.FlannBasedMatcher(flann_params, {})

	# Train FLANN matcher with descriptors of all images
	for f in os.listdir("img/"):
		#print "Processing " + f
		image = get_image("./img/%s" % (f,))
		keypoints, descriptors = get_image_features(image)
		if descriptors != None:
			try:
				matcher.add([descriptors])
				files.append(f)
			except:
				pass

	print "Training FLANN."
	matcher.train()
	print "Done."
	return matcher

def match_image(index, image):
	# Get image descriptors
	image = get_image(image)
	keypoints, descriptors = get_image_features(image)

	# Find 2 closest matches for each descriptor in image
	try:
		matches = index.knnMatch(descriptors, 2)
	except:
		return -1
	
	# Count matcher for each image in training set
	print "Counting matches..."
	count_dict = collections.defaultdict(int)
	for match in matches:
		# Only count as "match" if the two closest matches have big enough distance
		if match[0].distance / match[1].distance < 0.3:
			continue
		image_idx = match[0].imgIdx
		#print image_idx
		count_dict[files[image_idx]] += 1
	
	# Get image with largest count
	matched_image = max(count_dict.iteritems(), key=operator.itemgetter(1))[0]

	# Show results
	#print "Images", files
	#print "Counts: ", count_dict

	print "Hit: ", matched_image
	print "==========="
	return 0

	#return matched_image

if __name__ == "__main__":
	#['/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame130.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame88.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame28.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame47.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame62.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame228.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame155.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame129.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame83.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame39.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame94.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame175.jpg', '/Users/quake0day/wholedavis3rd_video_short_2/path2_3/frame29.jpg']
	filelists = ['/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame121.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3/frame204.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11/frame157.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11/frame115.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame159.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11/frame13.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame127.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame216.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame200.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12/frame101.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame222.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12/frame145.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34/frame16.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_13/frame15.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28/frame61.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame157.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_1/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame144.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame156.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12/frame153.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame2.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12/frame44.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame24.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_27/frame10.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_29/frame131.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame18.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame165.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5/frame107.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame219.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame221.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame226.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame16.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_43/frame48.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame17.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame107.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame334.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame5.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame31.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame180.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame168.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame185.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame37.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_36/frame107.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame195.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_26/frame15.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34/frame235.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame171.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_14/frame163.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3/frame194.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame194.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame26.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame161.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5/frame100.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18/frame19.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_29/frame25.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_33/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame224.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_27/frame115.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_16/frame21.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5/frame151.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_22/frame11.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_17/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame155.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame240.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame166.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame143.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame103.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame147.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_44/frame25.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame10.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame128.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame349.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame6.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame121.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_13/frame162.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame156.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_15/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_1/frame15.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_30/frame13.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame298.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_26/frame126.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame157.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_17/frame216.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame198.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame159.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame107.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28/frame114.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame140.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_30/frame97.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_22/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_30/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18/frame155.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_26/frame135.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame256.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame14.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_14/frame18.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_16/frame141.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame102.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_43/frame20.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame136.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_6/frame113.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_6/frame23.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame164.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame207.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3/frame151.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame148.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame169.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame174.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame145.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame341.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame151.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_33/frame131.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34/frame242.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28/frame160.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame186.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28/frame153.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame156.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_43/frame102.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_43/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_14/frame12.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame167.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame101.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame261.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame142.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame325.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11/frame97.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame50.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18/frame101.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame179.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame166.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_36/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_2/frame122.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame140.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23/frame112.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12/frame4.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame129.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_32/frame210.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame29.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3/frame192.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_16/frame100.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_2/frame1.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame294.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame32.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame353.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame105.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame145.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame157.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11/frame208.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_32/frame58.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame356.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame134.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame187.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame52.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame216.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame126.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame148.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_0/frame16.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5/frame27.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame169.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame15.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34/frame33.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame14.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame160.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame147.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5/frame11.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_26/frame118.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21/frame114.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame174.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame10.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame22.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame141.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_0/frame20.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_30/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_29/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame214.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame135.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3/frame164.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame156.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame230.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25/frame15.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_27/frame7.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10/frame24.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame171.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame213.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame116.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_6/frame105.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_44/frame101.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41/frame181.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_13/frame101.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_32/frame121.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame291.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_4/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40/frame12.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37/frame244.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_13/frame155.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38/frame216.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35/frame197.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_31/frame125.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_36/frame167.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_32/frame191.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42/frame13.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39/frame211.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24/frame232.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_0/frame3.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_4/frame14.jpg', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_44/frame3.jpg']
	print "OpenCV Demo, OpenCV version " + cv2.__version__
	
	start_time = time.time()
	flann_matcher = train_index_new(filelists)
	#flann_matcher = train_index()
	print "\nIndex generation took ", (time.time() - start_time), "s.\n"
	# ======================== Training done, image matching here ===============
	
	start_time = time.time()
	match_image(flann_matcher, "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_9/frame84.jpg")
	print "Matching took", (time.time() - start_time), "s."
