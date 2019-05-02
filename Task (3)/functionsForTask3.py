# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:12:25 2019

@author: manog
"""
import numpy as np


def startUpCycle (magneticVector, phantomSize, flipAngle, exponentialOfT1AndTR, x):
    x = x-1
    if x<0:
        for j in range(phantomSize):
            for k in range(phantomSize):
                magneticVector[j][k][2] = np.cos(flipAngle) + 1 - exponentialOfT1AndTR[j][k]
        startUpCycle (magneticVector, phantomSize, flipAngle, exponentialOfT1AndTR, x)
    else:
        return magneticVector

    
def multiplyingPD_ByMagneticVector (magneticVector, PD, phantomSize, flipAngle, exponentialOfT1AndTR):
    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k] = magneticVector[j][k]**PD[j][k]
            magneticVector[j][k][0] = 0
            magneticVector[j][k][1] = 0
            magneticVector[j][k][2] = np.cos(flipAngle) + 1 - exponentialOfT1AndTR[j][k]
    
    return magneticVector

#############################################################################################
#############################################################################################

def rotationAroundXFunction(phantomSize, flipAngle, magneticVector):
    rotationAroundXMatrix = np.array([[1, 0, 0],
                                      [0, np.cos(flipAngle), np.sin(flipAngle)],
                                      [0, -np.sin(flipAngle), np.cos(flipAngle)]])
    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k] = np.matmul(rotationAroundXMatrix, magneticVector[j][k])
            
    return magneticVector

#############################################################################################
#############################################################################################
    
def rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector):
    for j in range(phantomSize):
        for k in range(phantomSize):
            rotateX = np.array([[np.cos(gxStep*j), np.sin(gxStep*j), 0],
                                [-np.sin(gxStep*j), np.cos(gxStep*j), 0],
                                [0, 0, 1]])
            rotateY = np.array([[np.cos(gyStep*k), np.sin(gyStep*k), 0],
                                [-np.sin(gyStep*k), np.cos(gyStep*k), 0],
                                [0, 0, 1]])
            magneticVector[j][k] = np.matmul(rotateX, magneticVector[j][k])
            magneticVector[j][k] = np.matmul(rotateY, magneticVector[j][k])

            
    return magneticVector

#############################################################################################
#############################################################################################

def lookUpForDecay(phantomSize,T1,T2,TE,TR,exponentialOfT1AndTR,exponentialOfT1AndTE,exponentialOfT2AndTE,decayMatrices):
    
    
    epsilon = np.finfo(np.float32).eps
    
    for j in range(phantomSize):
        for k in range(phantomSize):
            if T2[j][k]==0:
                T2[j][k] = epsilon
            if T1[j][k] == 0:
                T1[j][k] = epsilon
            exponentialOfT1AndTR[j][k] = np.exp(-TR/T1[j][k])
            exponentialOfT2AndTE[j][k] = np.exp(-TE/T2[j][k])
            exponentialOfT1AndTE[j][k] = np.exp(-TE/T1[j][k])
            decayMatrices[j][k][:][:] = np.array([[exponentialOfT2AndTE[j][k], 0, 0],
                                                  [0, exponentialOfT2AndTE[j][k], 0],
                                                  [0, 0, exponentialOfT1AndTE[j][k]]])

#############################################################################################
#############################################################################################

def decayFunction(phantomSize,decayMatrices,magneticVector):

    for j in range(phantomSize):
        for k in range(phantomSize):

            magneticVector[j][k] = np.matmul(decayMatrices[j][k][:][:], magneticVector[j][k])
        
    return magneticVector

#############################################################################################
#############################################################################################

def gradientMultiplicationFunction (phantomSize, gxStep, gyStep, magneticVector, kSpace, kSpaceRowIndex, kSpaceColumnIndex):

    for j in range(phantomSize):
        for k in range(phantomSize):
            alpha = gxStep*j + gyStep*k
            magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
            kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude

#############################################################################################
#############################################################################################

def spoilerMatrix (phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle):
    
    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k][0] = 0
            magneticVector[j][k][1] = 0
            magneticVector[j][k][2] =  np.cos(flipAngle) + 1 - exponentialOfT1AndTR[j][k]
            
    return magneticVector



