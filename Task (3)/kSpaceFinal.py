# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
# import cv2
from matplotlib import pyplot as plt

#phantomSize = 8
#
#T1 = np.full((phantomSize, phantomSize), 0)

#T1[0:2, 0:2] = np.full((2, 2), 1)
#T1[2:4, 2:4] = np.full((2, 2), 1)

#
#
#kidneyT1 = np.full((20, 75), 400)
#liverT1 = np.full((50, 35), 400)
#spleenT1 = np.full((30, 55), 550)
#fatT1 = np.full((10, 60), 250)
#intestineT1 = np.full((37, 20), 700)
#
#T1[20:40, 10:85] = kidneyT1
#T1[45:95, 90:125] = liverT1
#T1[90:120, 20:75] = spleenT1
#T1[5:15, 40:100] = fatT1
#T1[43:80, 30:50] = intestineT1
## to make it able to show as image
#T1 = (255*T1)/np.max(T1)
#
#T2 = np.full((phantomSize, phantomSize), 1)

#T1[0:2, 0:2] = np.full((2, 2), 0)
#T1[2:4, 2:4] = np.full((2, 2), 0)

#kidneyT2 = np.full((20, 75),  60)
#liverT2 = np.full((50, 35), 40)
#spleenT2 = np.full((30, 55), 60)
#fatT2 = np.full((10, 60), 70)
#intestineT2 = np.full((37, 20), 30)
#
#T2[20:40, 10:85] = kidneyT2
#T2[45:95, 90:125] = liverT2
#T2[90:120, 20:75] = spleenT2
#T2[5:15, 40:100] = fatT2
#T2[43:80, 30:50] = intestineT2
#
#T2 = (255*T2)/np.max(T2)

#T1 = np.resize(T1, (phantomSize, phantomSize))
#T2 = np.resize(T2, (phantomSize, phantomSize))


#T1 = np.full((phantomSize,phantomSize), 1000)
#T2 = np.full((phantomSize,phantomSize), 40)

phantomSize = 3



T1 = np.array([[1000,1280,2550],[1280,2550,1000],[2550,1000,1280]])
T2 = np.array([[30,40,50],[40,50,30],[50,30,40]])


flipAngle = 0.5*np.pi

TE = 20
TR = 5000


magneticVector = np.zeros((phantomSize, phantomSize, 3))

magneticVector[0:phantomSize, 0:phantomSize, 0] = np.zeros((phantomSize, phantomSize))
magneticVector[0:phantomSize, 0:phantomSize, 1] = np.zeros((phantomSize, phantomSize))
magneticVector[0:phantomSize, 0:phantomSize, 2] = np.ones((phantomSize, phantomSize))


rotationAroundXMatrix = np.array([[1, 0, 0],
                                  [0, np.cos(flipAngle), np.sin(flipAngle)],
                                  [0, -np.sin(flipAngle), np.cos(flipAngle)]])


kSpace = np.zeros((phantomSize, phantomSize), dtype=np.complex)

for kSpaceRowIndex in range(phantomSize):    # Row Index for kSpace
    for j in range(phantomSize):
        for k in range(phantomSize):
            
            #magnetic Vector haysawy {0, 0, 1}
            magneticVector[j][k] = np.matmul(rotationAroundXMatrix, magneticVector[j][k])
            #magnetic Vector haysawy {0, 1, 0}
            decayMatrix = np.array([[np.exp(-TE / T2[j][k]), 0, 0],
                                    [0, np.exp(-TE / T2[j][k]), 0],
                                    [0, 0, np.exp(-TE / T1[j][k])]])
            
            magneticVector[j][k] = np.matmul(decayMatrix, magneticVector[j][k])
            #magentic Vector {0, 0.5, 0}
            
    gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex

    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex

        for j in range(phantomSize):
            for k in range(phantomSize):
                alpha = gxStep*j + gyStep*k
                magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude

    # Spoiler

    magneticVector[0:phantomSize][0:phantomSize][0] = 0
    magneticVector[0:phantomSize][0:phantomSize][1] = 0

    for j in range(phantomSize):
        for k in range(phantomSize):
            magneticVector[j][k][2] =  1 - np.exp(-TR / T1[j][k])
    
    
phantomFinal = np.fft.ifft2(kSpace)

phantomFinal = np.abs(phantomFinal)

kSpace = np.abs(kSpace)


kSpace = (255*kSpace)/(np.max(kSpace))


print('K-Space')
plt.imshow(kSpace, cmap='gray')
plt.show()

print('Phantom Retrieved')
plt.imshow(phantomFinal, cmap='gray')
plt.show()


print(T1)
print(phantomFinal)