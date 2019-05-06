# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:11:30 2019

@author: Gamila
"""
import numpy as np
import functionsForTask3
import pyqtgraph as pg

#signal =0
#maximumSignal=0
#flipAngleArray=0
#signalArray=0


def DrawErnstAngleSSFP(phantomSize,TR,TE,T1,T2,ernst_plot):
    flipAngleArray=[]
    signalArray=[]
    magneticVector = np.array([0,0,1])
    maximumSignal=0
    exponentialOfT1AndTR = np.exp(-TR/T1)
    exponentialOfT1AndTE = np.exp(-TE/T1)
    exponentialOfT2AndTE = np.exp(-TE/T2)
#    ErnstAngle = 0
    decayExponential = np.array([[exponentialOfT2AndTE,0,0],
                                 [0,exponentialOfT2AndTE,0],
                                 [0,0,exponentialOfT1AndTE]])
    recoveryExponential = np.array([0,0,1-exponentialOfT1AndTR])
    for flipAngle in range (181): #for SSFP,

        rotationAroundXMatrix = np.array([[1, 0, 0],
                                          [0, np.cos(flipAngle), np.sin(flipAngle)],
                                          [0, -np.sin(flipAngle), np.cos(flipAngle)]])
#        rotationAroundNegativeXMatrix = np.array([[1, 0, 0],
#                                                  [0, np.cos(f-lipAngle), np.sin(-flipAngle)],
#                                                  [0, -np.sin(-flipAngle), np.cos(-flipAngle)]])
#
        flipAngleArray.append(flipAngle)
        for counter in range (10):
           magneticVector=np.matmul(rotationAroundXMatrix,magneticVector)
           magneticVector=np.matmul(decayExponential,magneticVector)
           magneticVector=np.add(recoveryExponential,magneticVector)



           #signal+=signal we need the last magnetization vector not average
        signalArray.append(magneticVector[2])


        if signalArray[flipAngle]> maximumSignal:
             maximumSignal=signalArray[flipAngle]
             ErnstAngle=flipAngle
    #Plot signalArray vs flipAngle
    n = 180
    s1 = pg.ScatterPlotItem(size=10, pen=pg.mkPen(None), brush=pg.mkBrush(255, 255, 255, 120))
    pos = np.random.normal(size=(2,n), scale=1e-5)
    spots = [{'pos': pos[:,i], 'data': 1} for i in range(n)] + [{'pos': [0,0], 'data': 1}]
    s1.addPoints(spots)
    ernst_plot.addItem(s1)

## for GRE #choosing tissue from combobox from tab1 to take its T! and
def DrawErnstAngleGRE(TR,TE,T1,T2,ernst_plot):
#        signal[x][y][z]=np.sin(flipAngle)*(1-np.exp(-TR/T1))*np.exp(-TE/T2)/(1-np.cos(flipAngle)*np.exp(-TR/T1))            #using T2*=T2
## plot only signal[z] versus theta
        theta = np.arange(180)
        ernst_angle_plot= np.sin(theta)*(1-np.exp(-TR/T1))*np.exp(-TE/T2)/(1-np.cos(theta)*np.exp(-TR/T1))
        ernst_plot.plot(ernst_angle_plot)

