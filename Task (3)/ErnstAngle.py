# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:11:30 2019

@author: Gamila
"""
import numpy as np
#import functionsForTask3
import pyqtgraph as pg




def DrawErnstAngleSSFP(phantomSize,TR,TE,T1,T2,ernst_plot,label):
    array_to_be_plotted=np.zeros((180,2))
    flipAngleArray=[]
    signalArray=[]
    magneticVector = np.array([0,0,1])
    maximumSignal=0
    exponentialOfT1AndTR = np.exp(-TR/T1)
    exponentialOfT1AndTE = np.exp(-TE/T1)
    exponentialOfT2AndTE = np.exp(-TE/T2)

    decayExponential = np.array([[exponentialOfT2AndTE,0,0],
                                 [0,exponentialOfT2AndTE,0],
                                 [0,0,exponentialOfT1AndTE]])
    recoveryExponential = np.array([0,0,1-exponentialOfT1AndTR])
    for flipAngle in range (180): #for SSFP,

        rotationAroundXMatrix = np.array([[1, 0, 0],
                                          [0, np.cos(flipAngle*np.pi/180), np.sin(flipAngle*np.pi/180)],
                                          [0, -np.sin(flipAngle*np.pi/180), np.cos(flipAngle*np.pi/180)]])
#
#
        flipAngleArray.append(flipAngle)
        for counter in range (10):
           magneticVector=np.matmul(rotationAroundXMatrix,magneticVector)
           magneticVector=np.matmul(decayExponential,magneticVector)
           magneticVector=np.add(magneticVector, recoveryExponential)



           #signal+=signal we need the last magnetization vector not average
        signalArray.append(magneticVector[2])


        if signalArray[flipAngle]> maximumSignal:
             maximumSignal=signalArray[flipAngle]
             ErnstAngle=flipAngle


    #Plot signalArray vs flipAngle
    vLine = pg.InfiniteLine(angle=90, movable=False)
    hLine = pg.InfiniteLine(angle=0, movable=False)
    array_to_be_plotted[:,0] = flipAngleArray
    array_to_be_plotted[:,1] = signalArray
    ernst_plot.plot(array_to_be_plotted, pen='r')
    vLine.setPos(ErnstAngle)
    hLine.setPos(signalArray[ErnstAngle])
    ernst_plot.addItem(vLine,ignoreBounds=True)
    ernst_plot.addItem(hLine,ignoreBounds=True)
    label.setText("Ernst Angle "+str(ErnstAngle)+"∘")

## for GRE #choosing tissue from combobox from tab1 to take its T! and
def DrawErnstAngleGRE(TR,TE,T1,T2,ernst_plot,label):

## plot only signal[z] versus theta
        array_to_be_plotted=np.zeros((180,2))
        theta_range = np.arange(0,180,1)
        theta_range = np.reshape(theta_range,(180))
        array_to_be_plotted[:,0] = theta_range
        ernst_angle_equation= np.sin(theta_range*np.pi/180)*(1-np.exp(-TR/T1))*np.exp(-TE/T2)/(1-np.cos(theta_range*np.pi/180)*np.exp(-TR/T1))
        array_to_be_plotted[:,1] = ernst_angle_equation
        max_recovery_index = np.argmax(ernst_angle_equation)
        vLine = pg.InfiniteLine(angle=90, movable=False)
        vLine.setPos(theta_range[max_recovery_index])
        hLine = pg.InfiniteLine(angle=0, movable=False)
        hLine.setPos(ernst_angle_equation[max_recovery_index])
        ernst_plot.plot(array_to_be_plotted, pen='r')
        ernst_plot.addItem(vLine,ignoreBounds=True)
        ernst_plot.addItem(hLine,ignoreBounds=True)
        label.setText("Ernst Angle "+str(theta_range[max_recovery_index])+"∘")



