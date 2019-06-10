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
from PyQt5.QtGui import QPixmap, QMouseEvent, QFocusEvent
from PyQt5.QtCore import Qt, pyqtSlot, QEvent
from PyQt5.QtWidgets import QFileDialog,QMessageBox
import numpy as np
from MRI_Simulator import Ui_MainWindow,Label
import qimage2ndarray
import pyqtgraph as pg
import threading
import functionsForTask3
import graphicalRepresentation as gr
import ErnstAngle as ea
import Artifacts



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
        #connecting generate button with generating the k-space
        self.ui.generate_button.clicked.connect(self.generate_Kspace)
        #connecting convert button with converting ifft
        self.ui.convert_button.clicked.connect(self.inverseFourier)
        self.ui.convert_button.setEnabled(False)
        #connecting sheppLogan button with its function
        self.ui.pushButton_2.clicked.connect(self.sheppLogan)
        # Initializing Pixel clicked counter
        # Must not exceed 5
        self.clicks_counter=0

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
        self.ui.comboBox_2.currentIndexChanged.connect(self.on_sequence_change)
        self.ui.comboBox_3.currentIndexChanged.connect(self.on_preparation_change)
        self.ui.port_comboBox.currentIndexChanged.connect(self.port_selection)
        self.ui.ernst_comboBox.currentIndexChanged.connect(self.ernst_tissue_selection)
        self.ui.comboBox_4.currentIndexChanged.connect(self.artifact_selection)
        self.ui.show_phantom_label.mouseMoveEvent=self.brightness
        self.ui.show_phantom_label.mousePressEvent=self.readCoordinates
        self.ratio = 0
