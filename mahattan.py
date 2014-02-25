#!/usr/bin/python
#-*- encoding: utf-8 -*-
'''
Created on 2014-02-25 15:10:10

@author: quake0day
'''

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