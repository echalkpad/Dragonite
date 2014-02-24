#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import Position as Pos
import math

# Align direction to one of the domination axis
def regulationDirection(direction, domination_axis):
    print math.radians(direction)
    """if direction > 1:
        print direction
    if direction < 45:
        direction = 0
    elif direction >= 45 and direction <= 135:
        direction = 90
    elif direction > 135:
        direction = -90
        """
    return direction

# initial position
# moving speed
# time
# direction in dgree
# align to dominant axis?
def calNewPos(initialPos, length, direction, regulation=True):
    if regulation is True:
        direction = regulationDirection(direction,[0,0])
    newPostion = Pos.Position(0,0)
    newPostion.x = initialPos[0] + length * math.cos(math.radians(direction))
    newPostion.y = initialPos[1]+ length * math.sin(math.radians(direction))
    #newPostion.Show()
    return newPostion.x, newPostion.y

def calNewPosMatrix(initialPos, length_M, direction_M, regulation=True):
    assert len(length_M) == len(direction_M)
    # cal the difference between the previous direction and current direction
    #direction_diff_M = np.diff(np.array(direction_M))
    #print direction_diff_M
    i = 0
    PosMatrix = []
    PosMatrix.append(initialPos)
    pre_Position = initialPos
    while i < len(length_M):
        x,y = calNewPos(pre_Position, length_M[i], direction_M[i], regulation)
        i = i + 1
        PosMatrix.append([x,y])
        pre_Position = [x,y]
    print PosMatrix
    return PosMatrix




aa = [1,1,1,1]
bb = [0,0,90,180]
calNewPosMatrix([0,0], aa, bb, True)
#calNewPos([0,0],10,2,180,True)
x = np.linspace(0, 2*np.pi*np.random.random_integers(100), 100)
y = np.sin(x)
#print y
y = np.random.random_integers(600,size=(100.))
#print y


    
def plotTrace(x, y):
    # len x shold equal to len y
    assert len(x) == len(y)
    plt.figure()
    #im = plt.imread("./temp/temp.png")
    #im[:, :, -1] = .8
    #implot = plt.imshow(im)
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)
    #plt.xlim([0,2])
    #plt.ylim([-0.1,0.1])
    #plt.plot(x,y)
    plt.show()

def plotTraceM(Pos):
    x = []
    y = []
    for item in Pos:
        print item
        x.append(item[0])
        y.append(item[1])
    assert len(x)  == len(y)
    x = np.array(x)
    y = np.array(y)
    plotTrace(x,y)

#plotTrace(x,y)