#!/usr/bin/python

class Position():
	# Define postion class

	def __init__(self, x, y):
		self.x = x
		self.y = y
	def x(self, x):
		self.x = x
	def y(self, y):
		self.y = y
	# return y
	def getX(self):
		return float(self.x)
	# return x
	def getY(self):
		return float(self.y)

	def Show(self):
		print self.x,self.y
