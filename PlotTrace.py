#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import Position as Pos
import math

# Align direction to one of the domination axis
def regulationDirection(direction, domination_axis):
    return direction

# initial position
# moving speed
# time
# direction in dgree
# align to dominant axis?
def calNewPos(initialPos, speed, time, direction, regulation=True):
    if regulation is True:
        direction = regulationDirection(direction,[0,0])
    newPostion = Pos.Position(0,0)
    newPostion.x = initialPos[0] + speed*time * math.cos(math.radians(direction))
    newPostion.y = initialPos[1]+ speed*time * math.sin(math.radians(direction))
    newPostion.Show()

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
    im = plt.imread("./temp/temp.png")
    im[:, :, -1] = .8
    implot = plt.imshow(im)
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)
    plt.show()


plotTrace(x,y)