#        self.ui.show_phantom_label.mouseDoubleEvent=self.readCoordinates
#
        self.tr_entry_flag=False
        self.te_entry_flag=False
        self.flipAngle_entry_flag=False
        self.preparation_value_entry_flag=False


        self.epsilon = np.finfo(np.float32).eps
        self.imaginaryNumber = np.exp(np.complex(0, 1))

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
        self.ui.lineEdit_2.setFocusPolicy(Qt.ClickFocus)
        self.ui.lineEdit_3.setFocusPolicy(Qt.ClickFocus)
        self.ui.lineEdit_4.setFocusPolicy(Qt.ClickFocus)
        self.ui.preparation_lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.ui.lineEdit_2.editingFinished.connect(self.on_lineEdit_change_te)
        self.ui.lineEdit_3.editingFinished.connect(self.on_lineEdit_change_tr)
        self.ui.lineEdit_4.editingFinished.connect(self.on_lineEdit_change_flipAngle)
        self.ui.preparation_lineEdit.editingFinished.connect(self.on_lineEdit_change_preparation)
        self.ui.doubleSpinBox.valueChanged.connect(self.get_dumm_runs)

        self.ui.tabWidget.setCurrentIndex(0)

        self.SHEPPLOGAN_FLAG= False

        #Flags
        self.GRE=True
        self.SSFP=False
        self.SE=False
        self.INVERSION_RECOVERY=True
        self.T2PREP=False
        self.TAGGING=False

        self.FAT = False
        self.WHITE_MATTER = False
        self.GRAY_MATTER = False
        self.BLOOD = False

        self.__init__Sequence()
        self.__init__Preparation()

        self.ui.tabWidget.setTabEnabled(1,False)
        self.ui.tabWidget.setTabEnabled(2,False)
        self.ui.tabWidget.setTabEnabled(3,False)

        self.PHANTOM_OPENED = False
        self.ui.preparation_lineEdit.setEnabled(True)
        self.ui.preparation_label.setText("Inversion Time (ms)")
        self.PropertyOfPhantom = "T1"
        self.current_port = 1

        self.numOfDumm = 0

        self.mode = 1

        self.ui.ernst_comboBox.setEnabled(False)

        self.prep_type = 1



        #zoom related variables
        self.zoom=0
        self.drag_x=0
        self.drag_y=0
        self.ui.show_phantom_label.setFocusPolicy(Qt.StrongFocus)
        self.ui.label_11.setFocusPolicy(Qt.StrongFocus)
        




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
           self.default_width= self.ui.show_phantom_label.geometry().width()
           self.default_height= self.ui.show_phantom_label.geometry().height()
           self.resetPainting()
           self.resetPlot()
           self.getValueFromProperties_ComboBox()
           self.ui.generate_button.setEnabled(True)
           self.ui.inverseFourier_label.setText(" ")
           self.ui.kspace_label.setText(" ")
           self.ui.tabWidget.setTabEnabled(1,True)
           self.ui.tabWidget.setTabEnabled(2,True)
           self.ui.tabWidget.setTabEnabled(3,True)
           self.PHANTOM_OPENED = True


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

          self.PropertyOfPhantom=self.ui.properties_comboBox.currentText()

          if self.SHEPPLOGAN_FLAG==False:
           #show phantom according to chosen property
              if str(self.PropertyOfPhantom)== ("T1"):
                  self.phantom=qimage2ndarray.array2qimage(self.T1_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()

              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)
              elif str(self.PropertyOfPhantom)== ("Proton Density"):
                  self.phantom=qimage2ndarray.array2qimage(self.I_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              else:
                  self.phantom=qimage2ndarray.array2qimage(self.T2_mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
          else:
              if str(self.PropertyOfPhantom)== ("T1"):
                  self.phantom=qimage2ndarray.array2qimage(self.T1)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()

              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)
              elif str(self.PropertyOfPhantom)== ("Proton Density"):
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

          elif str(selected_size)== ("32x32"):
              self.ui.show_phantom_label.setGeometry(0,0,32,32)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(32,32,Qt.KeepAspectRatio,Qt.FastTransformation))

          elif str(selected_size)== ("64x64"):
              self.ui.show_phantom_label.setGeometry(0,0,64,64)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(64,64,Qt.KeepAspectRatio,Qt.FastTransformation))

          elif str(selected_size)== ("128x128"):
              self.ui.show_phantom_label.setGeometry(0,0,128,128)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(128,128,Qt.KeepAspectRatio,Qt.FastTransformation))

          elif str(selected_size)== ("256x256"):
              self.ui.show_phantom_label.setGeometry(0,0,256,256)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(256,256,Qt.KeepAspectRatio,Qt.FastTransformation))

          elif str(selected_size)== ("512x512"):
              self.ui.show_phantom_label.setGeometry(0,0,512,512)
              self.ui.show_phantom_label.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))


          self.ui.label_25.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
          self.ui.label_11.setPixmap(self.pixmap_of_phantom.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
          self.resetPlot()
          self.resetPainting()

     ##########################################################################################################################################
     ##########################################################################################################################################
    def getValueFromSequence_ComboBox(self):

        selected_sequence = self.ui.comboBox_2.currentText()

        if str(selected_sequence) == ("GRE"):
            self.GRE=True
            self.SSFP=False
            self.SE=False
            self.ui.ernst_graphicView.clear()
            if self.tr_entry_flag==True and self.flipAngle_entry_flag==True and self.preparation_value_entry_flag==True and self.te_entry_flag==True:
                self.ui.ernst_comboBox.setEnabled(True)
                self.ui.ernst_comboBox.setCurrentIndex(0)
        elif str(selected_sequence) == ("SSFP"):
            self.GRE=False
            self.SSFP=True
            self.SE=False
            self.ui.ernst_graphicView.clear()
            if self.tr_entry_flag==True and self.flipAngle_entry_flag==True and self.preparation_value_entry_flag==True and self.te_entry_flag==True:
                self.ui.ernst_comboBox.setEnabled(True)
                self.ui.ernst_comboBox.setCurrentIndex(0)
        elif str(selected_sequence) == ("SE"):
            self.GRE=False
            self.SSFP=False
            self.SE=True
            self.ui.ernst_graphicView.clear()
            self.ui.ernst_comboBox.setEnabled(False)
            self.ui.label_21.setText("Ernst Angle")



    def getValueFromPreparation_ComboBox(self):

        selected_preparation = self.ui.comboBox_3.currentText()

        if str(selected_preparation) == ("Inversion Recovery"):
            self.INVERSION_RECOVERY=True
            self.T2PREP=False
            self.TAGGING=False
            self.ui.preparation_label.setText("Inversion Time (ms)")
            self.prep_type = 1
        elif str(selected_preparation) == ("T2 Prep"):
            self.INVERSION_RECOVERY=False
            self.T2PREP=True
            self.TAGGING=False
            self.ui.preparation_label.setText("Time between Flips (ms)")
            self.prep_type = 2
        elif str(selected_preparation) == ("Tagging"):
            self.INVERSION_RECOVERY=False
            self.T2PREP=False
            self.TAGGING=True
            self.ui.preparation_label.setText("Spacing between Sine waves")
            self.prep_type = 3
        self.ui.preparation_lineEdit.setEnabled(True)

    ##########################################################################################################################################
    ##########################################################################################################################################

    def getValueFromLine_edit_te(self):
        try:
            self.te= int(self.ui.lineEdit_2.text())
            self.vLine1.setPos(self.te)
            self.vLine3.setPos(self.te)
            self.te_entry_flag=True
            if self.tr_entry_flag==True and self.flipAngle_entry_flag==True and self.preparation_value_entry_flag==True :
                self.ui.ernst_comboBox.setEnabled(True)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Only Integer")
            msg.setWindowTitle("Value Error")
            msg.exec_()

    def getValueFromLine_edit_tr(self):
        try:
            self.tr=int(self.ui.lineEdit_3.text())
            self.vLine2.setPos(self.tr)
            self.vLine4.setPos(self.tr)
            self.tr_entry_flag=True
            if self.te_entry_flag==True and self.flipAngle_entry_flag==True and self.preparation_value_entry_flag==True :
                self.ui.ernst_comboBox.setEnabled(True)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Only Integer")
            msg.setWindowTitle("Value Error")
            msg.exec_()


    def getValueFromLine_edit_flipAngle(self):
        try:
            self.flipAngle=int(self.ui.lineEdit_4.text())
            self.flipAngle_entry_flag=True
            if self.tr_entry_flag==True and self.te_entry_flag==True and self.preparation_value_entry_flag==True :
                self.ui.ernst_comboBox.setEnabled(True)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Only Integer")
            msg.setWindowTitle("Value Error")
            msg.exec_()



    def getValueFromLine_edit_preparation(self):
        try:
            self.preparation_value=int(self.ui.preparation_lineEdit.text())
            self.preparation_value_entry_flag=True
            self.clearPreparation()
            self.updatePreparation()
            if self.tr_entry_flag==True and self.flipAngle_entry_flag==True and self.te_entry_flag==True :
                self.ui.ernst_comboBox.setEnabled(True)
        except ValueError:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Only Integer")
            msg.setWindowTitle("Value Error")
            msg.exec_()



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
       self.clicks_counter = 0
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
        self.clicks_counter = 0
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
        if event.type() == event.MouseButtonDblClick and source is self.ui.show_phantom_label and self.PHANTOM_OPENED:


            # Getting scaled height in case of resizing
            self.label_height=self.ui.show_phantom_label.geometry().height()

            # Getting scaled Width
            self.label_width=self.ui.show_phantom_label.geometry().width()

            # Calculating the ratio of scaling in both height and width
            self.height_scale=self.label_height/self.size_of_matrix_root

            self.width_scale=self.label_width/self.size_of_matrix_root

            # Getting mouse position
            self.mouse_pos= event.pos()


            # Using the scaling ratio to retrieve the target pixel
            # Dividing and flooring the mouse position in X and Y coordinates by scaling factor
            # These 2 variables will be used to catch the intended pixel that the used clicked
            self.ui.pixel_clicked_x= math.floor(self.mouse_pos.x()/self.width_scale)

            self.ui.pixel_clicked_y= math.floor(self.mouse_pos.y()/self.height_scale)

            self.ui.label.setText("Matrix Index  "+"("+str(self.ui.pixel_clicked_x)+","+str(self.ui.pixel_clicked_y)+")")
            self.ui.label_2.setText("Pixel Coordinates  "+"("+str(self.mouse_pos.x())+","+str(self.mouse_pos.y())+")")



            # Plotting
            self.plot()

        elif event.type() == event.MouseButtonPress and QMouseEvent.button(event) == Qt.RightButton and source is self.ui.show_phantom_label and self.PHANTOM_OPENED:
            self.resetPlot()
            self.resetPainting()
            self.getValueFromSize_ComboBox()

        elif event.type() == event.Resize and source is self.ui.show_phantom_label and self.PHANTOM_OPENED:
            # Getting scaled height in case of resizing
            #self.label_height=self.ui.show_phantom_label.geometry().height()
            # Getting scaled Width
            #self.label_width=self.ui.show_phantom_label.geometry().width()
            # Calculating the ratio of scaling in both height and width
            self.height_scale = event.size().height() / event.oldSize().height()
            self.width_scale = event.size().width() / event.oldSize().width()

            self.ui.show_phantom_label.point=[]
            if self.point1x != 0 and self.point1y != 0:
                self.ui.show_phantom_label.point.append([self.point1x*self.width_scale,self.point1y*self.height_scale,QtCore.Qt.red])
                self.point1x = self.point1x*self.width_scale
                self.point1y = self.point1y*self.height_scale
            if self.point2x != 0 and self.point2y != 0:
                self.ui.show_phantom_label.point.append([self.point2x*self.width_scale,self.point2y*self.height_scale,QtCore.Qt.green])
                self.point2x = self.point2x*self.width_scale
                self.point2y = self.point2y*self.height_scale
            if self.point3x != 0 and self.point3y != 0:
                self.ui.show_phantom_label.point.append([self.point3x*self.width_scale,self.point3y*self.height_scale,QtCore.Qt.blue])
                self.point3x = self.point3x*self.width_scale
                self.point3y = self.point3y*self.height_scale
            if self.point4x != 0 and self.point4y != 0:
                self.ui.show_phantom_label.point.append([self.point4x*self.width_scale,self.point4y*self.height_scale,QtCore.Qt.yellow])
                self.point4x = self.point4x*self.width_scale
                self.point4y = self.point4y*self.height_scale
            if self.point5x != 0 and self.point5y != 0:
                self.ui.show_phantom_label.point.append([self.point5x*self.width_scale,self.point5y*self.height_scale,QtCore.Qt.magenta])
                self.point5x = self.point5x*self.width_scale
                self.point5y = self.point5y*self.height_scale

           # elif event.type() == QEvent.KeyPress and source is self.ui.show_phantom_label and self.PHANTOM_OPENED:

            else: pass


        return super(Label, self.ui.show_phantom_label).eventFilter(source, event)
#

    @pyqtSlot()
    def on_size_change(self):
        self.clicks_counter= 0
        self.getValueFromSize_ComboBox()

    @pyqtSlot()
    def on_property_change(self):
        self.clicks_counter= 0
        self.getValueFromProperties_ComboBox()

    @pyqtSlot()
    def on_sequence_change(self):
        self.getValueFromSequence_ComboBox()
        self.clearSequence()
        self.updateSequence()

    @pyqtSlot()
    def on_preparation_change(self):
        self.getValueFromPreparation_ComboBox()
        self.clearPreparation()
        self.updatePreparation()

    @pyqtSlot()
    def port_selection(self):
        current_port_string= self.ui.port_comboBox.currentText()
        if(current_port_string == "Port1"):
            self.current_port = 1
        elif (current_port_string == "Port2"):
            self.current_port = 2

    @pyqtSlot()
    def ernst_tissue_selection(self):
        selected_tissue = self.ui.ernst_comboBox.currentText()
        if (selected_tissue == "Fat"):
            self.ui.ernst_graphicView.clear()
            self.FAT = True
            self.WHITE_MATTER = False
            self.GRAY_MATTER = False
            self.BLOOD = False
            if self.GRE:
                ea.DrawErnstAngleGRE(self.tr,self.te,800,150,self.ui.ernst_graphicView,self.ui.label_21)
            elif self.SSFP:
                ea.DrawErnstAngleSSFP(self.size_of_matrix_root, self.tr, self.te, 800, 150,self.ui.ernst_graphicView,self.ui.label_21)
        elif (selected_tissue == "White Matter"):
            self.ui.ernst_graphicView.clear()
            self.WHITE_MATTER = True
            self.FAT = False
            self.GRAY_MATTER = False
            self.BLOOD = False
            if self.GRE:
                ea.DrawErnstAngleGRE(self.tr,self.te,200,50,self.ui.ernst_graphicView,self.ui.label_21)
            elif self.SSFP:
                ea.DrawErnstAngleSSFP(self.size_of_matrix_root, self.tr, self.te, 200, 50,self.ui.ernst_graphicView,self.ui.label_21)
        elif (selected_tissue == "Gray Matter"):
            self.ui.ernst_graphicView.clear()
            self.WHITE_MATTER = False
            self.FAT = False
            self.GRAY_MATTER = True
            self.BLOOD = False
            if self.GRE:
                ea.DrawErnstAngleGRE(self.tr,self.te,600,100,self.ui.ernst_graphicView,self.ui.label_21)
            elif self.SSFP:
                ea.DrawErnstAngleSSFP(self.size_of_matrix_root, self.tr, self.te, 600, 100,self.ui.ernst_graphicView,self.ui.label_21)
        elif (selected_tissue == "Blood"):
            self.ui.ernst_graphicView.clear()
            self.WHITE_MATTER = False
            self.FAT = False
            self.GRAY_MATTER = False
            self.BLOOD = True
            if self.GRE:
                ea.DrawErnstAngleGRE(self.tr,self.te,400,80,self.ui.ernst_graphicView,self.ui.label_21)
            elif self.SSFP:
                ea.DrawErnstAngleSSFP(self.size_of_matrix_root, self.tr, self.te, 400, 80,self.ui.ernst_graphicView,self.ui.label_21)
        else:
            self.WHITE_MATTER = False
            self.FAT = False
            self.GRAY_MATTER = False
            self.BLOOD = False
            self.ui.ernst_graphicView.clear()

    @pyqtSlot()
    def artifact_selection(self):
        current_artifact_string= self.ui.comboBox_4.currentText()
        if(current_artifact_string == "Aliasing"):
            Artifacts.Aliasing_kspace(self)
            self.ARTIFACT_1 = True
            self.ARTIFACT_2 = False
        elif (current_artifact_string == "Non-Uniform Sampling"):
            Artifacts.NonUnifromSampling_kspace(self)
            self.ARTIFACT_2 = True
            self.ARTIFACT_1 = False
        else:
            self.ARTIFACT_1 = False
            self.ARTIFACT_2 = False


    @pyqtSlot()
    def on_lineEdit_change_te(self):
        self.getValueFromLine_edit_te()
        self.ui.generate_button.setEnabled(True)


    @pyqtSlot()
    def on_lineEdit_change_tr(self):
        self.getValueFromLine_edit_tr()
        self.ui.generate_button.setEnabled(True)


    @pyqtSlot()
    def on_lineEdit_change_flipAngle(self):
        self.getValueFromLine_edit_flipAngle()
        self.ui.generate_button.setEnabled(True)


    @pyqtSlot()
    def on_lineEdit_change_preparation(self):
        self.getValueFromLine_edit_preparation()



    @pyqtSlot()
    def get_dumm_runs(self):
        self.numOfDumm = self.ui.doubleSpinBox.value()

 ##########################################################################################################################################
 ##########################################################################################################################################

    # Plot function
    def plot(self):

        self.ui.show_phantom_label.paint=True
        # Coloring the curve
        if self.clicks_counter == 0:
            red=255
            green=0
            blue=0

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.red])
            self.point1x = self.mouse_pos.x()
            self.point1y = self.mouse_pos.y()


        elif self.clicks_counter == 1:
            red=0
            green=255
            blue=0

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.green])
            self.point2x = self.mouse_pos.x()
            self.point2y = self.mouse_pos.y()


        elif self.clicks_counter == 2:
            red=0
            green=0
            blue=255

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.blue])
            self.point3x = self.mouse_pos.x()
            self.point3y = self.mouse_pos.y()

        elif self.clicks_counter == 3:
            red=255
            green=255
            blue=0

            self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.yellow])
            self.point4x = self.mouse_pos.x()
            self.point4y = self.mouse_pos.y()

        elif self.clicks_counter == 4:
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
        if self.clicks_counter<=4:
            # Plotting T1
            self.t1_plotWindow.plot(t1_plot,pen=(red,green,blue),name="T1")
            self.t1_plotWindow.showGrid(x=True, y=True)

            # Plotting T2
            self.t2_plotWindow.plot(t2_plot,pen=(red,green,blue),name="T2")
            self.t2_plotWindow.showGrid(x=True, y=True)


            self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]))
            self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_y,self.ui.pixel_clicked_x]))


            # Incrementing the clicks_counter
            self.clicks_counter+=1
        else:
            # Now if more than 5 pixels are picked, clear both widgets and start over
            self.ui.show_phantom_label.point=[]
           # self.ui.show_phantom_label.paint=False
            self.resetPlot()
            self.resetPainting()
            #red=255
            #green=0
            #blue=0

            #self.point1x = self.mouse_pos.x()
            #self.point1y = self.mouse_pos.y()
            # Plotting
            #self.t1_plotWindow.plot(t1_plot,pen=(red,green,blue),name="T1")
            #self.t1_plotWindow.showGrid(x=True, y=True)
            #self.ui.label_9.setText("T1= "+str(self.T1[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            #self.t2_plotWindow.plot(t2_plot,pen=(red,green,blue),name="T2")
            #self.t2_plotWindow.showGrid(x=True, y=True)
            #self.ui.label_10.setText("T2= "+str(self.T2[self.ui.pixel_clicked_x,self.ui.pixel_clicked_y]))
            #self.ui.show_phantom_label.point.append([self.mouse_pos.x(),self.mouse_pos.y(),QtCore.Qt.red])

            # Reseting the counter to 1
            self.clicks_counter=0
            self.plot()


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

