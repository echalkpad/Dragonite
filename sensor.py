import numpy as np
import matplotlib.pyplot as plt
import ReadAccFile as raf

a = raf.ReadAccFile("./data/Linear_Acceleration_18_Feb_2014_14-53-07_GMT.txt")
a.ReadNextLine()
print(a.time)
