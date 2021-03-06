#-*- encoding: utf-8 -*-
'''
Created on 2014-03-09 16:34:15

@author: quake0day
'''

# trace1 = {
#     'id' : [1,2,3],
#     'connection': {
#         1: [None,None,None,None,None,None,None,None,None,[2,None]],
#         2: [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[3,None]],
#         3: [None,None,None,None,None,None,None,None,None,],
#     },
#     'image':{'111011.jpg': [1,1], '22.jpg': [2,2], '23.jpg': [2,3],'112j121233.jpg':[3,4]},
# }
import Path as Path
class Trace():

	def __init__(self, paths):
		self.id = []
		self.connection = {}
		self.paths = paths
		self.image = {}
		for path in self.paths:
			self.id.append(path.id)
			self.connection[path.id] = path.path
			for image in path.image:
				# print "PATHIMAGE"
				# print image
				self.image[image.keys()[0]] = [path.id, image.values()[0]]
		# print self.connection
		# print self.id
		# print self.image
	def getImagePos(self,imageName):
		return self.image[imageName]

	# Only return list **NOT** PATH
	def getPath(self, pathID):
		return self.connection[pathID]

	def getLength(self, pathID):
		offset = self.id.index(pathID)
		return self.paths[offset].getLength()

	# Given changelist = [a,b] 
	# Change ID from b to a
	# Use for changing "id" and "image" for a certain trace after merge
	def changeID(self, ChangeList):
		for changeSeed in ChangeList:
			for imageKeyValue in self.image.iteritems():
				print imageKeyValue
				if imageKeyValue[1][0] == changeSeed[1]:
					self.image[imageKeyValue[0]] = [changeSeed[0], imageKeyValue[1][1]]
					#self.image[]
			for singleID in self.id:
				if singleID == changeSeed[1]:
					self.id.remove(singleID)
					self.id.append(changeSeed[0])
		return 0

	# def getPathID(self):
	# 	for path in self.paths:
	# 		print path.id

if __name__=="__main__":
    path1 = Path.Path(1, [None,None,None,None,None,None,None,None,None,[2,None]],[{'1110111.jpg': 1},{'1110211.jpg': 2}])
    path2 = Path.Path(2, [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[3,None]],[{'11123011.jpg': 1},{'111121011.jpg': 2}])
    path3 = Path.Path(3, [None,None,None,None,None,None,None,None,None],[{'111323011.jpg': 1},{'111013243241.jpg': 2}])
    path4 = Path.Path(4, [None,None,None,None,None,None,None,[5,None]],[{'111011.jpg': 1},{'111011.jpg': 2}])
    path5 = Path.Path(5, [None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,[6,None]],[{'111011.jpg': 1},{'111011.jpg': 2}])
    path6 = Path.Path(6, [None,None,None,None,None,None,None,None,None,None,None,None],[{'111011.jpg': 1},{'111011.jpg': 2}])
    #print path3.getLength()
    trace1 = Trace([path1,path2,path3])
    #print trace1.getImagePos('1110111.jpg')
    #print trace1.getLength(1)
    changeList = [[4,3]]
    print trace1.changeID(changeList)
    print trace1.image.values()
    print trace1.id
