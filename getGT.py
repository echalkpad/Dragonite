from PIL import Image
import math
import sys
import collections

# im = Image.open('./gt1.png')
# im2 = Image.open('./gt3.png')
# pix = im.load()
# pix2 = im2.load()
# print im.size

def get_colorMatrix(im, color):
	pix = im.load()
	right_pix = []
	for x in range(im.size[0]):
		for y in range(im.size[1]):
			if pix[x,y] == color:
				right_pix.append([x,y])
	return right_pix

def mergeTwoTrace(image1,image2, newfile, color, offset=0):
	im1 = Image.open(image1)
	im2 = Image.open(image2)
	pix2 = im2.load()
	col = get_colorMatrix(im1, color)
	for item in col:
		pix2[item[0],item[1]] = color
		#im2.putpixel((item[0],item[1]), (26, 143, 255))
	im2.save(newfile)

# based on WiFi data
def check_merge(image1,image2,color):
	im1 = Image.open(image1)
	im2 = Image.open(image2)
	matrix = get_colorMatrix(im1, color)
	matrix2 = get_colorMatrix(im2, color)
	intersection = [val for val in matrix if val in matrix2]
	if len(intersection) > 0:
		return True
	return False

def parseMatchLog(logFile):
	f = open(logFile,'r')
	data = f.read().split('\n')
	hitdata = []
	to_hitdata = []
	match_matrix = []
	for item in data:
		if len(item) != 0:
			if item[0] == 'H' and item[1] == 'i' and item[2] == 't': # find hit
				hitdata.append(item)
			if item[0] == "O" and item [1] == "R" and item[2] == "I":
				to_hitdata.append(item)
	assert len(hitdata) == len(to_hitdata)
	for item in zip(to_hitdata,hitdata):
		match_point = item[0].split("path2_")[1]
		match_point2 = item[1].split("path2_")[1]
		if len(match_point) != 0 and len(match_point2) != 0:
			trace_name1 = match_point.split("/")[0]
			trace_name2 = match_point2.split("/")[0]
			match_matrix.append([trace_name1,trace_name2])

	#print filter(lambda x: match_matrix.count(x) > 1, match_matrix)
	return removeDup(match_matrix)

def removeDup(mylist):
	K = ""
	finallist = []
	for item in mylist:
		K += ".".join(item)
		K += " "
	k1  = K.split(" ")
	deDupList = sorted(set(k1),key=k1.index)
	for item in deDupList:
		newlist = item.split(".")
		if len(newlist) > 1:
			finallist.append(newlist)
	return finallist


def correctness(matrix):
	correct = 0
	for item in matrix:
		if int(item[0]) == int(item[1]) + 1:
			correct +=1
		elif int(item[0]) == int(item[1]) - 1:
			correct +=1
		elif int(item[0]) == int(item[1]) - 2:
			correct +=1
		elif int(item[0]) == int(item[1]) + 2:
			correct +=1
		else:
			pass
	print correct

def check_top(imageList):
	COLOR = (26, 143, 255)
	top = {}
	for imageName in imageList:
		image = imageName.split("/")[2]
		im = Image.open(imageName)
		matrix = get_colorMatrix(im, COLOR)
		top[image] = len(matrix)
	print sorted(top.items(),key = lambda top:top[1],reverse=True)



PATH = "./f85/"
COLOR = (26, 143, 255)
matrix = parseMatchLog('./running_log/tmatch85.log')

#print correctness(matrix)
total_correct = 0
toplist = []

for item in matrix:
	image1 = PATH+str(item[0])+".png"
	image2 = PATH+str(item[1])+".png"
	if check_merge(image1, image2, COLOR) == True:
		total_correct +=1
		#print image1, image2
		mergeTwoTrace(image1,image2, image1, COLOR, offset=0)
		mergeTwoTrace(image1,image2, image2, COLOR, offset=0)
		toplist.append(image1)
		toplist.append(image2)
check_top(toplist)
print len(matrix)
print total_correct
#print toplist

#COLOR = (26, 143, 255)
#print check_merge('./gt1.png', './gt3.png', COLOR)
#mergeTwoTrace('./gt1.png', './gt5.png','./nnn.png', COLOR, 50)
#get_distance('./gt12.png', './gt2.png', COLOR)


