#!/usr/bin/env python
import os
import subprocess
from sklearn import svm
import numpy as np
import pylab as pl

BINS = [0.5, 1.0, 1.5, 2.0]
FLOW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build/flow')

def find_bin(val):
    values = map(lambda x: abs(x - val), BINS)
    a = float('Inf')
    index = -1
    for i in xrange(len(values)):
        if values[i] < a:
            a = values[i]
            index = i

    return index


def run_flow(i1, i2):
    p = subprocess.Popen([FLOW, i1, i2], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, _ = p.communicate()
    cnt = 0.00001
    dx = 0.0
    dy = 0.0
    for l in out.split('\n'):
        if (l):
            cnt += 1
            p1, p2 = eval(l)
            dx += abs(p2[0] - p1[0])
            dy += abs(p2[1] - p1[1])

    return [dx / cnt, dy / cnt], (cnt >= 1)


def calc_flow_dir(dir):
    X = []
    Y = []
    fi = open(dir + '/measure')
    img = dir + '/img'
    distance = float(fi.readline())
    dirlist = sorted(os.listdir(img))
    last_img = dirlist[-1]
    first_img = dirlist[0]
    dtime = long(last_img[:-4]) - long(first_img[:-4])
    speed = distance / dtime * 1000
    prev_img = dirlist[0]
#    print "Speed: " + str(speed)
    for cur_img in dirlist[1:]:
        print "Flow of: " + prev_img + ' ' + cur_img
        avg, found = run_flow(img + '/' + prev_img, img + '/' + cur_img)
        if (found):
            print "  avg: " + str(avg) + " class: " + str(find_bin(speed))
            X += [avg]
            Y += [find_bin(speed)]
        prev_img = cur_img

    return X, Y


def collect_data(root):
    dirs = sorted(os.listdir(root))
    X = []
    Y = []
    for d in dirs:
        cur_dir = os.path.join(root, d)
        print "In dir: " + cur_dir
        cx, cy = calc_flow_dir(cur_dir)
        X += cx
        Y += cy

    return X, Y


trainX, trainY = collect_data('/home/bruce/Works/Research/3D/open3d/Dragonite/speed/data/train')
print "========== Collect Test ========="
testX, testY = collect_data('/home/bruce/Works/Research/3D/open3d/Dragonite/speed/data/test')

C = 1.0
clf = svm.SVC()
clf.fit(trainX, trainY)

outY = clf.predict(testX)

XAr = np.array(trainX)
YAr = np.array(trainY)

pl.scatter(XAr[:, 0], XAr[:, 1], c=YAr)
pl.show()
print trainX
print trainY

print "==== output ===="
print testY
print outY
