#-*- encoding: utf-8 -*-
'''
Created on 2014-03-16 16:45:45

@author: quake0day
'''

import os
import subprocess
import sys
import cv2
from PIL import Image
import imagehash
from feature_extract import get_image, get_image_features
# Using Bag of words matching 
import find_image
import random
import time
# final_match_list = []
global final_match_list
final_match_list = []

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
imageSets2_3 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_3"
imageSets2_4 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_4"
imageSets2_5 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_5"
imageSets2_6 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_6"
imageSets2_7 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_7"
imageSets2_8 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_8"
imageSets2_9 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_9"
imageSets2_11 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_11"
imageSets2_12 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12"
imageSets2_14 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_14"
imageSets2_16 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_16"
imageSets2_17 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_17"
imageSets2_18 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18"
imageSets2_20 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20"
imageSets2_21 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21"
imageSets2_23 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23"
imageSets2_24 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24"
imageSets2_26 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_26"
imageSets2_27 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_27"
imageSets2_28 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28"
imageSets2_29 = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_29"


# imageSets = []
# PATH = "/Users/quake0day/wholedavis3rd_video_short_2_b/path2_"
# totaltrace = sys.argv[2] 
# while t <= totaltrace:
#     r = random.randint(0,68) 
#     imageSets.append(PATH+str(r))
#     t += 1
# image = "./frame395.jpg"
# print imageSets

def imageQuality(image):
    return True


def matching2Trace(newTrace, oldTrace):
    if newTrace == oldTrace:
        print "CANNOT MATCH THE SAME TRACE"
        return 0

    sliding_window = 1
    match_list = []
    image_hash = {}
    for fileitem in os.listdir(newTrace):
        try:
            if fileitem.split(".")[1] == 'jpg':
                hash_res = imagehash.average_hash(Image.open(newTrace+"/"+fileitem))
                image_hash[hash_res] = newTrace+"/"+fileitem
        except:
            pass
        #print image_hash
    image_hash_old = {}
    hash_old = []
    for fileitem in os.listdir(oldTrace):
        try:
            if fileitem.split(".")[1] == 'jpg':
                hash_res = imagehash.average_hash(Image.open(oldTrace+"/"+fileitem))
                image_hash_old[hash_res] = oldTrace+"/"+fileitem
                hash_old.append(hash_res)
        except:
            pass
    for item in image_hash.keys():
        if len(match_list) == 0:
            match_list.append(item)
        else:
            if item - match_list[-1] > 15:
                match_list.append(item)
            else:
                pass
    #print len(match_list)
    #for item in match_list:
        #slim_trace.append(image_hash[item])
    i = 0
    dis = 0
    while i < len(match_list):
        j = 0
        while j < len(image_hash_old):
            k = 0
            while k < sliding_window:
                try:
                    dis += match_list[i+k] - hash_old[j+k]
                except:
                    pass
                k += 1    
            j += 1
            if dis <= 15 * sliding_window:
                #print image_hash[match_list[i]],image_hash_old[hash_old[j]]
                #image = get_image(image_hash[match_list[i]])
                #image = cv2.resize(image, (600, 318))
                #keypoints, descriptors = get_image_features(image)
                #if len(descriptors) > 300:
                final_match_list.append([image_hash[match_list[i]],image_hash_old[hash_old[j]]])
                  #  print "BINGO"
                #else:
                    #del image_hash[match_list[i]]
                 #   del match_list[i]
            dis = 0
            #print "J",str(j)
        i += sliding_window
        #print "I",str(i)
    # for item_new in match_list:
    #     for hash_old in image_hash_old:
    #         if item_new - hash_old < 15:
    #             score+=1
    #print score

        #matching2Trace(item2, item)
#matching2Trace(imageSets2_3, imageSets2_5)


def doubleCheck(final_match_list):
    to_match = []
    target = []
    for item in final_match_list:
        to_match.append(item[0])
        target.append(item[1])
    to_match = list(set(to_match))
    target = list(set(target))
    return to_match, target



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
    #   else:
    #       i = i + 1

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
if __name__=="__main__":
    
    imageSets = []
    tomatch = sys.argv[1]
    targets = ['/Users/quake0day/wholedavis3rd_video_short_2_b/path2_50', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_38', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_42', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_34', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_53', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_54', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_40', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_41', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_52', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_48', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_28', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_22', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_59', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_27', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_13', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_45', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_44', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_25', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_8', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_43', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_2', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_17', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_49', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_39', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_33', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_6', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_19', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_15', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_24', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_30', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_18', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_64', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_16', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_20', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_10', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_4', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_21', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_51', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_0', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_65', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_7', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_66', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_61', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_23', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_47', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_12', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_35', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_14', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_46', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_56', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_9', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_57', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_62', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_36', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_37', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_67', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_63', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_55', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_29', '/Users/quake0day/wholedavis3rd_video_short_2_b/path2_60']
    start_time = time.time()
    

    for target in targets:
        matching2Trace(tomatch,target)
    #print final_match_list

    if len(final_match_list) != 0:
            to_match, target = doubleCheck(final_match_list)
            filelists = target
            try:
                flann_matcher = find_image.train_index_new(filelists)
                if to_match != None:
                    for item in to_match:
                        res = find_image.match_image(flann_matcher, item)
                        if res == 0:
                            print "ORIGNAL:",item
            except:
                pass

    print "Total Time:", (time.time() - start_time), "s."




    #print "OpenCV Demo, OpenCV version " + cv2.__version__

    
    #flann_matcher = train_index()
    # ======================== Training done, image matching here ===============

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
#matchingImages(image, imageSets25)
#matchingImages(image, imageSets26)

