# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 14:01:34 2019

@author: Gamila
"""

import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
from  phantomsGUI import Ui_MainWindow
import sys
import numpy as np
from PIL import Image
from pyqtgraph import PlotWidget

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)









def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
