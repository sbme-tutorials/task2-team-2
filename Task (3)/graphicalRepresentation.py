#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:39 2019

@author: crow
"""


import numpy as np
import math

def drawRF(rf_plot,recoveryTime,echoTime):
    x = np.linspace(-6,6,math.floor(recoveryTime*0.15))
    equation = np.sin(2*x)/x
    rf_plot.setXRange(0,recoveryTime)
    rf_plot.plot(equation)


def drawGZ(gz_plot,mode,recoveryTime,echoTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,math.floor(recoveryTime*0.15)),1)
    flat_line[:,0:math.floor(recoveryTime*0.15)] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gz_plot.setXRange(0,recoveryTime)
    gz_plot.plot(step)


def drawGX(gx_plot,mode,recoveryTime,echoTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,math.floor(recoveryTime*0.15)),1)
    flat_line[:,math.floor(recoveryTime*0.15 + recoveryTime*0.02):math.floor(2*recoveryTime*0.15 + recoveryTime*0.02)] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gx_plot.setXRange(0,recoveryTime)
    gx_plot.plot(step)



def drawGY(gy_plot,mode,recoveryTime,echoTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,math.floor(recoveryTime*0.15)),1)
    flat_line[:,math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02):math.floor(3*recoveryTime*0.15 + 2*recoveryTime*0.02)] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gy_plot.setXRange(0,recoveryTime)
    gy_plot.plot(step)



def drawReadOut(readout_plot,mode,recoveryTime,echoTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,math.floor(recoveryTime*0.15)),1)
    flat_line[:,math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02):math.floor(3*recoveryTime*0.15 + 2*recoveryTime*0.02)] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    readout_plot.setXRange(0,recoveryTime)
    readout_plot.plot(step)




