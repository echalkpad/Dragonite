import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import prettyplotlib
import csv 

datafile = csv.reader(open('./graph_sensys.csv', 'rU'), dialect=csv.excel_tab)

print ('loading %s' % datafile)
for row in datafile:
    print row
r = mlab.csv2rec('./graph_sensys.csv')
r.sort()
print r
# first we'll do it the default way, with gaps on weekends
fig, ax = plt.subplots()
#ax.set_autoscaley_on(False)
#ax.set_ylim([1000,10000000])
# ax.set_yscale('log')
ax.plot(r.red, r.wifi, 'o-', label="Sift (CPU)")
ax.plot(r.red, r.nowifi, 'o-', label="Sift (GPU) DIMM 2048")
# ax.plot(r.pixel, r.siftgpu3200, 'o-', label="Sift (GPU) DIMM 3200")
# ax.plot(r.pixel, r.siftgpu4096, 'o-', label="Sift (GPU) DIMM 4096")
# # create a legend for the contour set
# handles, labels = ax.get_legend_handles_labels()
# print labels
# #fig.autofmt_ydate()
# ax.legend(handles, labels, loc=2)
# plt.xlabel("Number of Pixels (log(N))")
# plt.ylabel("Exectution time(s)", labelpad=20)
# plt.title("Number of pixels vs execution time for SIFT")

plt.show()