#            self.sequenceChosen = 2             #Value coming from comboBox

            T1 = self.T1
            T2 = self.T2

            flipAngle = self.flipAngle*np.pi/180

            TE = self.te
            TR = self.tr

            magneticVector = np.zeros((phantomSize, phantomSize, 3))


            magneticVector[0:phantomSize, 0:phantomSize, 0] = np.zeros((phantomSize, phantomSize))
            magneticVector[0:phantomSize, 0:phantomSize, 1] = np.zeros((phantomSize, phantomSize))
            magneticVector[0:phantomSize, 0:phantomSize, 2] = np.ones((phantomSize, phantomSize))


            exponentialOfT1AndTR = np.zeros((phantomSize,phantomSize))
            exponentialOfT2AndTE = np.zeros((phantomSize,phantomSize))
            exponentialOfT1AndTE = np.zeros((phantomSize,phantomSize))
            decayMatrices = np.zeros((phantomSize,phantomSize,3,3))

            functionsForTask3.lookUpForDecay(phantomSize,T1,T2,TE,TR,exponentialOfT1AndTR,exponentialOfT1AndTE,exponentialOfT2AndTE,decayMatrices)

#            magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)



#            rotationAroundXMatrix = np.array([[1, 0, 0],
#                                              [0, np.cos(flipAngle), np.sin(flipAngle)],
#                                              [0, -np.sin(flipAngle), np.cos(flipAngle)]])



            self.kSpace = np.full((phantomSize, phantomSize), np.finfo(np.float32).eps, dtype=np.complex)
