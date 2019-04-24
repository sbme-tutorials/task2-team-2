# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:12:25 2019

@author: manog
"""
import numpy as np

def multiplyingPD_ByMagneticVector (magneticVector, PD, phantomSize):
    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k] = magneticVector[j][k]**PD[j][k]
    
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

def decayFunction(phantomSize,T1,T2,TE,TR,magneticVector):
    
    exponentialOfT1AndTR = np.zeros((phantomSize,phantomSize))
    exponentialOfT2AndTE = np.zeros((phantomSize,phantomSize))
    exponentialOfT1AndTE = np.zeros((phantomSize,phantomSize))
    decayMatrices = np.zeros((phantomSize,phantomSize,3,3))
    
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

def spoilerMatrix (phantomSize, magneticVector, T1, TR):
    
    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k][0] = 0
            magneticVector[j][k][1] = 0
            magneticVector[j][k][2] =  1 - np.exp(-TR / T1[j][k])
            
    return magneticVector



