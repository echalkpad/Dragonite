#!/usr/bin/python

import matplotlib.pyplot as plt
import numpy as np
import random
import Position as Pos
import math

# Align direction to one of the domination axis
def regulationDirection(direction, domination_axis):
    return direction

def generateTrace(initialPos, speed, time, direction, regulation=True):
    if regulation is True:
        direction = regulationDirection(direction,[0,0])
    newPostion = Pos.Position(0,0)
    newPostion.x = initialPos[0] + speed*time * math.cos(direction)
    newPostion.y = initialPos[1]+ speed*time * math.sin(direction)
    newPostion.Show()
generateTrace([0,0],10,2,90,True)
x = np.linspace(0, 2*np.pi, 20)
y = np.sin(x)
#print y
y = np.random.random_integers(20,size=(20.))
#print y
    
def plotTrace(x, y):
    # len x shold equal to len y
    assert len(x) == len(y)
    plt.figure()
    plt.quiver(x[:-1], y[:-1], x[1:]-x[:-1], y[1:]-y[:-1], scale_units='xy', angles='xy', scale=1)

    plt.show()


#plotTrace(x,y)