#            magneticVector = functionsForTask3.startUpCycle2 (magneticVector, phantomSize, flipAngle, T1, TR, decayMatrices, exponentialOfT1AndTR, int(self.numOfDumm))

#            magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

            if(self.INVERSION_RECOVERY):
#                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)
                magneticVector = functionsForTask3.inversionRecovery(magneticVector,phantomSize,T1,self.preparation_value)

            if(self.T2PREP):
#                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

                magneticVector = functionsForTask3.T2Prep(magneticVector, phantomSize, self.preparation_value, T2, T1)

            if(self.TAGGING):
#                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

                magneticVector = functionsForTask3.Tagging(magneticVector, phantomSize, self.preparation_value)
            magneticVector = functionsForTask3.startUpCycle2 (magneticVector, phantomSize, flipAngle, T1, TR, decayMatrices, exponentialOfT1AndTR, int(self.numOfDumm))

            if(self.GRE):    #Value coming from comboBox indicating GRE
#                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

                for kSpaceRowIndex in range(phantomSize):    # Row Index for kSpace


                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,flipAngle,magneticVector)
#                        if T2[j][k]==0:
#                            T2[j][k] = self.epsilon
#                        if T1[j][k] == 0:
#                            T1[j][k] = self.epsilon

#                magneticVector[j][k] = np.array([0, 0, 1-np.exp(-TR/T1[j][k])])
                        #magnetic Vector haysawy {0, 0, 1}
