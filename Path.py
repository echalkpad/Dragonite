class Path():

	def __init__(self, id, path, images):
		self.id = id
		self.path = path
		self.image = images

	def getLength(self):
		return 0.5 * len(self.path)



	def getImage(self,segmentID):
		for image in self.image:
			if image.values()[0] == segmentID:
				print image
		return 0



if __name__=="__main__":
	path1 = Path(1, [None,None,None,None,None,None,None,None,None,[2,None]],[{'111011.jpg': 1},{'111011.jpg': 2}])
	path1.getImage(2)
