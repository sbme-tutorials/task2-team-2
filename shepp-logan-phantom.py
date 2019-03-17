# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 01:15:05 2019

@author: Gamila
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as pl

def phantom (n = 256, p_type = 'Modified Shepp-Logan'):
        ellipses=_mod_shepp_logan_PD ()

        # Blank image
        p = np.zeros ((n, n)) ## defining blank  512 x512 image
        
        # Create the pixel grid
        ygrid, xgrid = np.mgrid[-1:1:(1j*n), -1:1:(1j*n)]

        for ellip in ellipses:
                I   = ellip [0]
                a2  = ellip [1]**2 # power 2
                b2  = ellip [2]**2 # power2
                x0  = ellip [3]
                y0  = ellip [4]
                phi = ellip [5] * np.pi / 180  # Rotation angle in radians

                # Create the offset x and y values for the grid
                x = xgrid - x0
                y = ygrid - y0

                cos_p = np.cos (phi)
                sin_p = np.sin (phi)
                 #(x-h)²/a²+(y-k)²/b²=1.
                # Find the pixels within the ellipse
                locs = (((x * cos_p + y * sin_p)**2) / a2
              + ((y * cos_p - x * sin_p)**2) / b2) <= 1

                # Add the ellipse intensity to those pixels
                p [locs] += I

        return p
def _mod_shepp_logan_PD ():
        #  Modified version of Shepp & Logan's head phantom,
        #  adjusted to improve contrast.  Taken from Toft.
        return [[   1,   .69,   .92,    0,      0,   0],
                [-.80, .6624, .8740,    0, -.0184,   0],
                [-.20, .1100, .3100,  .22,      0, -18],
                [-.20, .1600, .4100, -.22,      0,  18],
                [ .10, .2100, .2500,    0,    .35,   0],
                [ .10, .0460, .0460,    0,     .1,   0],
                [ .10, .0460, .0460,    0,    -.1,   0],
                [ .10, .0460, .0230, -.08,  -.605,   0],
                [ .10, .0230, .0230,    0,  -.606,   0],
                [ .10, .0230, .0460,  .06,  -.605,   0]]
def _mod_shepp_logan_T1 ():
        #  Modified version of Shepp & Logan's head phantom,
        #  adjusted to improve contrast.  Taken from Toft.
        return [[   1,   .69,   .92,    0,      0,   0],
                [-.50, .6624, .8740,    0, -.0184,   0],
                [-.70, .1100, .3100,  .22,      0, -18],
                [-.10, .1600, .4100, -.22,      0,  18],
                [ .70, .2100, .2500,    0,    .35,   0],
                [ .40, .0460, .0460,    0,     .1,   0],
                [ .80, .0460, .0460,    0,    -.1,   0],
                [ .70, .0460, .0230, -.08,  -.605,   0],
                [ .10, .0230, .0230,    0,  -.606,   0],
                [ .50, .0230, .0460,  .06,  -.605,   0]]
def _mod_shepp_logan_T2 ():
        #  Modified version of Shepp & Logan's head phantom,
        #  adjusted to improve contrast.  Taken from Toft.
        return [[   1,   .69,   .92,    0,      0,   0],
                [-.80, .6624, .8740,    0, -.0184,   0],
                [-.50, .1100, .3100,  .22,      0, -18],
                [-.10, .1600, .4100, -.22,      0,  18],
                [ .60, .2100, .2500,    0,    .35,   0],
                [ .40, .0460, .0460,    0,     .1,   0],
                [ .550, .0460, .0460,    0,    -.1,   0],
                [ .30, .0460, .0230, -.08,  -.605,   0],
                [ .10, .0230, .0230,    0,  -.606,   0],
                [ .30, .0230, .0460,  .06,  -.605,   0]]
P = phantom ()
pl.imshow (P, cmap='gray')

