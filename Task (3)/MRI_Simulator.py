# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRI_Simulator.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 747)
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
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
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
        self.gridLayout_3.addWidget(self.groupBox, 1, 1, 1, 1)
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
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
        self.verticalLayout_12.addWidget(self.splitter_2)
        self.graphicsView = PlotWidget(self.tab)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_12.addWidget(self.graphicsView)
        self.horizontalLayout_7.addLayout(self.verticalLayout_12)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
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
        self.verticalLayout_13.addWidget(self.splitter_3)
        self.graphicsView_2 = PlotWidget(self.tab)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_13.addWidget(self.graphicsView_2)
        self.horizontalLayout_7.addLayout(self.verticalLayout_13)
        self.verticalLayout_14.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_21 = QtWidgets.QLabel(self.tab)
        self.label_21.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_8.addWidget(self.label_21)
        self.ernst_comboBox = QtWidgets.QComboBox(self.tab)
        self.ernst_comboBox.setObjectName("ernst_comboBox")
        self.ernst_comboBox.addItem("")
        self.ernst_comboBox.addItem("")
        self.ernst_comboBox.addItem("")
        self.ernst_comboBox.addItem("")
        self.ernst_comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.ernst_comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.ernst_graphicView = PlotWidget(self.tab)
        self.ernst_graphicView.setObjectName("ernst_graphicView")
        self.verticalLayout_2.addWidget(self.ernst_graphicView)
        self.verticalLayout_14.addLayout(self.verticalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_14, 2, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_4.addWidget(self.lineEdit)
        self.show_phantom_label = Label(self.centralwidget)
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
        self.splitter_6 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.widget = QtWidgets.QWidget(self.splitter_6)
        self.widget.setObjectName("widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_14 = QtWidgets.QLabel(self.widget)
        self.label_14.setMaximumSize(QtCore.QSize(16777215, 21))
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
        self.widget1 = QtWidgets.QWidget(self.splitter_6)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_13 = QtWidgets.QLabel(self.widget1)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_13.setFrameShape(QtWidgets.QFrame.Box)
        self.label_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_5.addWidget(self.label_13)
        self.splitter_4 = QtWidgets.QSplitter(self.widget1)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.kspace_label = QtWidgets.QLabel(self.splitter_4)
        self.kspace_label.setText("")
        self.kspace_label.setScaledContents(True)
        self.kspace_label.setObjectName("kspace_label")
        self.kspace_label2 = QtWidgets.QLabel(self.splitter_4)
        self.kspace_label2.setText("")
        self.kspace_label2.setObjectName("kspace_label2")
        self.verticalLayout_5.addWidget(self.splitter_4)
        self.widget2 = QtWidgets.QWidget(self.splitter_6)
        self.widget2.setObjectName("widget2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_12 = QtWidgets.QLabel(self.widget2)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_12.setFrameShape(QtWidgets.QFrame.Box)
        self.label_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_6.addWidget(self.label_12)
        self.splitter_5 = QtWidgets.QSplitter(self.widget2)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.inverseFourier_label = QtWidgets.QLabel(self.splitter_5)
        self.inverseFourier_label.setText("")
        self.inverseFourier_label.setScaledContents(True)
        self.inverseFourier_label.setObjectName("inverseFourier_label")
        self.inverseFourier_label2 = QtWidgets.QLabel(self.splitter_5)
        self.inverseFourier_label2.setText("")
        self.inverseFourier_label2.setObjectName("inverseFourier_label2")
        self.verticalLayout_6.addWidget(self.splitter_5)
        self.gridLayout_5.addWidget(self.splitter_6, 0, 0, 1, 3)
        self.port_comboBox = QtWidgets.QComboBox(self.tab_2)
        self.port_comboBox.setObjectName("port_comboBox")
        self.port_comboBox.addItem("")
        self.port_comboBox.addItem("")
        self.gridLayout_5.addWidget(self.port_comboBox, 1, 0, 1, 1)
        self.generate_button = QtWidgets.QPushButton(self.tab_2)
        self.generate_button.setObjectName("generate_button")
        self.gridLayout_5.addWidget(self.generate_button, 1, 1, 1, 1)
        self.convert_button = QtWidgets.QPushButton(self.tab_2)
        self.convert_button.setObjectName("convert_button")
        self.gridLayout_5.addWidget(self.convert_button, 1, 2, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setAccessibleName("")
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.graphicsView_3 = pg.GraphicsView(self.tab_3)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.gridLayout_7.addWidget(self.graphicsView_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_5.addWidget(self.lineEdit_3)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_6.addWidget(self.lineEdit_4)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.preparation_label = QtWidgets.QLabel(self.groupBox_2)
        self.preparation_label.setObjectName("preparation_label")
        self.horizontalLayout.addWidget(self.preparation_label)
        self.preparation_lineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.preparation_lineEdit.setEnabled(True)
        self.preparation_lineEdit.setObjectName("preparation_lineEdit")
        self.horizontalLayout.addWidget(self.preparation_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_22 = QtWidgets.QLabel(self.groupBox_2)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_9.addWidget(self.label_22)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setDecimals(0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_9.addWidget(self.doubleSpinBox)
        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 2, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 986, 22))
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
        self.label_8.setText(_translate("MainWindow", "T1 Plot"))
        self.label_7.setText(_translate("MainWindow", "T2 Plot"))
        self.label_21.setText(_translate("MainWindow", "Ernst Angle"))
        self.ernst_comboBox.setItemText(0, _translate("MainWindow", "Choose a tissue"))
        self.ernst_comboBox.setItemText(1, _translate("MainWindow", "Fat"))
        self.ernst_comboBox.setItemText(2, _translate("MainWindow", "White Matter"))
        self.ernst_comboBox.setItemText(3, _translate("MainWindow", "Gray Matter"))
        self.ernst_comboBox.setItemText(4, _translate("MainWindow", "Blood"))
        self.label.setText(_translate("MainWindow", "Matrix Index"))
        self.label_2.setText(_translate("MainWindow", "Pixel Coordinates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Phantom"))
        self.label_14.setText(_translate("MainWindow", "Phantom"))
        self.label_13.setText(_translate("MainWindow", "K-Space representation"))
        self.label_12.setText(_translate("MainWindow", "Reconstruction"))
        self.port_comboBox.setItemText(0, _translate("MainWindow", "Port1"))
        self.port_comboBox.setItemText(1, _translate("MainWindow", "Port2"))
        self.generate_button.setText(_translate("MainWindow", "Generate K-space"))
        self.convert_button.setText(_translate("MainWindow", "Convert"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "K-Space"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Sequence"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Artifacts"))
        self.groupBox_2.setTitle(_translate("MainWindow", "RF Properties"))
        self.label_4.setText(_translate("MainWindow", "Time to Echo"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "milliseconds"))
        self.label_5.setText(_translate("MainWindow", "Time to Repeat"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "milliseconds"))
        self.label_6.setText(_translate("MainWindow", "Flipping Angel"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Degrees"))
        self.label_16.setText(_translate("MainWindow", "Sequence"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "GRE"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "SSFP"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SE"))
        self.label_15.setText(_translate("MainWindow", "Preparation"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Inversion Recovery"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "T2 Prep"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Tagging"))
        self.preparation_label.setText(_translate("MainWindow", "Inversion Time"))
        self.label_22.setText(_translate("MainWindow", "No. of Dummy runs"))

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