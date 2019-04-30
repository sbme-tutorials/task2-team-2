# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:11:30 2019

@author: Gamila
"""
import numpy as np
import functionsForTask3

siganl =0
maximumSignal=0
flipAngleArray=0
signalArray=0


for flipAngle in range (180): #for SSFP
    flipAngleArray.append(flipAngle)
    for counter in range (10):
       signal=functionsForTask3.rotationAroundXFunction(phantomSize, flipAngle, magneticVector)
       signalArray.append(signal)
       #signal+=signal we need the last magnetization vector not average
    signalArray.append(signal)

       
    if signal> maximumSignal:
         maximumSignal=signal
         print(flipAngle) 

## for GRE #choosing tissue from combobox from tab1 to take its T! and T2
signal=np.sin(flipAngle)*(1-np.exp(-TR/T1))*np.exp(-TE/T2)/(1-np.cos(flipAngle)*np.exp(-TR/T1))            #using T2*=T2
         
         
       
       
