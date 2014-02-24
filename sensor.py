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
	time = []
	length = []
	angle = []
	while a.ReadNextLine():
		angle.append(a.azimuth)
	y = np.array(angle)
	z = np.diff(y)
	#x = np.random.random_integers(2,size=(len(z)))
	a = [0]
	b = [0]
	i = 0
	x = 0
	y = 0
	for dire in z:
		if i >= 10:
			try:
				x,y = pt.calNewPos([x+0,y+0],10,dire,True)
				#print x,y
				a.append(x)
				b.append(y)
			except:
				pass
			i = 0
		i = i + 1
	a = np.array(a)
	b = np.array(b)
	
	pt.plotTrace(a,b)

#returnMatrix(accFile)

prepareMatrix(compassFile)