#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 10:47:35 2019

@author: crow
"""

class Label(QtWidgets.QLabel):
    def _init_(self, parent=None):
        super(Label, self)._init_(parent = parent)
        self.x = 0
        self.y = 0
        self.point=[]
        self.pixel=[]
        self.paint=False
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        if  self.point: 
            for self.pixel in self.point:     
               painter.setPen(QtGui.QPen(self.pixel[2]))
               painter.drawRect(self.pixel[0],self.pixel[1],4,4)
               
               
               
               
self.show_phantom_label = Label(self.centralwidget)