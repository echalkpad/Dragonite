#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2014-02-25 15:10:14

@author: quake0day
'''

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
