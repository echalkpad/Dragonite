import cv2
import sys

filepath = sys.argv[1]
filename = sys.argv[2]
vidcap = cv2.VideoCapture(filepath+"/"+filename)
success,image = vidcap.read()

count = 0
while success:
    success,image = vidcap.read()
    filename 
    cv2.imwrite(filepath + "/frame%d.jpg" % count,image)
    if cv2.waitKey(10) == 27:
        break
    count +=1
