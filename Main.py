#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:34:52 2019

@author: crow
"""
import sys
import math
from PyQt5 import QtWidgets ,QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from Main_GUI import Ui_MainWindow
import numpy as np
import matplotlib.pyplot as pl
import qimage2ndarray


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
        # Assigning a filter for the label to catch any mouse events
        self.ui.show_phantom_label.installEventFilter(self)
        # Getting Default size of the label on starting the application
        self.ui.default_height= self.ui.show_phantom_label.geometry().height()
        self.ui.default_width= self.ui.show_phantom_label.geometry().width()
        self.ui.browse_button.clicked.connect(self.button_clicked)
        
    def  button_clicked(self):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Choose a phantom", "", "Filter -- ( *.npy)")
        if fileName:
           Phantom_file=np.load(fileName)
           SeparatingArrays=(len(Phantom_file)/3)
           print(SeparatingArrays)
           I=Phantom_file[1:int(SeparatingArrays),:]
           T1=Phantom_file[1+int(SeparatingArrays):2*int(SeparatingArrays),:]
           T2=Phantom_file[1+2*int(SeparatingArrays):3*int(SeparatingArrays),:]
           phantom=qimage2ndarray.array2qimage(I)
           pixmap_of_phantom=QPixmap.fromImage(phantom)
           self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)          
           
    
           
        else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("File is not Compatible!")
                msg.setInformativeText('Choose a phantom')
                msg.setWindowTitle("Error")
                msg.exec_()   
  
    #def getValueFromProperties_ComboBox:
        
    
    # This is the filter used to catch mouse events exculesivly on label
    # source >> the target widget
    # event >> the mouse event passed
    
    def eventFilter(self, source, event):
        # checking whether the event is a mouse click and the target is the widget
        if event.type() == event.MouseButtonPress and source is self.ui.show_phantom_label:
            # Getting scaled height in case of resizing
            self.ui.scaled_height=self.ui.show_phantom_label.geometry().height()
            # Getting scaled Width
            self.ui.scaled_width=self.ui.show_phantom_label.geometry().width()
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