#                        magneticVector[j][k] = np.matmul(rotationAroundXMatrix, magneticVector[j][k])
                        #magnetic Vector haysawy {0, 1, 0}

                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)

#                        decayMatrix = np.array([[np.exp(-TE / T2[j][k]), 0, 0],
#                                                [0, np.exp(-TE / T2[j][k]), 0],
#                                                [0, 0, np.exp(-TE / T1[j][k])]])
#
#                        magneticVector[j][k] = np.matmul(decayMatrix, magneticVector[j][k])
                        #magentic Vector {0, 0.5, 0}

#                    gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex

                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 2 * np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex


                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, magneticVector, self.kSpace, kSpaceRowIndex, kSpaceColumnIndex)
#                    for j in range(phantomSize):
#                        for k in range(phantomSize):
#                            alpha = gxStep*j + gyStep*k
#                            magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
#                            self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude
                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label.setText(" ")
                    else:
                        self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label2.setText(" ")

                # Spoiler

#                    magneticVector[0:phantomSize][0:phantomSize][0] = 0
#                    magneticVector[0:phantomSize][0:phantomSize][1] = 0

                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle)

#                for j in range(phantomSize):
#                    for k in range(phantomSize):
#                        if T1[j][k] == 0:
#                            magneticVector[j][k][2] = 1
#                        else:
#                            magneticVector[j][k][2] =  1 - np.exp(-TR / T1[j][k])


