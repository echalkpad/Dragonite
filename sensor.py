#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2014-02-25 15:10:34

@author: quake0day
'''

import ReadAccFile as raf
import ReadCompassFile as rcf
import PlotTrace as pt
import Position as Pos
import mahattan as ma
accFile = "./data/Corrected_Gyroscope_Sensor_24_Feb_2014_15-52-21_GMT.txt"
compassFile = "/Users/quake0day/trace/wholedavis3rd_video_short_2/15_Mar_2014_21-07-51_GMT/data/MPL_Orientation_15_Mar_2014_21-07-51_GMT.txt"

def returnMatrix(accFile):
	a = raf.ReadAccFile(accFile)
	foo = []
	while a.ReadNextLine():
		foo.append([a.time, a.accMix])
	pt.plotTraceL(foo)
	#print(a.dt)

#calNewPos(initialPos, length, direction, regulation=True)
def prepareMatrix(compassFile):
	a = rcf.ReadCompassFile(compassFile)
	angle = []
	while a.ReadNextLine():
		#print a.azimuth
		angle.append(a.azimuth)
	#y = np.array(angle)
	initialPos = Pos.Position(0,0)
	#ma.calNewPos(initialPos, length, direction)
	M = ma.calNewPosMatrix(initialPos,[1]*len(angle),angle,True)
	pt.plotTraceM(M)

returnMatrix(accFile)

#prepareMatrix(compassFile)