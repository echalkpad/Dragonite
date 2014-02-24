#import readrecordfile as Base
import datetime

class ReadAccFile():
	# Read accelerate log file

	def __init__(self, fileName=''):
		#Base.readrecordfile.__init__(self, fileName)
		self.lineNum = 0
		self.time = 0
		self.dt = 0
		self.data = open(fileName).read().split()
		self.totalLine = len(self.data)
		print self.totalLine


	def __parseLine(self, lineNum):
		parsedData = self.data[lineNum].split(",")
		self.time_pre = self.time
		self.time = int(parsedData[0])
		if(self.lineNum == 0):
			self.dt = 0
		else:
			self.dt = int(self.time) - int(self.time_pre)
		self.accType = int(parsedData[1])
		self.accX = float(parsedData[2])
		self.accY = float(parsedData[3])
		self.accZ = float(parsedData[4])

	def ReadNextLine(self):
		if self.lineNum < self.totalLine:
			ret = True
		if ret:
			self.__parseLine(self.lineNum)
			self.lineNum = self.lineNum + 1
		return ret

	def parseLine(self):
		print self.data



if __name__=="__main__":
	a = ReadAccFile("./data/Linear_Acceleration_18_Feb_2014_14-53-07_GMT.txt")
	a.ReadNextLine()
	print(a.time)
	print(a.accZ)
	a.ReadNextLine()
	print(a.time)
	print(a.accZ)