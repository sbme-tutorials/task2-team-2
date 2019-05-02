#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:39 2019

@author: crow
"""

import sys
import math
import numpy as np
import qimage2ndarray
import pyqtgraph as pg

def drawRF(rf_plot,narrower):
    x = np.linspace(-5,5,50)
    equation = np.sin(narrower*x)/x
    rf_plot.plot(equation)


def drawGZ(gz_plot,identifier):
    flat_line = np.full((1,1000),-1)
    temp = np.full((1,200),1)
    flat_line[:,11:211] = temp
    step = np.heaviside(flat_line,flat_line)
    gz_plot.plot(step)

