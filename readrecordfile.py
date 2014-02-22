import datetime as dt

class readrecordfile:
	# use for generally read log file
	def __init__(self, fileName=""):
		self.__filename = fileName
		self.__file = open(self.__filename)
		print "HE"

	def getFileName(self):
		return self.__filename

	def ReadNextLine(self):
		self._readBuffer = self.__file.readline()
		if not self.__readBuffer:
			return False
		else:
			return True

	def __strToDateTime(self, strTime="1392735233834998030"):
		return strTime

	def __del__(self):
		if self.__file.closed != True:
			self.__file.close()


if __name__=="__main__":
	print ("hi")