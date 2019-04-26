"""
Demonstrate the use of layouts to control placement of multiple plots / views /
labels


"""



from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np

app = QtGui.QApplication([])
view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
view.setCentralItem(l)
view.show()
view.setWindowTitle('Customized')
view.resize(800,600)



## Add a sub-layout into the second row (automatic position)
## The added item should avoid the first column, which is already filled
l.nextRow()
l2 = l.addLayout(colspan=3, border=(50,0,0))
l2.setContentsMargins(10, 10, 10, 10)
l2.addLabel("Graphical Representation of used sequence", colspan=3)

l2.nextRow()
l2.addLabel('RF', angle=-90, rowspan=1)
p21 = l2.addPlot()

l2.nextRow()
l2.addLabel('Gz', angle=-90, rowspan=1)
p22 = l2.addPlot()

l2.nextRow()
l2.addLabel('Gx', angle=-90, rowspan=1)
p23 = l2.addPlot()

l2.nextRow()
l2.addLabel('Gy', angle=-90, rowspan=1)
p24 = l2.addPlot()

l2.nextRow()
l2.addLabel('Readout', angle=-90, rowspan=1)
p26 = l2.addPlot()

l2.nextRow()
l2.addLabel("Time", col=1, colspan=2)

## hide axes on some plots
p21.hideAxis('bottom')
p22.hideAxis('bottom')
p23.hideAxis('bottom')
p24.hideAxis('bottom')

view.show()

## Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
