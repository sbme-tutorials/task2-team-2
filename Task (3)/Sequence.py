#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 15:06:14 2019

@author: crow
"""

import pyqtgraph as pg

class Sequence(object):
    view = pg.GraphicsView()
    l = pg.GraphicsLayout(border=(100,100,100))
    view.setCentralItem(l)

    def __init__(self):
        self.l.nextRow()
        l2 = self.l.addLayout(colspan=3, border=(50,0,0))
        l2.setContentsMargins(10, 10, 10, 10)
        l2.addLabel("Graphical Representation of used sequence", colspan=3)

        l2.nextRow()
        l2.addLabel('RF', angle=-90, rowspan=1)
        rf_plot = l2.addPlot()

        l2.nextRow()
        l2.addLabel('Gz', angle=-90, rowspan=1)
        gz_plot = l2.addPlot()

        l2.nextRow()
        l2.addLabel('Gx', angle=-90, rowspan=1)
        gx_plot = l2.addPlot()

        l2.nextRow()
        l2.addLabel('Gy', angle=-90, rowspan=1)
        gy_plot = l2.addPlot()

        l2.nextRow()
        l2.addLabel('Readout', angle=-90, rowspan=1)
        readout_plot = l2.addPlot()

        l2.nextRow()
        l2.addLabel("Time", col=1, colspan=2)

    ## hide axes on some plots
        rf_plot.hideAxis('bottom')
        gz_plot.hideAxis('bottom')
        gx_plot.hideAxis('bottom')
        gy_plot.hideAxis('bottom')

    def show(self):
        self.view.show()
