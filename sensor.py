import numpy as np
import matplotlib.pyplot as plt
import ReadAccFile as raf

accFile = "./data/Linear_Acceleration_18_Feb_2014_14-53-07_GMT.txt"


def returnMatrix(accFile):
	a = raf.ReadAccFile(accFile)
	a.ReadNextLine()
	a.ReadNextLine()
	print(a.time)
	print(a.dt)
	a.ReadNextLine()
	print(a.dt)



returnMatrix(accFile)