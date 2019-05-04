#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:39 2019

@author: crow
"""


import numpy as np


def drawRF(rf_plot,recoveryTime):
    x = np.linspace(-6,6,150)
    equation = np.sin(2*x)/x
    rf_plot.setXRange(0,recoveryTime)
    rf_plot.plot(equation)


def drawGZ(gz_plot,mode,recoveryTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,150),1)
    flat_line[:,0:150] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gz_plot.setXRange(0,recoveryTime)
    gz_plot.plot(step)


def drawGX(gx_plot,mode,recoveryTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,150),1)
    flat_line[:,170:320] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gx_plot.setXRange(0,recoveryTime)
    gx_plot.plot(step)



def drawGY(gy_plot,mode,recoveryTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,150),1)
    flat_line[:,340:490] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    gy_plot.setXRange(0,recoveryTime)
    gy_plot.plot(step)



def drawReadOut(readout_plot,mode,recoveryTime):
    flat_line = np.full((1,recoveryTime),-1)
    temp = np.full((1,150),1)
    flat_line[:,340:490] = temp
    step = np.heaviside(flat_line,flat_line)
    step = np.reshape(step,(recoveryTime,))
    readout_plot.setXRange(0,recoveryTime)
    readout_plot.plot(step)




