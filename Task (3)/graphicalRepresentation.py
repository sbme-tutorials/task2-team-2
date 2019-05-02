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
    x = np.linspace(-5, 5, 41)
    equation = np.sin(narrower*x)/x
    rf_plot.plot(equation)