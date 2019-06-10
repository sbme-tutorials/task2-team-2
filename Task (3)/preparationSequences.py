# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:07:52 2019

@author: manog
"""

import numpy as np
import functionsForTask3

def inversionRecovery(magneticVector,phantomSize,T1,InversionTime,exponentialOfT1AndTR):
    exponentialOfT1AndInversionTime = np.zeros((phantomSize,phantomSize))
    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi,magneticVector)
    for j in range(phantomSize):
        for k in range(phantomSize):
            exponentialOfT1AndInversionTime[j][k] = np.exp(-InversionTime/T1[j][k])
            magneticVector[j][k][2] = -1 + 2*exponentialOfT1AndInversionTime[j][k]
    return magneticVector


def T2Prep(magneticVector, phantomSize, timeBetweenPulses, T2, T1):
    decayForT2Prep = np.zeros((phantomSize,phantomSize,3,3))
    for j in range(phantomSize):
       for k in range(phantomSize):
           decayMatrix = np.array([[np.exp(-timeBetweenPulses/T2[j][k]),0,0],
                                    [0,np.exp(-timeBetweenPulses/T2[j][k]),0],
                                    [0,0,np.exp(-timeBetweenPulses/T1[j][k])]])
           decayForT2Prep[j][k][:][:] = decayMatrix
    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)
    magneticVector = functionsForTask3.decayFunction(phantomSize,decayForT2Prep,magneticVector)
    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,-np.pi/2,magneticVector)
    return magneticVector


def Tagging(magneticVector, phantomSize, spacingBetweenWaves):
    for j in range(phantomSize):
        if (j%spacingBetweenWaves) == 0:
            for k in range(phantomSize):
                magneticVector[j][k][2] *= np.sin(2*np.pi/phantomSize*k)
    return magneticVector