#
 #           if(self.sequenceChosen == 2 ):      #Value coming from comboBox indicating GRE





            if(self.SSFP):      #Value coming from comboBox indicating SSFP


#                magneticVector = functionsForTask3.startUpCycle (magneticVector, phantomSize, flipAngle, exponentialOfT1AndTR, self.numOfDumm)


                magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,flipAngle/2,magneticVector)
                magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
                phaseEncodingMagneticVector = magneticVector
                for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                    gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                    gxStep = 2 * np.pi / phantomSize * 0
                    for j in range(phantomSize):
                        for k in range(phantomSize):

                            alpha = gxStep*j + gyStep*k
                            magnitude = np.sqrt(phaseEncodingMagneticVector[j][k][0]*phaseEncodingMagneticVector[j][k][0] + phaseEncodingMagneticVector[j][k][1]*phaseEncodingMagneticVector[j][k][1])
                            self.kSpace[0][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude

                self.phantomFinal = self.kSpace
                self.kSpace1 = np.abs(self.kSpace)
                self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label.setText(" ")
                else:
                        self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label2.setText(" ")
                magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)

                for kSpaceRowIndex in range(phantomSize-1):

                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,((-1)**kSpaceRowIndex)*flipAngle/2,magneticVector)
                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
                    phaseEncodingMagneticVector = magneticVector
                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * (kSpaceRowIndex+1)
                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, phaseEncodingMagneticVector, self.kSpace, kSpaceRowIndex+1, kSpaceColumnIndex)

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label.setText(" ")
                    else:
                        self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label2.setText(" ")

                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)


            if(self.SE):      #Value coming from comboBox indicating SE

                encodedVector = np.zeros((phantomSize,phantomSize,3))
                magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)
                
                for j in range(phantomSize):
                    for k in range (phantomSize):
                        gyStep = 2 * np.pi / phantomSize * k
                        gxStep = 2 * np.pi / phantomSize * j
                        
                magneticVector = functionsForTask3.rotationInXYPlaneFunction2(phantomSize, gxStep, gyStep, magneticVector)

                magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi,magneticVector)


#                functionsForTask3.lookUpForDecay(phantomSize,T1,T2,TE/2,TR,exponentialOfT1AndTR,exponentialOfT1AndTE,exponentialOfT2AndTE,decayMatrices)
                for kSpaceRowIndex in range(phantomSize):

#                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)

#                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
#                    gyStep = 2 * np.pi / phantomSize * kSpaceRowIndex
#                    for j in range(phantomSize):
#                        for k in range(phantomSize):
#                            magneticVector[j][k] = functionsForTask3.rotationInXYPlaneFunction(phantomSize, 0, gyStep, magneticVector[j][k], j, k)
                    
#                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
#                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi,magneticVector)


                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
#                        for j in range(phantomSize):
#                            for k in range(phantomSize):
#                                magneticVector[j][k] = functionsForTask3.rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector[j][k], j, k)
                        
                        gyStep = 2 * np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex

                        encodedVector = functionsForTask3.rotationInXYPlaneFunction2(phantomSize, gxStep, gyStep, magneticVector)


                        summationX = np.sum(encodedVector[:][:][0])
                        summationY = np.sum(encodedVector[:][:][1])
                        magnitude = np.complex(summationX,summationY)
                        self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += magnitude

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label.setText(" ")
                    else:
                        self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                        self.ui.inverseFourier_label2.setText(" ")

#                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, np.pi/2)

            self.ui.label_18.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

            self.ui.convert_button.setEnabled(True)



##########################################################################################################################################
##########################################################################################################################################

    def generate_Kspace(self):
        if self.tr_entry_flag and self.te_entry_flag and self.flipAngle_entry_flag and self.preparation_value_entry_flag:
            self.clearSequence()
            self.clearPreparation()
            self.updateSequence()
            self.updatePreparation()
            self.kSpaceThread = threading.Thread(target=self.kSpace_generation,args=())
            self.kSpaceThread.start()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("TE, TR, FlipAngle or Preparation Value not entered!")
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
        if (self.current_port == 1):
            self.ui.inverseFourier_label.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
        else: self.ui.inverseFourier_label2.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
        self.ui.convert_button.setEnabled(False)
        self.ui.label_19.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

