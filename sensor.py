import numpy as np
import matplotlib.pyplot as plt
import ReadAccFile as raf
import ReadCompassFile as rcf
import PlotTrace as pt
accFile = "./data/Linear_Acceleration_18_Feb_2014_14-53-07_GMT.txt"
compassFile = "./data/Orientation_18_Feb_2014_14-53-07_GMT.txt"

def returnMatrix(accFile):
	a = raf.ReadAccFile(accFile)
	a.ReadNextLine()
	a.ReadNextLine()
	print(a.time)
	print(a.dt)
	a.ReadNextLine()
	print(a.dt)


def prepareMatrix(compassFile):
	a = rcf.ReadCompassFile(compassFile)
	angle = []
	while a.ReadNextLine():
		print a.azimuth
		angle.append(a.azimuth)
	#y = np.array(angle)
	M = pt.calNewPosMatrix([0,0],[1]*len(angle),angle,True)
	print "HI"
	pt.plotTraceM(M)

#returnMatrix(accFile)

prepareMatrix(compassFile)