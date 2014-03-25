import os
import subprocess
import sys

PATH = "/Users/quake0day/wholedavis3rd_video_short_2"
splitScript = "cv.py"
path = os.listdir(PATH)
for dirs in os.walk(PATH):
	for item in dirs:
		try:
			if item[0].split(".")[1] == 'mp4':
				#print dirs[0]
				#print item[0]
				path_for_mp4 = dirs[0]+"/"+ item[0]
				#print path_for_mp4
				command = ['python',splitScript, dirs[0], item[0]]
				print command
				process = subprocess.Popen(command, stdout=subprocess.PIPE)
				out, err = process.communicate()
				print out
		except:
			pass