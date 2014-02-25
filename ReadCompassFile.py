#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2014-02-25 15:10:21

@author: quake0day
'''

#import readrecordfile as Base
import datetime

class ReadCompassFile():
	# Read accelerate log file

	def __init__(self, fileName=''):
		#Base.readrecordfile.__init__(self, fileName)
		self.lineNum = 0
		self.data = open(fileName).read().split()
		self.totalLine = len(self.data)
		print self.totalLine


	def __parseLine(self, lineNum):
		parsedData = self.data[lineNum].split(",")
		self.time = parsedData[0]
		self.compassType = int(parsedData[1])
		self.azimuth = float(parsedData[2])
		self.pitch = float(parsedData[3])
		self.roll = float(parsedData[4])


	def ReadNextLine(self):
		if self.lineNum < self.totalLine:
			ret = True
		else:
			ret = False
		if ret:
			self.__parseLine(self.lineNum)
			self.lineNum = self.lineNum + 1
		return ret


if __name__=="__main__":
	a = ReadCompassFile("./data/Orientation_18_Feb_2014_14-53-07_GMT.txt")
	a.ReadNextLine()
	print(a.time)
	print(a.azimuth)
	a.ReadNextLine()
	print(a.time)
	print(a.azimuth)