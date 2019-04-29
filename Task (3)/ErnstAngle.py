# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 09:11:30 2019

@author: Gamila
"""
import math
import functionsForTask3

siganl =0
maximumSignal=0

for flipAngle in range (180): #for SSFP
    for counter in range (10):
       signal=functionsForTask3.rotationAroundXFunction(phantomSize, flipAngle, magneticVector)
       signal+=signal
       
    if signal> maximumSignal:
         maximumSignal=signal
         print(flipAngle) 

## for GRE
flipAngle=math.acose(exp(-TR\T1[j][k]))
         
         
       
       
