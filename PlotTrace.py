#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import Position as Pos
import math

# Align direction to one of the domination axis 
# based on manhattan assumption
def regulationDirection(direction, domination_axis):
    #print direction
    assert(direction <= 360 and direction >= 0)
    if direction < 45 or direction > 315:
        direction = 0+domination_axis
    elif direction >= 45 and direction <= 135:
        direction = 90+domination_axis
    elif direction > 135 and direction <= 225:
        direction = 180+domination_axis
    elif direction > 225 and direction <= 315:
        direction = 270+domination_axis
    return direction

# Input 
# initial position -- [Pos.x Pos.y]
# Length
# direction in dgree
# align to dominant axis?
def calNewPos(initialPos, length, direction, regulation=True):
    if regulation is True:
        direction = regulationDirection(direction,45)
    newPostion = Pos.Position(0,0)
    newPostion.x = initialPos.x + length * math.cos(math.radians(direction))
    newPostion.y = initialPos.y + length * math.sin(math.radians(direction))
    #newPostion.Show()
    return newPostion

# calculate a matrix for all x,y points in a path
def calNewPosMatrix(initialPos, length_M, direction_M, regulation=True):
    assert len(length_M) == len(direction_M)
    # cal the difference between the previous direction and current direction
    #direction_diff_M = np.diff(np.array(direction_M))
    PosMatrix = [initialPos]
    pre_Position = initialPos
    for length,direction in zip(length_M,direction_M):
        newPos = calNewPos(pre_Position, length, direction, regulation)
        PosMatrix.append(newPos)
        pre_Position = newPos
    return PosMatrix

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
        x.append(item.getX())
        y.append(item.getY())
    assert len(x)  == len(y)
    x = np.array(x)
    y = np.array(y)
    plotTrace(x,y)


# just for test
if __name__=="__main__":
    newPostion = Pos.Position(0,0)
    aa = [1,1,1,1]
    bb = [0,0,90,180]
    calNewPosMatrix(newPostion, aa, bb, True)
    #calNewPos([0,0],10,2,180,True)
    x = np.linspace(0, 2*np.pi*np.random.random_integers(100), 100)
    y = np.sin(x)
    #print y
    y = np.random.random_integers(600,size=(100.))
