#!/usr/bin/env python
import os
import subprocess
from sklearn import svm
import numpy as np
import pylab as pl

BINS = [0.70, 1.5]
FLOW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build/flow')

# def find_bin(val):
#     values = map(lambda x: abs(x - val), BINS)
#     a = float('Inf')
#     index = -1
#     for i in xrange(len(values)):
#         if values[i] < a:
#             a = values[i]
#             index = i

#     return index

def find_bin(val):
    for i in xrange(len(BINS)):
        if val < BINS[i]:
            index = i
            break

    return index


def run_flow(i1, i2):
    p = subprocess.Popen([FLOW, i1, i2], stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE)
    out, _ = p.communicate()
    cnt = 0.00001
    dx = 0.0
    dy = 0.0
    max_x = 0.00001
    max_y = 0.00001
    min_x = float('Inf')
    min_y = float('Inf')
    for l in out.split('\n'):
        if (l):
            cnt += 1
            p1, p2 = eval(l)
            ddx = abs(p2[0] - p1[0])
            ddy = abs(p2[1] - p1[1])

            if (ddx > max_x):
                max_x = ddx
            else:
                if (ddx < min_x):
                    min_x = ddx

            if (ddy > max_y):
                max_y = ddy
            else:
                if (ddy < min_y):
                    min_y = ddy

            dx += ddx
            dy += ddy

    return [dx / cnt / (max_x-min_x), dy / cnt / (max_y-min_y)], (cnt >= 3)


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
#        print "Flow of: " + prev_img + ' ' + cur_img
        avg, found = run_flow(img + '/' + prev_img, img + '/' + cur_img)
        if (found):
#            print "  avg: " + str(avg) + " class: " + str(find_bin(speed))
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


def train_svm(root):
    trainX, trainY = collect_data(root)
    clf = svm.SVC(kernel='rbf', C=100.0)
    clf.fit(trainX, trainY)
    return clf


def classify(s, i1, i2):
    vec, have_flow = run_flow(i1, i2)
    if (have_flow):
        return s.predict([vec])[0]

    return False


if __name__ == "__main__":
    # BEGIN Example
    clf = train_svm('/home/muyuan/Programming/projects/Open3D/Dragonite/speed/data/train')
    print "==== Single Test ===="
    print classify(clf, "/home/muyuan/Programming/projects/Open3D/Dragonite/speed/data/test/9_Mar_2014_20-15-12_GMT/img/1394396123635.jpg",
                   "/home/muyuan/Programming/projects/Open3D/Dragonite/speed/data/test/9_Mar_2014_20-15-12_GMT/img/1394396125120.jpg")
    # END Example

    print "========== Collect Test ========="
    testX, testY = collect_data('/home/muyuan/Programming/projects/Open3D/Dragonite/speed/data/test')

    outY = clf.predict(testX)

    XAr = np.array(testX)
    YAr = np.array(testY)

    h = .02
    x_min, x_max = XAr[:, 0].min() - 1, XAr[:, 0].max() + 1
    y_min, y_max = XAr[:, 1].min() - 1, XAr[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    print "Shape: "
    print xx.shape
    print outY.shape
    print "======="
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.scatter(XAr[:, 0], XAr[:, 1], c=YAr, cmap=pl.cm.Paired)
    pl.show()
    # print trainX
    # print trainY

    print "==== output ===="
    print YAr
    print outY
