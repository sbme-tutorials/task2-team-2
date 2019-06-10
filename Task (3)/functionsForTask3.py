# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 12:12:25 2019

@author: manog
"""
import numpy as np


def startUpCycle (magneticVector, phantomSize, flipAngle, T1, TR, decayMatrices, x):

    for counter in range(x):
        magneticVector = rotationAroundXFunction(phantomSize, flipAngle, magneticVector)
        magneticVector = decayFunction(phantomSize,decayMatrices,magneticVector)
        magneticVector = rotationAroundXFunction(phantomSize, -1*flipAngle, magneticVector)

        for j in range(phantomSize):
            for k in range(phantomSize):
                magneticVector[j][k] = magneticVector[j][k] + np.array([0,0,np.cos(flipAngle) + magneticVector[j][k][2] - np.exp(-TR/T1[j][k])])
    return magneticVector


def startUpCycle2 (magneticVector, phantomSize, flipAngle, T1, TR, decayMatrices, exponentialOfT1AndTR, x):

    for counter in range(x):
        magneticVector = rotationAroundXFunction(phantomSize, flipAngle, magneticVector)
        magneticVector = decayFunction(phantomSize,decayMatrices,magneticVector)
        magneticVector = spoilerMatrix (phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle)
    return magneticVector


#############################################################################################
#############################################################################################


def multiplyingPD_ByMagneticVector (magneticVector, PD, phantomSize, flipAngle, exponentialOfT1AndTR):
    for j in range(phantomSize):
        for k in range(phantomSize):
#            magneticVector[j][k] = magneticVector[j][k]**PD[j][k]
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

def rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector, j, k):
    
        rotateX = np.array([[np.cos(gxStep*j), np.sin(gxStep*j), 0],
                            [-np.sin(gxStep*j), np.cos(gxStep*j), 0],
                            [0, 0, 1]])
        rotateY = np.array([[np.cos(gyStep*k), np.sin(gyStep*k), 0],
                            [-np.sin(gyStep*k), np.cos(gyStep*k), 0],
                            [0, 0, 1]])
        magneticVector = np.matmul(rotateX, magneticVector)
        magneticVector = np.matmul(rotateY, magneticVector)


        return magneticVector
    
    
def rotationInXYPlaneFunction2(phantomSize, gxStep, gyStep, magneticVector):

    encodedVector = np.zeros((phantomSize,phantomSize,3))
    for j in range(phantomSize):
        for k in range(phantomSize):
            alpha = gxStep*j + gyStep*k
            rotate = np.array([[np.cos(alpha), np.sin(alpha), 0],
                               [-np.sin(alpha), np.cos(alpha), 0],
                               [0, 0, 1]])
            encodedVector[j][k] = np.matmul(rotate, magneticVector[j][k])

    return encodedVector

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
                                                  [0, 0, 1]])

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
            exp = np.array([[1,0,0],
                            [0,1,0],
                            [0,0,exponentialOfT1AndTR[j][k]]])
            magneticVector[j][k] = np.matmul(exp,magneticVector[j][k]) + np.array([0,0,1-exponentialOfT1AndTR[j][k]])

    return magneticVector


#############################################################################################
############################## Preparation Sequences ########################################
#############################################################################################



def inversionRecovery(magneticVector,phantomSize,T1,InversionTime):
#    exponentialOfT1AndInversionTime = np.zeros((phantomSize,phantomSize))
    magneticVector = rotationAroundXFunction(phantomSize,np.pi,magneticVector)
    for j in range(phantomSize):
        for k in range(phantomSize):
#            exponentialOfT1AndInversionTime[j][k] = np.exp(-InversionTime/T1[j][k])
#            magneticVector[j][k][2] = -1 + 2*exponentialOfT1AndInversionTime[j][k]
            magneticVector[j][k][2] = 1 - 2*np.exp(-InversionTime/T1[j][k])
    return magneticVector


def inversionRecovery2(magneticVector,phantomSize,T1,InversionTime):
#    exponentialOfT1AndInversionTime = np.zeros((phantomSize,phantomSize))
    magneticVector = rotationAroundXFunction(phantomSize,np.pi,magneticVector)
    for j in range(phantomSize):
        for k in range(phantomSize):
            exp = np.array([[1,0,0],
                            [0,1,0],
                            [0,0,np.exp(-InversionTime/T1[j][k])]])
            magneticVector[j][k] = np.matmul(exp,magneticVector[j][k]) + np.array([0,0,1-np.exp(InversionTime/T1[j][k])])
    return magneticVector



def T2Prep(magneticVector, phantomSize, timeBetweenPulses, T2, T1):
    decayForT2Prep = np.zeros((phantomSize,phantomSize,3,3))
    for j in range(phantomSize):
       for k in range(phantomSize):
           decayMatrix = np.array([[np.exp(-timeBetweenPulses/T2[j][k]),0,0],
                                    [0,np.exp(-timeBetweenPulses/T2[j][k]),0],
                                    [0,0,1]])
           decayForT2Prep[j][k][:][:] = decayMatrix
    magneticVector = rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)
    magneticVector = decayFunction(phantomSize,decayForT2Prep,magneticVector)
    magneticVector = rotationAroundXFunction(phantomSize,-np.pi/2,magneticVector)
    return magneticVector


def Tagging(magneticVector, phantomSize, spacingBetweenWaves):
    for j in range(phantomSize):
        if (j%spacingBetweenWaves) == 0:
            for k in range(phantomSize):
                magneticVector[j][k][2] *= np.sin(2*np.pi/phantomSize*k)
    return magneticVector

def Tagging2(magneticVector, phantomSize, spacingBetweenWaves):
    magneticVector = rotationAroundXFunction(phantomSize,np.pi,magneticVector)
    magneticVector = rotationInXYPlaneFunction2(phantomSize,0,np.pi/phantomSize*spacingBetweenWaves,magneticVector)
    magneticVector = rotationAroundXFunction(phantomSize,-np.pi,magneticVector)
    magneticVector[:][:][0] = 0
    magneticVector[:][:][1] = 0

    return magneticVector













def gradientXY(matrix, stepY, stepX):
    shape = np.shape(matrix)
    rows = shape[0]
    cols = shape[1]
    newMatrix = np.zeros(shape)
    for i in range(0, rows):
        for j in range(0, cols):
            angle = stepY * j + stepX * i
            angle = (angle) * (np.pi / 180)
            newMatrix[i, j] = np.matmul(np.array([[np.cos(angle), -1 * np.sin(angle), 0],
                                                  [np.sin(angle), np.cos(angle), 0],
                                                  [0, 0, 1]]), matrix[i, j])
    return newMatrix

