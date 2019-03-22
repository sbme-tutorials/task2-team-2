# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:26:23 2019

@author: Gamila
"""
import numpy as np
import matplotlib.pyplot as pl
from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication
from PyQt5 import  QtCore
from PyQt5.QtGui import QPixmap
import sys
import qimage2ndarray


square_phantom = np.zeros ((32,32))

kidney =np.full((5,5 ), 255) 
liver=np.full((3,3), 200)
spleen=np.full((6,6), 100)
fat=np.full((7,7), 50)

## adding tissues to the phantom
square_phantom [1:6, 2:7]=kidney
square_phantom [9:12, 9:12]=liver
square_phantom [14:20, 14:20]=spleen
square_phantom [ 21:28, 21:28]=fat

# assign T1 and T2 to each tissue 
T1=np.full((32,32), 0) 

kidneyT1 =np.full((5,5  ), 400) 
liverT1=np.full((3,3), 400)
spleenT1=np.full((6,6), 550)
fatT1=np.full((7,7), 250)

T1 [1:6, 2:7]=kidneyT1
T1[9:12, 9:12]=liverT1
T1[14:20, 14:20]=spleenT1
T1 [ 21:28, 21:28]=fatT1

#to make it able to show as image
T1= (255*T1)/np.max(T1)

T2=np.full((32,32 ), 0)  
kidneyT2 =np.full((5,5  ), 60) 
liverT2=np.full((3,3), 40)
spleenT2=np.full((6,6), 60)
fatT2=np.full((7,7), 70)


T2 [1:6, 2:7]=kidneyT2
T2[9:12, 9:12]=liverT2
T2[14:20, 14:20]=spleenT2
T2  [21:28, 21:28]=fatT2


T2= (255*T2)/np.max(T2)
#pl.imshow(T2 , cmap='gray', vmin=0, vmax=255)




class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Title")
        self.square_phantom = np.zeros ((32,32))

        kidney =np.full((5,5 ), 255) 
        liver=np.full((3,3), 200)
        spleen=np.full((6,6), 100)
        fat=np.full((7,7), 50)

## adding tissues to the phantom
        self.square_phantom [1:6, 2:7]=kidney
        self.square_phantom [9:12, 9:12]=liver
        self.square_phantom [14:20, 14:20]=spleen
        self.square_phantom [ 21:28, 21:28]=fat

# assign T1 and T2 to each tissue 
        self.T1=np.full((32,32), 0) 

        kidneyT1 =np.full((5,5  ), 400) 
        liverT1=np.full((3,3), 400)
        spleenT1=np.full((6,6), 550)
        fatT1=np.full((7,7), 250)

        self.T1 [1:6, 2:7]=kidneyT1
        self.T1[9:12, 9:12]=liverT1
        self.T1[14:20, 14:20]=spleenT1
        self.T1 [ 21:28, 21:28]=fatT1

#to make it able to show as image
        self.T1= (255*self.T1)/np.max(self.T1)

        self.T2=np.full((32,32 ), 0)  
        kidneyT2 =np.full((5,5  ), 60) 
        liverT2=np.full((3,3), 40)
        spleenT2=np.full((6,6), 60)
        fatT2=np.full((7,7), 70)


        self.T2 [1:6, 2:7]=kidneyT2
        self.T2[9:12, 9:12]=liverT2
        self.T2[14:20, 14:20]=spleenT2
        self.T2  [21:28, 21:28]=fatT2


        self.T2= (255*self.T2)/np.max(self.T2)
        
        label = QLabel(self)
        phantom=qimage2ndarray.array2qimage(self.T1)
        self.pixmap_of_phantom=QPixmap.fromImage(phantom)
        label.setPixmap(self.pixmap_of_phantom)
        #self.resize(self.pixmap_of_phantom.width(), self.pixmap_of_phantom.height())
        self.pixmap_of_phantom = self.pixmap_of_phantom.scaled(int(self.pixmap_of_phantom.height()), int(self.pixmap_of_phantom.width()), QtCore.Qt.KeepAspectRatio)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())