#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:34:52 2019

@author: crow
"""

import sys
import math
from PyQt5 import QtWidgets, QtCore
from PIL import Image, ImageEnhance 
from PyQt5.QtGui import QPixmap, QMouseEvent
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QFileDialog
import numpy as np
from MRI_Simulator import Ui_MainWindow
import qimage2ndarray
import pyqtgraph as pg
import threading




class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow,self).__init__()
        self.ui= Ui_MainWindow()
        self.ui.setupUi(self)
    
        # Assigning a filter for the label to catch any mouse events
        self.ui.show_phantom_label.installEventFilter(self)
        # Getting Default size of the label on starting the application
        self.default_height= self.ui.show_phantom_label.geometry().height()
        self.default_width= self.ui.show_phantom_label.geometry().width()
        #connecting browsebutton with loading the file function
        self.ui.browse_button.clicked.connect(self.button_clicked)
        #connecting generate button with generating the k-space
        self.ui.generate_button.clicked.connect(self.generate_Kspace)
        #connecting convert button with converting ifft
        self.ui.convert_button.clicked.connect(self.inverseFourier)
        self.ui.convert_button.setEnabled(False)
        #connecting sheppLogan button with its function
        self.ui.pushButton_2.clicked.connect(self.sheppLogan)
        # Initializing Pixel clicked counter
        # Must not exceed 5
        self.ui.pixel_counter=0
        
        #self.ui.label_10.hide()
#        self.ui.label_9.hide()
        self.point1x = 0
        self.point1y = 0
        self.point2x = 0
        self.point2y = 0
        self.point3x = 0
        self.point3y = 0
        self.point4x = 0
        self.point4y = 0
        self.point5x = 0
        self.point5y = 0
        self.ui.show_phantom_label.point=[]
        
        self.ui.comboBox.currentIndexChanged.connect(self.on_size_change)
        self.ui.properties_comboBox.currentIndexChanged.connect(self.on_property_change)
        self.ui.show_phantom_label.mouseMoveEvent=self.brightness
        self.ui.show_phantom_label.mousePressEvent=self.readCoordinates
        self.ratio = 0

        self.tr_entry_flag=False
        self.te_entry_flag=False
        self.flipAngle_entry_flag=False
        
        self.tr=0
        self.te=0
        self.flipAngle=0
        # self.ui.graphicsView and self.ui.graphicsView_2 aren't graphicsViews
        # Instead, I changed them to PlotWidgets in the Main_GUI.py file 
        # starting by passing them to variables
        self.t1_plotWindow = self.ui.graphicsView
        self.t2_plotWindow = self.ui.graphicsView_2
        
        
        self.vLine1 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine2 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine3 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine4 = pg.InfiniteLine(angle=90, movable=False)
        self.t1_plotWindow.addItem(self.vLine1,ignoreBounds=True)
        self.t1_plotWindow.addItem(self.vLine2,ignoreBounds=True)
        self.t2_plotWindow.addItem(self.vLine3,ignoreBounds=True)
        self.t2_plotWindow.addItem(self.vLine4,ignoreBounds=True)
        
        self.ui.lineEdit_2.editingFinished.connect(self.on_lineEdit_change_te)
        self.ui.lineEdit_3.editingFinished.connect(self.on_lineEdit_change_tr)
        self.ui.lineEdit_4.editingFinished.connect(self.on_lineEdit_change_flipAngle)
        
        self.ui.tabWidget.setCurrentIndex(0)
        
        self.epsilon = np.finfo(np.float32).eps
        self.imaginaryNumber = np.exp(np.complex(0, 1))
        
        self.SHEPPLOGAN_FLAG= False
        
        
       

    ##########################################################################################################################################    
    ##########################################################################################################################################    
        

    def  button_clicked(self):
        fileName, _filter = QFileDialog.getOpenFileName(self, "Choose a phantom", "", "Filter -- ( *.npy)")
        if fileName:
           self.SHEPPLOGAN_FLAG = False
           Phantom_file=np.load(fileName)
           self.ui.lineEdit.setText(fileName)
           SeparatingArrays=(len(Phantom_file)/6)
           self.I=Phantom_file[1:int(SeparatingArrays),:]
           self.T1=Phantom_file[1+int(SeparatingArrays):2*int(SeparatingArrays),:]
           self.T2=Phantom_file[1+2*int(SeparatingArrays):3*int(SeparatingArrays),:]
           self.I_mapped=Phantom_file[1+3*int(SeparatingArrays):4*int(SeparatingArrays),:]
           self.T1_mapped=Phantom_file[1+4*int(SeparatingArrays):5*int(SeparatingArrays),:]
           self.T2_mapped=Phantom_file[1+5*int(SeparatingArrays):6*int(SeparatingArrays),:]          
           self.size_of_matrix= np.size(self.T1)
           self.size_of_matrix_root= math.floor(math.sqrt(self.size_of_matrix))
           self.resetPainting()
           self.resetPlot()
           self.getValueFromProperties_ComboBox()
           self.default_width= self.ui.show_phantom_label.geometry().width()
           self.default_height= self.ui.show_phantom_label.geometry().height()
           self.ui.generate_button.setEnabled(True)
           self.ui.inverseFourier_label.setText(" ")
           self.ui.kspace_label.setText(" ")
            
        else:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Critical)
                msg.setText("File is not Compatible!")
                msg.setInformativeText('Choose a phantom')
                msg.setWindowTitle("Error")
                msg.exec_()   
  
    
    ##########################################################################################################################################
    ##########################################################################################################################################
    
    def getValueFromProperties_ComboBox(self):
        
          PropertyOfPhantom=self.ui.properties_comboBox.currentText()
          
          if self.SHEPPLOGAN_FLAG==False:
           #show phantom according to chosen property      
              if str(PropertyOfPhantom)== ("T1"):  
                  self.phantom=qimage2ndarray.array2qimage(self.T1_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              
              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)  
              elif str(PropertyOfPhantom)== ("Proton Density"):
                  self.phantom=qimage2ndarray.array2qimage(self.I_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              else:  
                  self.phantom=qimage2ndarray.array2qimage(self.T2_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
          elif self.SHEPPLOGAN_FLAG==True:
              if str(PropertyOfPhantom)== ("T1"):
                  self.phantom=qimage2ndarray.array2qimage(self.T1)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              
              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)  
              elif str(PropertyOfPhantom)== ("Proton Density"):
                  self.phantom=qimage2ndarray.array2qimage(self.I)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              else:  
                  self.phantom=qimage2ndarray.array2qimage(self.T2)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              

   
    def getValueFromSize_ComboBox(self):
          
          selected_size=self.ui.comboBox.currentText()
          
           #show phantom according to chosen property      
          if str(selected_size)== ("Default"):
              self.ui.show_phantom_label.setGeometry(0,0,math.sqrt(self.size_of_matrix),math.sqrt(self.size_of_matrix))
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom)
              self.ui.label_11.setPixmap(self.pixmap_of_phantom)
          elif str(selected_size)== ("32x32"):
              self.ui.show_phantom_label.setGeometry(0,0,32,32)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(32,32,Qt.KeepAspectRatio,Qt.FastTransformation))
              self.ui.label_11.setPixmap(self.pixmap_of_phantom.scaled(32,32,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("128x128"):
              self.ui.show_phantom_label.setGeometry(0,0,128,128)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(128,128,Qt.KeepAspectRatio,Qt.FastTransformation))
              self.ui.label_11.setPixmap(self.pixmap_of_phantom.scaled(128,128,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("256x256"):
              self.ui.show_phantom_label.setGeometry(0,0,256,256)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(256,256,Qt.KeepAspectRatio,Qt.FastTransformation))
              self.ui.label_11.setPixmap(self.pixmap_of_phantom.scaled(256,256,Qt.KeepAspectRatio,Qt.FastTransformation))
          elif str(selected_size)== ("512x512"):
              self.ui.show_phantom_label.setGeometry(0,0,512,512)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
              self.ui.label_11.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
          self.resetPlot()
          self.resetPainting()

 ##########################################################################################################################################
 ##########################################################################################################################################
    

    def getValueFromLine_edit_te(self):
        self.te= int(self.ui.lineEdit_2.text())
        self.vLine1.setPos(self.te)
        self.vLine3.setPos(self.te)
        self.te_entry_flag=True

        
    def getValueFromLine_edit_tr(self):
        self.tr=int(self.ui.lineEdit_3.text())
        self.vLine2.setPos(self.tr)
        self.vLine4.setPos(self.tr)
        self.tr_entry_flag=True
        
        
    def getValueFromLine_edit_flipAngle(self):
        self.flipAngle=int(self.ui.lineEdit_4.text())
        self.flipAngle_entry_flag=True
    
    
    
  ########################################################################################################################################## 
  ##########################################################################################################################################  
    
    def sheppLogan(self): 
          self.SHEPPLOGAN_FLAG = True
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
          self.default_width= self.ui.show_phantom_label.geometry().width()
          self.default_height= self.ui.show_phantom_label.geometry().height()

          
   ##########################################################################################################################################       
   ########################################################################################################################################## 
    def resetPainting(self):
       self.ui.pixel_counter == 0
       self.point1x = 0
       self.point1y = 0
       self.point2x = 0
       self.point2y = 0
       self.point3x = 0
       self.point3y = 0
       self.point4x = 0
       self.point4y = 0
       self.point5x = 0
       self.point5y = 0   
       self.ui.show_phantom_label.point=[]
       
       
    def resetPlot(self):
        self.ui.pixel_counter == 0
        self.t1_plotWindow.clear()
        self.t2_plotWindow.clear()
        self.vLine1 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine2 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine3 = pg.InfiniteLine(angle=90, movable=False)
        self.vLine4 = pg.InfiniteLine(angle=90, movable=False)
        self.t1_plotWindow.addItem(self.vLine1,ignoreBounds=True)
        self.t1_plotWindow.addItem(self.vLine2,ignoreBounds=True)
        self.t2_plotWindow.addItem(self.vLine3,ignoreBounds=True)
        self.t2_plotWindow.addItem(self.vLine4,ignoreBounds=True)


   ##########################################################################################################################################       
   ##########################################################################################################################################      
        
    
    # This is the filter used to catch mouse events exculesivly on label
    # source >> the target widget
    # event >> the mouse event passed
    
    def eventFilter(self, source, event):
        # checking whether the event is a mouse click and the target is the widget
        if event.type() == event.MouseButtonDblClick and source is self.ui.show_phantom_label:
            
            # Getting scaled height in case of resizing
            self.label_height=self.ui.show_phantom_label.geometry().height()
            # Getting scaled Width
            self.label_width=self.ui.show_phantom_label.geometry().width()
            
            # Calculating the ratio of scaling in both height and width
            self.height_scale=self.label_height/self.default_height
            self.width_scale=self.label_width/self.default_width
            # Getting mouse position 
            self.mouse_pos= event.pos()
            
            # Using the scaling ratio to retrieve the target pixel
            # Dividing and flooring the mouse position in X and Y coordinates by scaling factor
            # These 2 variables will be used to catch the intended pixel that the used clicked
            self.ui.pixel_clicked_x= math.floor(self.mouse_pos.x()/self.width_scale)
            self.ui.pixel_clicked_y= math.floor(self.mouse_pos.y()/self.height_scale)
            self.ui.label.setText("Matrix Index  "+"("+str(self.ui.pixel_clicked_y)+","+str(self.ui.pixel_clicked_x)+")")
            self.ui.label_2.setText("Pixel Coordinates  "+"("+str(self.mouse_pos.x())+","+str(self.mouse_pos.y())+")")
            
            # Plotting
            self.plot()
        
        elif event.type() == event.MouseButtonPress and QMouseEvent.button(event) == Qt.RightButton and source is self.ui.show_phantom_label:
            self.resetPlot()
            self.resetPainting()
            self.getValueFromSize_ComboBox()
            
        elif event.type() == event.Resize:
            # Getting scaled height in case of resizing
            self.label_height=self.ui.show_phantom_label.geometry().height()
            # Getting scaled Width
            self.label_width=self.ui.show_phantom_label.geometry().width()
            # Calculating the ratio of scaling in both height and width
            self.height_scale=self.label_height/self.default_height
            self.width_scale=self.label_width/self.default_width
            
            self.ui.show_phantom_label.point=[]
            if self.point1x != 0 and self.point1y != 0:
                self.ui.show_phantom_label.point.append([self.point1x*self.width_scale,self.point1y*self.height_scale,QtCore.Qt.red])
            if self.point2x != 0 and self.point2y != 0:
                self.ui.show_phantom_label.point.append([self.point2x*self.width_scale,self.point2y*self.height_scale,QtCore.Qt.green])
            if self.point3x != 0 and self.point3y != 0:
                self.ui.show_phantom_label.point.append([self.point3x*self.width_scale,self.point3y*self.height_scale,QtCore.Qt.blue])
            if self.point4x != 0 and self.point4y != 0:
                self.ui.show_phantom_label.point.append([self.point4x*self.width_scale,self.point4y*self.height_scale,QtCore.Qt.yellow])
            if self.point5x != 0 and self.point5y != 0:
                self.ui.show_phantom_label.point.append([self.point5x*self.width_scale,self.point5y*self.height_scale,QtCore.Qt.magenta])
            else: pass
            
        return super(ApplicationWindow, self).eventFilter(source, event)
        
        
    @pyqtSlot()
    def on_size_change(self):
        self.getValueFromSize_ComboBox()
        
    @pyqtSlot()
    def on_property_change(self):
        self.getValueFromProperties_ComboBox()
        
    @pyqtSlot()
    def on_lineEdit_change_te(self):
        self.getValueFromLine_edit_te()
        self.ui.generate_button.setEnabled(True)
        self.ui.inverseFourier_label.setText(" ")
        
    @pyqtSlot()
    def on_lineEdit_change_tr(self):
        self.getValueFromLine_edit_tr()
        self.ui.generate_button.setEnabled(True)
        self.ui.inverseFourier_label.setText(" ")
    
    @pyqtSlot()
    def on_lineEdit_change_flipAngle(self):
        self.getValueFromLine_edit_flipAngle()
        self.ui.generate_button.setEnabled(True)
        self.ui.inverseFourier_label.setText(" ")
    
    
    
 ##########################################################################################################################################
 ##########################################################################################################################################
    
    # Plot function
    def plot(self):
        
        self.ui.show_phantom_label.paint=True
        # Coloring the curve
        if self.ui.pixel_counter == 0:  
            red=255
            green=0
            blue=0
           
            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.red])
            self.point1x = self.mouse_pos.x()
            self.point1y = self.mouse_pos.y()
            
        elif self.ui.pixel_counter == 1:  
            red=0
            green=255
            blue=0

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.green])
            self.point2x = self.mouse_pos.x()
            self.point2y = self.mouse_pos.y()
            
        elif self.ui.pixel_counter == 2:
            red=0
            green=0
            blue=255

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.blue])
            self.point3x = self.mouse_pos.x()
            self.point3y = self.mouse_pos.y()
            
        elif self.ui.pixel_counter == 3:      
            red=255
            green=255
            blue=0

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.yellow])
            self.point4x = self.mouse_pos.x()
            self.point4y = self.mouse_pos.y()
            
        elif self.ui.pixel_counter == 4:
            red=255
            green=0
            blue=255

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.magenta])
            self.point5x = self.mouse_pos.x()
            self.point5y = self.mouse_pos.y()

            
        # A time array from 1 to 1000 seconds
        t= np.arange(1000)
        # T1 equation
        t1_plot=[]
        if self.T1[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x] == 0:
            self.T1[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]= self.epsilon
        t1_plot= 1 - np.exp(-t/self.T1[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x])   # Replace self.ui.t1 with the T1
        # T2 equation
        t2_plot=[]
        if self.T2[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x] == 0:
            self.T2[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]= self.epsilon
        t2_plot= np.exp(-t/self.T2[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x])   #Replace the self.ui.t2 with the T2
        # Checking if no more than 5 pixels are chosen
        if self.ui.pixel_counter<5:
            # Plotting T1
            self.t1_plotWindow.plot(t1_plot,pen=(red,green,blue),name="T1")
            self.t1_plotWindow.showGrid(x=True, y=True)
            
            # Plotting T2
            self.t2_plotWindow.plot(t2_plot,pen=(red,green,blue),name="T2")
            self.t2_plotWindow.showGrid(x=True, y=True)
            
            
            self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]))
            self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]))
            
           
            # Incrementing the pixel_counter
            self.ui.pixel_counter+=1
        else:
            # Now if more than 5 pixels are picked, clear both widgets and start over
            self.ui.show_phantom_label.point=[]
           # self.ui.show_phantom_label.paint=False
            self.resetPlot()
            self.resetPainting()
            red=255
            green=0
            blue=0
            
            self.point1x = self.mouse_pos.x()
            self.point1y = self.mouse_pos.y()
            # Plotting
            self.t1_plotWindow.plot(t1_plot,pen=(red,green,blue),name="T1")
            self.t1_plotWindow.showGrid(x=True, y=True)
            self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            self.t2_plotWindow.plot(t2_plot,pen=(red,green,blue),name="T2")
            self.t2_plotWindow.showGrid(x=True, y=True)
            self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.red])
                      
            # Reseting the counter to 1
            self.ui.pixel_counter=1
            
            
  ##########################################################################################################################################          
  ##########################################################################################################################################          

    def readCoordinates(self,event):
            self.xx=event.pos().x()
            self.yy=event.pos().y()
            
  ##########################################################################################################################################         
  ##########################################################################################################################################          
            
            
    def brightness(self,event):
        PropertyOfPhantom=self.ui.properties_comboBox.currentText()
        x = int(event.pos().x())
        y = int(event.pos().y())
        if str(PropertyOfPhantom)== ("T1"):  
              self.im = Image.fromarray(self.T1)
              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)  
        elif str(PropertyOfPhantom)== ("Proton Density"):
              self.im = Image.fromarray(self.I)
        else:  
              self.im = Image.fromarray(self.T2)
        
        
        self.im = self.im.convert("L")
        bightness = ImageEnhance.Brightness(self.im)
        contrast = ImageEnhance.Contrast(self.im)

        if self.xx < x and y<y+5 and y>y-5:
            self.ratio += 0.01
            enhanced_img = bightness.enhance(self.ratio)
            enhanced_img.save('task.png')
            self.im = Image.open('task.png')
            pixmap = QPixmap('task.png')
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            self.ui.show_phantom_label.setScaledContents(True)
            self.ui.show_phantom_label.setPixmap(image)

        elif self.xx > x and y<y+5 and y>y-5:
            self.ratio -= 0.01
            enhanced_img = bightness.enhance(self.ratio)
            enhanced_img.save('task.png')
            self.im = Image.open('task.png')
            pixmap = QPixmap('task.png')
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            self.ui.show_phantom_label.setScaledContents(True)
            self.ui.show_phantom_label.setPixmap(image)

        elif self.yy < y and x< x+5 and x> x-5:
            self.ratio += 0.01
            enhanced_img = contrast.enhance(self.ratio)
            enhanced_img.save('task.png')
            self.im = Image.open('task.png')
            pixmap = QPixmap('task.png')
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            self.ui.show_phantom_label.setScaledContents(True)
            self.ui.show_phantom_label.setPixmap(image)

        elif self.yy > y and x<x+5 and x>x-5:
            self.ratio -= 0.01
            enhanced_img = contrast.enhance(self.ratio)
            enhanced_img.save('task.png')
            self.im = Image.open('task.png')
            pixmap = QPixmap('task.png')
            image = pixmap.scaled(pixmap.width(), pixmap.height())
            self.ui.show_phantom_label.setScaledContents(True)
            self.ui.show_phantom_label.setPixmap(image)
       
            
##########################################################################################################################################
##########################################################################################################################################     
            
    def kSpace_generation(self):
            self.ui.generate_button.setEnabled(False)
            phantomSize = self.size_of_matrix_root

            T1 = self.T1
            T2 = self.T2

            flipAngle = self.flipAngle*np.pi/180

            TE = self.te
            TR = self.tr
            
            magneticVector = np.zeros((phantomSize, phantomSize, 3))

            magneticVector[0:phantomSize, 0:phantomSize, 0] = np.zeros((phantomSize, phantomSize))
            magneticVector[0:phantomSize, 0:phantomSize, 1] = np.zeros((phantomSize, phantomSize))
            magneticVector[0:phantomSize, 0:phantomSize, 2] = np.ones((phantomSize, phantomSize))
            
            cosine_flip_angle = np.cos(flipAngle)
            sine_flip_angle=np.sin(flipAngle)
            
            
            rotationAroundXMatrix = np.array([[1, 0, 0],
                                              [0, cosine_flip_angle, sine_flip_angle],
                                              [0, -sine_flip_angle, cosine_flip_angle]])
            
            
    
            self.kSpace = np.zeros((phantomSize, phantomSize), dtype=np.complex)
            
            for kSpaceRowIndex in range(phantomSize):    # Row Index for kSpace
                for j in range(phantomSize):
                    for k in range(phantomSize):
                        
                        if T2[j][k]==0:
                            T2[j][k] = self.epsilon
                        if T1[j][k] == 0:
                            T1[j][k] = self.epsilon
                        
                        magneticVector[j][k] = np.array([0, 0, 1-np.exp(-TR/T1[j][k])])
                        #magnetic Vector haysawy {0, 0, 1}
                        magneticVector[j][k] = np.matmul(rotationAroundXMatrix, magneticVector[j][k])
                        #magnetic Vector haysawy {0, 1, 0}
                        
                        first_term = np.exp(-TE / T2[j][k])
                        second_term = np.exp(-TE / T2[j][k])
                        third_term = np.exp(-TE / T1[j][k])
                        
                        decayMatrix = np.array([[first_term, 0, 0],
                                                [0, second_term, 0],
                                                [0, 0, third_term]])
            
                        magneticVector[j][k] = np.matmul(decayMatrix, magneticVector[j][k])
                        #magentic Vector {0, 0.5, 0}
            
                gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex
                
                for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                    gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex

                    for j in range(phantomSize):
                        for k in range(phantomSize):
                            alpha = gxStep*j + gyStep*k
                            magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                            self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude
                self.phantomFinal = self.kSpace
                self.kSpace1 = np.abs(self.kSpace)
                self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

                # Spoiler

                magneticVector[0:phantomSize][0:phantomSize][0] = 0
                magneticVector[0:phantomSize][0:phantomSize][1] = 0
                
                for j in range(phantomSize):
                    for k in range(phantomSize):
                        if T1[j][k] == 0:
                            magneticVector[j][k][2] = 1
                        else:
                            magneticVector[j][k][2] =  1 - np.exp(-TR / T1[j][k])
                        
            self.ui.convert_button.setEnabled(True)
       
        

##########################################################################################################################################
##########################################################################################################################################  
      
    def generate_Kspace(self):
        if self.tr_entry_flag and self.te_entry_flag and self.flipAngle_entry_flag:
            self.kSpaceThread = threading.Thread(target=self.kSpace_generation,args=())
            self.kSpaceThread.start()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("TE, TR or FlipAngle not entered!")
            msg.setInformativeText('Please enter their values')
            msg.setWindowTitle("Input Required!")
            msg.exec_()
        
        
##########################################################################################################################################
##########################################################################################################################################
    
    def inverseFourier(self):
        phantomFinal= self.phantomFinal
        phantomFinal = np.fft.fft2(self.kSpace)
        phantomFinal = np.abs(phantomFinal)
        phantomFinal = (phantomFinal-np.min(phantomFinal))*255/(np.max(phantomFinal)-np.min(phantomFinal))
        phantomFinal=qimage2ndarray.array2qimage(phantomFinal)
        phantomFinal=QPixmap.fromImage(phantomFinal)
        self.ui.inverseFourier_label.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
        self.ui.convert_button.setEnabled(False)

##########################################################################################################################################
##########################################################################################################################################

         
def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