##########################################################################################################################################
##########################################################################################################################################

    def __init__Sequence(self):

        self.layout = pg.GraphicsLayout(border=(100,100,100))
        self.ui.graphicsView_3.setCentralItem(self.layout)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.addLabel("Acquisition Sequence", colspan=3)


        self.layout.nextRow()
        self.layout.addLabel('RF', angle=-90, rowspan=1)
        self.rf_plot = self.layout.addPlot()
        self.rf_plot.showGrid(x=True, y=True)

        self.layout.nextRow()
        self.layout.addLabel('Gz', angle=-90, rowspan=1)
        self.gz_plot = self.layout.addPlot()
        self.gz_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Gy', angle=-90, rowspan=1)
        self.gy_plot = self.layout.addPlot()
        self.gy_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Gx', angle=-90, rowspan=1)
        self.gx_plot = self.layout.addPlot()
        self.gx_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Readout', angle=-90, rowspan=1)
        self.readout_plot = self.layout.addPlot()
        self.readout_plot.showGrid(x=False, y=True)


        self.layout.nextRow()
        self.layout.addLabel("Time (Semi-log) ", col=1, colspan=2)

        ## hide axes on some plots
        self.rf_plot.hideAxis('bottom')
        self.gz_plot.hideAxis('bottom')
        self.gx_plot.hideAxis('bottom')
        self.gy_plot.hideAxis('bottom')
        self.readout_plot.hideAxis('bottom')

    def __init__Preparation(self):

        self.layout = pg.GraphicsLayout(border=(100,100,100))
        self.ui.preparation_gv.setCentralItem(self.layout)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.addLabel("Preparation Sequence", colspan=3)


        self.layout.nextRow()
        self.layout.addLabel('RF', angle=-90, rowspan=1)
        self.rf_preparation_plot = self.layout.addPlot()
        self.rf_preparation_plot.showGrid(x=True, y=True)

        self.layout.nextRow()
        self.layout.addLabel('Gz', angle=-90, rowspan=1)
        self.gz_preparation_plot = self.layout.addPlot()
        self.gz_preparation_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Gy', angle=-90, rowspan=1)
        self.gy_preparation_plot = self.layout.addPlot()
        self.gy_preparation_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Gx', angle=-90, rowspan=1)
        self.gx_preparation_plot = self.layout.addPlot()
        self.gx_preparation_plot.showGrid(x=True, y=True)


        self.layout.nextRow()
        self.layout.addLabel('Readout', angle=-90, rowspan=1)
        self.readout_preparation_plot = self.layout.addPlot()
        self.readout_preparation_plot.showGrid(x=False, y=True)


        self.layout.nextRow()
        self.layout.addLabel("Time (Semi-log) ", col=1, colspan=2)

        ## hide axes on some plots
        self.rf_preparation_plot.hideAxis('bottom')
        self.gz_preparation_plot.hideAxis('bottom')
        self.gx_preparation_plot.hideAxis('bottom')
        self.gy_preparation_plot.hideAxis('bottom')
        self.readout_preparation_plot.hideAxis('bottom')


##########################################################################################################################################
##########################################################################################################################################
    def updateSequence(self):
        self.rf_plot.setXRange(0,self.tr)
        self.gz_plot.setXRange(0,self.tr)
        self.gx_plot.setXRange(0,self.tr)
        self.gy_plot.setXRange(0,self.tr)
        self.readout_plot.setXRange(0,self.tr)
        gr.drawRF(self.rf_plot,self.tr,self.te,self.GRE,self.SSFP,self.SE)
        gr.drawGZ(self.gz_plot,self.mode,self.tr,self.te,self.GRE,self.SSFP,self.SE)
        gr.drawGX(self.gx_plot,self.mode,self.tr,self.te,self.GRE,self.SSFP,self.SE)
        gr.drawGY(self.gy_plot,self.mode,self.tr,self.te,self.GRE,self.SSFP,self.SE)
        gr.drawReadOut(self.readout_plot,self.mode,self.tr,self.te,self.GRE,self.SSFP,self.SE)
        gr.drawIndicators(self.rf_plot,self.gz_plot,self.gy_plot,self.gx_plot,self.readout_plot,self.tr,self.te,self.flipAngle)

    def updatePreparation(self):
        self.rf_preparation_plot.setXRange(0,self.tr)
        self.gz_preparation_plot.setXRange(0,self.tr)
        self.gx_preparation_plot.setXRange(0,self.tr)
        self.gy_preparation_plot.setXRange(0,self.tr)
        self.readout_preparation_plot.setXRange(0,self.tr)
        gr.drawPreparation(self.rf_preparation_plot,self.gz_preparation_plot, self.gx_preparation_plot, self.gy_preparation_plot, self.tr, self.prep_type, self.preparation_value)


    def clearSequence(self):
        self.rf_plot.clear()
        self.gz_plot.clear()
        self.gx_plot.clear()
        self.gy_plot.clear()
        self.readout_plot.clear()


    def clearPreparation(self):
        self.rf_preparation_plot.clear()
        self.gz_preparation_plot.clear()
        self.gx_preparation_plot.clear()
        self.gy_preparation_plot.clear()
        self.readout_preparation_plot.clear()

#        self.rf_plot.plot()
#        self.gz_plot.plot()
#        self.gx_plot.plot()
#        self.gy_plot.plot()
#        self.readout_plot.plot()


##########################################################################################################################################
######################################################################################################################################
    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_O:
            #self.zoom=self.zoom-1
            if self.zoom==0:
              pass
              #QMessageBox.question(self, 'Error', "No More ZoomOut allowed", QMessageBox.Ok)
            elif self.zoom==1:
                self.drag_x=0
                self.drag_y=0
                self.zoom=self.zoom-1
                
            else:
              self.zoom=self.zoom-1
            
        if event.key() == QtCore.Qt.Key_I:
            self.zoom=self.zoom+1
           # if self.size_of_matrix_root-self.zoom+self.drag_y ==self.size_of_matrix_root:
            if self.size_of_matrix_root+1-self.zoom*2 == 2:
                pass
              #QMessageBox.question(self, 'Error', "No More Zoom-In is allowed", QMessageBox.Ok)
