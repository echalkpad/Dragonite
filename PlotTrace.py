#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2014-02-25 15:09:58

@author: quake0day
'''

import matplotlib.pyplot as plt
import numpy as np
import Position as Pos
import mahattan as ma

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

def plotTraceL(Pos):
    x = []
    y = []
    for item in Pos:
        x.append(item[0])
        y.append(item[1])
    assert len(x)  == len(y)
    x = np.array(x)
    y = np.array(y)
    plotTrace(x,y)

# just for test
if __name__=="__main__":
    newPostion = Pos.Position(0,0)
    aa = [1,1,1,1]
    bb = [0,0,90,180]
    ma.calNewPosMatrix(newPostion, aa, bb, True)
    #calNewPos([0,0],10,2,180,True)
    x = np.linspace(0, 2*np.pi*np.random.random_integers(100), 100)
    y = np.sin(x)
    #print y
    y = np.random.random_integers(600,size=(100.))
