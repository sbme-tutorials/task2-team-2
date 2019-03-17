# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phantomsGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(651, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.browse_button.setObjectName("browse_button")
        self.recovery_grapgh = PlotWidget(self.centralwidget)
        self.recovery_grapgh.setGeometry(QtCore.QRect(20, 350, 256, 192))
        self.recovery_grapgh.setObjectName("recovery_grapgh")
        self.decay_grapgh = plotWidget(self.centralwidget)
        self.decay_grapgh.setGeometry(QtCore.QRect(370, 350, 256, 192))
        self.decay_grapgh.setObjectName("decay_grapgh")
        self.path_of_file = QtWidgets.QLineEdit(self.centralwidget)
        self.path_of_file.setGeometry(QtCore.QRect(90, 20, 301, 20))
        self.path_of_file.setObjectName("path_of_file")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 90, 221, 111))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.label.setObjectName("label")
        self.phantom_size = QtWidgets.QComboBox(self.groupBox)
        self.phantom_size.setGeometry(QtCore.QRect(120, 40, 69, 22))
        self.phantom_size.setObjectName("phantom_size")
        self.phantom_size.addItem("")
        self.phantom_size.addItem("")
        self.phantom_size.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 91, 16))
        self.label_2.setObjectName("label_2")
        self.phantom_mode = QtWidgets.QComboBox(self.groupBox)
        self.phantom_mode.setGeometry(QtCore.QRect(120, 80, 69, 22))
        self.phantom_mode.setObjectName("phantom_mode")
        self.phantom_mode.addItem("")
        self.phantom_mode.addItem("")
        self.phantom_mode.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(420, 210, 221, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_5.setObjectName("label_5")
        self.TR_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.TR_edit.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.TR_edit.setObjectName("TR_edit")
        self.TE_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.TE_edit.setGeometry(QtCore.QRect(100, 30, 113, 20))
        self.TE_edit.setObjectName("TE_edit")
        self.FA_edit = QtWidgets.QLineEdit(self.groupBox_2)
        self.FA_edit.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.FA_edit.setObjectName("FA_edit")
        self.shepp_logan = QtWidgets.QPushButton(self.centralwidget)
        self.shepp_logan.setGeometry(QtCore.QRect(440, 60, 191, 23))
        self.shepp_logan.setObjectName("shepp_logan")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 651, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.groupBox.setTitle(_translate("MainWindow", "Phantom Properties"))
        self.label.setText(_translate("MainWindow", "Size"))
        self.phantom_size.setItemText(0, _translate("MainWindow", "128"))
        self.phantom_size.setItemText(1, _translate("MainWindow", "256"))
        self.phantom_size.setItemText(2, _translate("MainWindow", "512"))
        self.label_2.setText(_translate("MainWindow", "Displayed Property"))
        self.phantom_mode.setItemText(0, _translate("MainWindow", "PD"))
        self.phantom_mode.setItemText(1, _translate("MainWindow", "T1"))
        self.phantom_mode.setItemText(2, _translate("MainWindow", "T2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RF Properties"))
        self.label_3.setText(_translate("MainWindow", "Time-To-Echo"))
        self.label_4.setText(_translate("MainWindow", "Flip Angle"))
        self.label_5.setText(_translate("MainWindow", "Time-To-Repeat"))
        self.shepp_logan.setText(_translate("MainWindow", "Shepp-Logan Phantom"))

from pyqtgrapght import plotWidget
from pyqtgraph import PlotWidget
