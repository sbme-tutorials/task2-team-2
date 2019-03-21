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
import numpy as np
from PyQt5 import QtWidgets
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
        #connecting browsebutton with loading the file function
        self.ui.browse_button.clicked.connect(self.button_clicked)
        #calling the property from the combobox to display the phantom
        
        # Initializing Pixel clicked counter
        # Must not exceed 5
        self.ui.pixel_counter=0
        
        # Change these variables to the real t1 and t2 got from the pixmap
        # You should pass them the values in the plot() function
        self.ui.t1=1
        self.ui.t2=1

        
        
        

    def  button_clicked(self):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Choose a phantom", "", "Filter -- ( *.npy)")
        if fileName:
           Phantom_file=np.load(fileName)
           SeparatingArrays=(len(Phantom_file)/3)
           self.I=Phantom_file[1:int(SeparatingArrays),:]
           self.T1=Phantom_file[1+int(SeparatingArrays):2*int(SeparatingArrays),:]
           self.T2=Phantom_file[1+2*int(SeparatingArrays):3*int(SeparatingArrays),:]
           self.getValueFromProperties_ComboBox()
           #show phantom according to chosen property      
#    
           
        else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("File is not Compatible!")
                msg.setInformativeText('Choose a phantom')
                msg.setWindowTitle("Error")
                msg.exec_()   
  
    def getValueFromProperties_ComboBox(self):
          PropertyOfPhantom=self.ui.properties_comboBox.currentText()
          print(str(PropertyOfPhantom))
           #show phantom according to chosen property      
          if str(PropertyOfPhantom)== ("T1"):
              phantom=qimage2ndarray.array2qimage(self.T1)
              pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)  
          elif str(PropertyOfPhantom)== ("Proton Density"):
              phantom=qimage2ndarray.array2qimage(self.I)
              pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.ui.show_phantom_label.setPixmap(pixmap_of_phantom) 
          else:
              phantom=qimage2ndarray.array2qimage(self.T2)
              pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.ui.show_phantom_label.setPixmap(pixmap_of_phantom) 
              
             

        
        
    
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
            # Plotting
            self.plot()
        return super(ApplicationWindow, self).eventFilter(source, event)
    
    # Plot function
    def plot(self):
        # self.ui.graphicsView and self.ui.graphicsView_2 aren't graphicsViews
        # Instead, I changed them to PlotWidgets in the Main_GUI.py file 
        # starting by passing them to variables
        t1_plotWindow = self.ui.graphicsView
        t2_plotWindow = self.ui.graphicsView_2
        # A time array from 1 to 1000 seconds
        t= np.arange(1000)
        # T1 equation
        t1_plot= 1 - np.exp(-t/self.ui.t1)   # Replace self.ui.t1 with the T1
        # T2 equation
        t2_plot= np.exp(-t/self.ui.t2)   #Replace the self.ui.t2 with the T2
        # Checking if no more than 5 pixels are chosen
        if self.ui.pixel_counter<5:
            # Plotting T1
            t1_plotWindow.plot(t1_plot)
            # Plotting T2
            t2_plotWindow.plot(t2_plot)
            # Incrementing the pixel_counter
            self.ui.pixel_counter+=1
        else:
            # Now if more than 5 pixels are picked, clear both widgets and start over
            t1_plotWindow.clear()
            t2_plotWindow.clear()
            # Plotting
            t1_plotWindow.plot(t1_plot)
            t2_plotWindow.plot(t2_plot)
            # Reseting the counter to 1
            self.ui.pixel_counter=1
        
            
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()