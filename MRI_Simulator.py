# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRI_Simulator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(952, 743)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(128, 128))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.browse_button = QtWidgets.QPushButton(self.tab)
        self.browse_button.setObjectName("browse_button")
        self.verticalLayout_3.addWidget(self.browse_button)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.properties_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.properties_comboBox.setObjectName("properties_comboBox")
        self.properties_comboBox.addItem("")
        self.properties_comboBox.addItem("")
        self.properties_comboBox.addItem("")
        self.gridLayout_4.addWidget(self.properties_comboBox, 0, 1, 1, 1)
        self.size_label = QtWidgets.QLabel(self.groupBox)
        self.size_label.setObjectName("size_label")
        self.gridLayout_4.addWidget(self.size_label, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 2, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 2, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.tab)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_8 = QtWidgets.QLabel(self.splitter_2)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.splitter_2)
        self.label_9.setText("")
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.splitter_2)
        self.graphicsView =PlotWidget(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.splitter_3 = QtWidgets.QSplitter(self.tab)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_10 = QtWidgets.QLabel(self.splitter_3)
        self.label_10.setText("")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.graphicsView_2 = PlotWidget(self.tab)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_2.addWidget(self.graphicsView_2)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.show_phantom_label = QtWidgets.QLabel(self.tab)
        self.show_phantom_label.setMinimumSize(QtCore.QSize(0, 0))
        self.show_phantom_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.show_phantom_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.show_phantom_label.setText("")
        self.show_phantom_label.setScaledContents(True)
        self.show_phantom_label.setAlignment(QtCore.Qt.AlignCenter)
        self.show_phantom_label.setObjectName("show_phantom_label")
        self.verticalLayout_4.addWidget(self.show_phantom_label)
        self.splitter = QtWidgets.QSplitter(self.tab)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.splitter)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 0, 3, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.generate_button = QtWidgets.QPushButton(self.tab_2)
        self.generate_button.setObjectName("generate_button")
        self.gridLayout_5.addWidget(self.generate_button, 1, 0, 1, 1)
        self.convert_button = QtWidgets.QPushButton(self.tab_2)
        self.convert_button.setObjectName("convert_button")
        self.gridLayout_5.addWidget(self.convert_button, 1, 1, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.widget = QtWidgets.QWidget(self.splitter_4)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_14.setFrameShape(QtWidgets.QFrame.Box)
        self.label_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_11.setText("")
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.widget1 = QtWidgets.QWidget(self.splitter_4)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_6.addWidget(self.label_13)
        self.kspace_label = QtWidgets.QLabel(self.widget1)
        self.kspace_label.setText("")
        self.kspace_label.setScaledContents(True)
        self.kspace_label.setObjectName("kspace_label")
        self.verticalLayout_6.addWidget(self.kspace_label)
        self.widget2 = QtWidgets.QWidget(self.splitter_4)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_12 = QtWidgets.QLabel(self.widget2)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_5.addWidget(self.label_12)
        self.inverseFourier_label = QtWidgets.QLabel(self.widget2)
        self.inverseFourier_label.setText("")
        self.inverseFourier_label.setScaledContents(True)
        self.inverseFourier_label.setObjectName("inverseFourier_label")
        self.verticalLayout_5.addWidget(self.inverseFourier_label)
        self.gridLayout_5.addWidget(self.splitter_4, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 952, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse_button.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Shepp-Logan Phantom"))
        self.groupBox.setTitle(_translate("MainWindow", "Phantom Properties"))
        self.label_3.setText(_translate("MainWindow", "Displayed Property"))
        self.properties_comboBox.setItemText(0, _translate("MainWindow", "T1"))
        self.properties_comboBox.setItemText(1, _translate("MainWindow", "T2"))
        self.properties_comboBox.setItemText(2, _translate("MainWindow", "Proton Density"))
        self.size_label.setText(_translate("MainWindow", "Size"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Default"))
        self.comboBox.setItemText(1, _translate("MainWindow", "32x32"))
        self.comboBox.setItemText(2, _translate("MainWindow", "128x128"))
        self.comboBox.setItemText(3, _translate("MainWindow", "256x256"))
        self.comboBox.setItemText(4, _translate("MainWindow", "512x512"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RF Properties"))
        self.label_4.setText(_translate("MainWindow", "Time to Echo"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "milliseconds"))
        self.label_5.setText(_translate("MainWindow", "Time to Repeat"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "milliseconds"))
        self.label_6.setText(_translate("MainWindow", "Flipping Angel"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Degrees"))
        self.label_8.setText(_translate("MainWindow", "T1 Plot"))
        self.label_7.setText(_translate("MainWindow", "T2 Plot"))
        self.label.setText(_translate("MainWindow", "Matrix Index"))
        self.label_2.setText(_translate("MainWindow", "Pixel Coordinates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Phantom"))
        self.generate_button.setText(_translate("MainWindow", "Generate K-space"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        self.label_14.setText(_translate("MainWindow", "Phantom"))
        self.label_13.setText(_translate("MainWindow", "K-Space representation"))
        self.label_12.setText(_translate("MainWindow", "Inverse Fourier"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "K-Space"))
