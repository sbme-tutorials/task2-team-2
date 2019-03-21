#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:34:52 2019

@author: crow
"""
import sys
import math
from PyQt5 import QtWidgets
from Main_GUI import Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        # Assigning a filter for the label to catch any mouse events
        self.ui.label.installEventFilter(self)
        # Getting Default size of the label on starting the application
        self.ui.default_height= self.ui.label.geometry().height()
        self.ui.default_width= self.ui.label.geometry().width()
        self.ui.
    def     
    # This is the filter used to catch mouse events exculesivly on label
    # source >> the target widget
    # event >> the mouse event passed
    def eventFilter(self, source, event):
        # checking whether the event is a mouse click and the target is the widget
        if event.type() == event.MouseButtonPress and source is self.ui.label:
            # Getting scaled height in case of resizing
            self.ui.scaled_height=self.ui.label.geometry().height()
            # Getting scaled Width
            self.ui.scaled_width=self.ui.label.geometry().width()
            # Calculating the ratio of scaling in both height and width
            self.ui.scaled_height_ratio=self.ui.scaled_height/self.ui.default_height
            self.ui.scaled_width_ratio=self.ui.scaled_width/self.ui.default_width
            # Getting mouse position 
            self.ui.mouse_pos= event.pos()
            # Using the scaling ratio to retrieve the target pixel
            # Dividing and flooring the mouse position in X and Y coordinates by scaling factor
            # These 2 variables will be used to catch the intended pixel that the used clicked
            self.ui.pixel_clicked_x= math.floor(self.ui.mouse_pos.x()/self.ui.scaled_width_ratio)
            self.ui.pixel_clicked_y= math.floor(self.ui.mouse_pos.y()/self.ui.scaled_height_ratio)
        return super(ApplicationWindow, self).eventFilter(source, event)
            
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()