#            else:
#              self.zoom=self.zoom+1

            
        if event.key() == QtCore.Qt.Key_S:
            if self.size_of_matrix_root-self.zoom+self.drag_x ==self.size_of_matrix_root:
             # QMessageBox.question(self, 'Error', "No More Drag is allowed", QMessageBox.Ok)
                 pass
            else:
                self.drag_x=self.drag_x+1
            
        if event.key() == QtCore.Qt.Key_W:

            if self.zoom+self.drag_x== 0:
                pass
             # QMessageBox.question(self, 'Error', "No More Drag is allowed", QMessageBox.Ok)
            else:
              self.drag_x=self.drag_x-1
            
        if event.key() == QtCore.Qt.Key_D:
            
            if self.size_of_matrix_root-self.zoom+self.drag_y ==self.size_of_matrix_root:
             # QMessageBox.question(self, 'Error', "No More Drag is allowed", QMessageBox.Ok)
               pass
            else:
              self.drag_y=self.drag_y+1

        if event.key() == QtCore.Qt.Key_A:
            if self.zoom+self.drag_y== 0:
             # QMessageBox.question(self, 'Error', "No More Drag is allowed", QMessageBox.Ok)
                 pass 
            else:
                self.drag_y=self.drag_y-1


#        if event.key() == QtCore.Qt.Key_O:
#            if self.zoom >= 1:
#              self.zoom=self.zoom-1
#            else: pass
#
#        if event.key() == QtCore.Qt.Key_I:
#            if self.zoom <= 10:
#                self.zoom=self.zoom+1
#            else: pass
#
#        if event.key() == QtCore.Qt.Key_S:
#            if self.size_of_matrix_root-self.zoom+self.drag_x < self.size_of_matrix_root:
#                self.drag_x=self.drag_x+1
#            else: pass
#
#        if event.key() == QtCore.Qt.Key_W:
#            if self.zoom+self.drag_x > 0:
#              self.drag_x=self.drag_x-1
#            else: pass
#
#        if event.key() == QtCore.Qt.Key_D:
#            if self.size_of_matrix_root-self.zoom+self.drag_y < self.size_of_matrix_root:
#              self.drag_y=self.drag_y+1
#            else: pass
#
#        if event.key() == QtCore.Qt.Key_A:
#            if self.zoom+self.drag_y > 0:
#                self.drag_y=self.drag_y-1
#            else:pass

        PropertyOfPhantom=self.ui.properties_comboBox.currentText()

        if self.SHEPPLOGAN_FLAG==False:
           #show phantom according to chosen property
              if str(PropertyOfPhantom)== ("T1"):
                  self.ZOOMED=self.T1_mapped [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]
                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()

              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)
              elif str(PropertyOfPhantom)== ("Proton Density"):
                  self.ZOOMED_I=self.I_mapped [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]

                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED_I)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              else:
                  self.ZOOMED_T2mapped=self.T2_mapped [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]

                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED_T2mapped)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
        else:
              if str(PropertyOfPhantom)== ("T1"):
                  self.ZOOMED=self.T1 [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]

                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()

              #self.ui.show_phantom_label.setPixmap(pixmap_of_phantom)
              elif str(PropertyOfPhantom)== ("Proton Density"):
                  self.ZOOMED=self.I [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]
                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
              else:
                  self.ZOOMED=self.T2 [self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]
                  self.phantom=qimage2ndarray.array2qimage(self.ZOOMED)
                  self.pixmap_of_phantom=QPixmap.fromImage(self.phantom)
                  self.getValueFromSize_ComboBox()
        self.Kspace1zoomed=self.kSpace1[self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]
        pixmap_of_kspace=qimage2ndarray.array2qimage(self.Kspace1zoomed)
        pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
        if (self.current_port == 1):
                  self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                  self.ui.inverseFourier_label.setText(" ")
        else:
                  self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                  self.ui.inverseFourier_label2.setText(" ")
                  
                  #zoom in inverse fourier
        phantomFinal= self.phantomFinal
        phantomFinal = np.fft.fft2(self.kSpace)
        phantomFinal = np.abs(phantomFinal)
        phantomFinal = (phantomFinal-np.min(phantomFinal))*255/(np.max(phantomFinal)-np.min(phantomFinal))
        phantomfinal_zoomed=phantomFinal[self.zoom+self.drag_x:self.size_of_matrix_root-self.zoom+self.drag_x,self.zoom+self.drag_y:self.size_of_matrix_root-self.zoom+self.drag_y  ]
        phantomFinal=qimage2ndarray.array2qimage(phantomfinal_zoomed)
        phantomFinal=QPixmap.fromImage(phantomFinal)
        if (self.current_port == 1):
                 self.ui.inverseFourier_label.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
        else: self.ui.inverseFourier_label2.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
        #self.ui.convert_button.setEnabled(False)
        self.ui.label_19.setPixmap(phantomFinal.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))









##########################################################################################################################################
##########################################################################################################################################


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()