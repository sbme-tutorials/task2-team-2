#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:34:52 2019

@author: crow
"""

import sys
import math
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QFileDialog
import numpy as np
import pyqtgraph as pg
from Main_GUI import Ui_MainWindow
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
        #connecting sheppLogan button with its function
        self.ui.pushButton_2.clicked.connect(self.sheppLogan)
        # Initializing Pixel clicked counter
        # Must not exceed 5
        self.ui.pixel_counter=0
        
        self.ui.comboBox.currentIndexChanged.connect(self.on_size_change)
        self.ui.properties_comboBox.currentIndexChanged.connect(self.on_property_change)
        
        # self.ui.graphicsView and self.ui.graphicsView_2 aren't graphicsViews
        # Instead, I changed them to PlotWidgets in the Main_GUI.py file 
        # starting by passing them to variables
        self.t1_plotWindow = self.ui.graphicsView
        self.t2_plotWindow = self.ui.graphicsView_2
        
        self.ui.lineEdit_2.textChanged.connect(self.on_lineEdit_change)
        self.ui.lineEdit_3.textChanged.connect(self.on_lineEdit_change_2)
        
        self.te_flag= False
        self.tr_flag= False
        
       

        
        
        

    def  button_clicked(self):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Choose a phantom", "", "Filter -- ( *.npy)")
        if fileName:
           Phantom_file=np.load(fileName)
           self.ui.lineEdit.setText(fileName)
           SeparatingArrays=(len(Phantom_file)/3)
           self.I=Phantom_file[1:int(SeparatingArrays),:]
           self.T1=Phantom_file[1+int(SeparatingArrays):2*int(SeparatingArrays),:]
           self.T2=Phantom_file[1+2*int(SeparatingArrays):3*int(SeparatingArrays),:]
           self.size_of_matrix= np.size(self.T1)
           self.size_of_matrix_root= math.sqrt(self.size_of_matrix)
           self.t1_plotWindow.clear()
           self.t2_plotWindow.clear()
           self.getValueFromProperties_ComboBox()
           
           #show phantom according to chosen property        
           
        else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("File is not Compatible!")
                msg.setInformativeText('Choose a phantom')
                msg.setWindowTitle("Error")
                msg.exec_()   
  
    def getValueFromProperties_ComboBox(self):
          PropertyOfPhantom=self.ui.properties_comboBox.currentText()
          
           #show phantom according to chosen property      
          if str(PropertyOfPhantom)== ("T1"):  
              phantom=qimage2ndarray.array2qimage(self.T1)
              self.pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.getValueFromSize_ComboBox()
              
              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)  
          elif str(PropertyOfPhantom)== ("Proton Density"):
              phantom=qimage2ndarray.array2qimage(self.I)
              self.pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.getValueFromSize_ComboBox()
          else:  
              phantom=qimage2ndarray.array2qimage(self.T2)
              self.pixmap_of_phantom=QPixmap.fromImage(phantom)
              self.getValueFromSize_ComboBox()
              
    def getValueFromSize_ComboBox(self):
          
          selected_size=self.ui.comboBox.currentText()
          
           #show phantom according to chosen property      
          if str(selected_size)== ("Default"):
              self.ui.show_phantom_label.setGeometry(0,0,math.sqrt(self.size_of_matrix),math.sqrt(self.size_of_matrix))
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom)
          elif str(selected_size)== ("32x32"):
              self.ui.show_phantom_label.setGeometry(0,0,32,32)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(32,32,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("128x128"):
              self.ui.show_phantom_label.setGeometry(0,0,128,128)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(128,128,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("256x256"):
              self.ui.show_phantom_label.setGeometry(0,0,256,256)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(256,256,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("512x512"):
              self.ui.show_phantom_label.setGeometry(0,0,512,512)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
              


    def getValueFromLine_edit_te(self):
        self.te=int(self.ui.lineEdit_2.text())
        self.te_flag= True
        
        
    def getValueFromLine_edit_tr(self):
        self.tr=int(self.ui.lineEdit_3.text())
        self.tr_flag= True
    
    
    
    
    def sheppLogan(self): 
          
          sheppLogan_file = np.load('sheppLogan_phantom.npy')
          z=(len(sheppLogan_file )/3)

          self.I=sheppLogan_file [1:int(z),:]
          self.T1=sheppLogan_file [1+int(z):2*int(z),:]
          self.T2=sheppLogan_file [1+2*int(z):3*int(z),:]
          self.T2= (255*self.T2)/np.max(self.T2)
          self.T1= (255*self.T1)/np.max(self.T1)
          self.I= (255*self.I)/np.max(self.I)
          self.size_of_matrix= np.size(self.T1)
          self.size_of_matrix_root= math.sqrt(self.size_of_matrix)
          self.getValueFromProperties_ComboBox()          
    
    
    
    
        #  Modified version of Shepp & Logan's head phantom,
        #  adjusted to improve contrast.  Taken from Toft.
          
        
        
    
    # This is the filter used to catch mouse events exculesivly on label
    # source >> the target widget
    # event >> the mouse event passed
    
    def eventFilter(self, source, event):
        # checking whether the event is a mouse click and the target is the widget
        if event.type() == event.MouseButtonPress and source is self.ui.show_phantom_label:
            
            # Getting scaled height in case of resizing
            self.label_height=self.ui.show_phantom_label.geometry().height()
            # Getting scaled Width
            self.label_width=self.ui.show_phantom_label.geometry().width()
            # Calculating the ratio of scaling in both height and width
            self.height_scale=self.label_height/self.size_of_matrix_root
            self.width_scale=self.label_width/self.size_of_matrix_root
            # Getting mouse position 
            self.ui.mouse_pos= event.pos()
            
            # Using the scaling ratio to retrieve the target pixel
            # Dividing and flooring the mouse position in X and Y coordinates by scaling factor
            # These 2 variables will be used to catch the intended pixel that the used clicked
            self.ui.pixel_clicked_x= math.floor(self.ui.mouse_pos.x()/self.width_scale)#/self.ui.scaled_width_ratio)
            self.ui.pixel_clicked_y= math.floor(self.ui.mouse_pos.y()/self.height_scale)#/self.ui.scaled_height_ratio)
            self.ui.label.setText("Matrix Index  "+"("+str(self.ui.pixel_clicked_y)+","+str(self.ui.pixel_clicked_x)+")")
            self.ui.label_2.setText("Pixel Coordinates  "+"("+str(self.ui.mouse_pos.x())+","+str(self.ui.mouse_pos.y())+")")
            # Plotting
            self.plot()
            return super(ApplicationWindow, self).eventFilter(source, event)
        
    @pyqtSlot()
    def on_size_change(self):
        self.getValueFromSize_ComboBox()
        
    @pyqtSlot()
    def on_property_change(self):
        self.getValueFromProperties_ComboBox()
        
    @pyqtSlot()
    def on_lineEdit_change(self):
        self.getValueFromLine_edit_te()
        
    @pyqtSlot()
    def on_lineEdit_change_2(self):
        self.getValueFromLine_edit_tr()
    
    # Plot function
    def plot(self):
        
        
        # Coloring the curve
        if self.ui.pixel_counter == 0:
            x=255
            y=0
            z=0
            if self.te_flag and self.tr_flag:
                lr1 = pg.LinearRegionItem([self.te,self.tr])
                lr2 = pg.LinearRegionItem([self.te,self.tr])
                lr1.setZValue(-10)
                lr2.setZValue(-10)
                self.t1_plotWindow.addItem(lr1)
                self.t2_plotWindow.addItem(lr2)
        elif self.ui.pixel_counter == 1:
            x=0
            y=255
            z=0
        elif self.ui.pixel_counter == 2:
            x=0
            y=0
            z=255
        elif self.ui.pixel_counter == 3:
            x=255
            y=255
            z=0
        elif self.ui.pixel_counter == 4:
            x=255
            y=0
            z=255
        # Sanity checking 
        if self.ui.pixel_clicked_x >= self.size_of_matrix_root:
            self.ui.pixel_clicked_x = self.size_of_matrix_root-2
        if self.ui.pixel_clicked_y >= self.size_of_matrix_root:
            self.ui.pixel_clicked_y = self.size_of_matrix_root-2
            
        # A time array from 1 to 1000 seconds
        t= np.arange(1000)
        # T1 equation
        t1_plot=[]
        if self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y] == 0:
            self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]= 0.00000000000001
        t1_plot= 1 - np.exp(-t/self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y])   # Replace self.ui.t1 with the T1
        # T2 equation
        t2_plot=[]
        if self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y] == 0:
            self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]= 0.00000000000001
        t2_plot= np.exp(-t/self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y])   #Replace the self.ui.t2 with the T2
        # Checking if no more than 5 pixels are chosen
        if self.ui.pixel_counter<5:
            # Plotting T1
            self.t1_plotWindow.plot(t1_plot,pen=(x,y,z),name="T1")
            self.t1_plotWindow.showGrid(x=True, y=True)
            self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            # Plotting T2
            self.t2_plotWindow.plot(t2_plot,pen=(x,y,z),name="T2")
            self.t2_plotWindow.showGrid(x=True, y=True)
            self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            # Incrementing the pixel_counter
            self.ui.pixel_counter+=1
        else:
            # Now if more than 5 pixels are picked, clear both widgets and start over
            self.t1_plotWindow.clear()
            self.t2_plotWindow.clear()
            x=255
            y=0
            z=0
            # Plotting
            self.t1_plotWindow.plot(t1_plot,pen=(x,y,z),name="T1")
            self.t1_plotWindow.showGrid(x=True, y=True)
            self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            self.t2_plotWindow.plot(t2_plot,pen=(x,y,z),name="T2")
            self.t2_plotWindow.showGrid(x=True, y=True)
            self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            if self.te_flag and self.tr_flag:
                lr1 = pg.LinearRegionItem([self.te,self.tr])
                lr2 = pg.LinearRegionItem([self.te,self.tr])
                lr1.setZValue(-10)
                lr2.setZValue(-10)
                self.t1_plotWindow.addItem(lr1)
                self.t2_plotWindow.addItem(lr2)
            
            # Reseting the counter to 1
            self.ui.pixel_counter=1
        
    
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()