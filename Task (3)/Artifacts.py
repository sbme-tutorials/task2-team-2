#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 18:17:42 2019

@author: crow
"""

    def NonUnifromSampling_kspace(self):


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



            self.kSpace = np.zeros((phantomSize, phantomSize), dtype=np.complex)

            magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

#            if(self.INVERSTION_RECOVERY):
#
#                magneticVector = preparationSequences.inversionRecovery(magneticVector,phantomSize,T1,self.preparation_value,exponentialOfT1AndTR)
#
#            if(self.T2PREP):
#
#                magneticVector = preparationSequences.T2Prep(magneticVector, phantomSize, self.preparation_value, T2, T1)
#
#            if(self.TAGGING):
#
#                magneticVector = preparationSequences.Tagging(magneticVector, phantomSize, self.preparation_value)


            if(self.GRE):    #Value coming from comboBox indicating GRE
                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

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
                        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex


#                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, magneticVector, self.kSpace, kSpaceRowIndex, kSpaceColumnIndex)
                    for j in range(phantomSize):
                        for k in range(phantomSize):
                            if (k%2==0):
                                alpha = gxStep*j + gyStep*(k-1)
                            else:
                                alpha= gxStep*j + gyStep*(k)
                            magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                            self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude
                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

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


                magneticVector = functionsForTask3.startUpCycle (magneticVector, phantomSize, flipAngle, exponentialOfT1AndTR, self.numOfDumm)


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
                else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)

                for kSpaceRowIndex in range(phantomSize-1):

                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,((-1)**kSpaceRowIndex)*flipAngle/2,magneticVector)
                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
                    phaseEncodingMagneticVector = magneticVector
                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * (kSpaceRowIndex+1)
#                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, phaseEncodingMagneticVector, self.kSpace, kSpaceRowIndex+1, kSpaceColumnIndex)
                        for j in range(phantomSize):
                            for k in range(phantomSize):
                              if(k%2==0):
                                 alpha = gxStep*j + gyStep*(k-1)
                              else:
                                 alpha=gxStep*j+gyStep*k

                    magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                    kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)


            if(self.SE):      #Value coming from comboBox indicating SE

                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)
                for kSpaceRowIndex in range(phantomSize):

                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)
                    functionsForTask3.lookUpForDecay(phantomSize,T1,T2,TE/2,TR,exponentialOfT1AndTR,exponentialOfT1AndTE,exponentialOfT2AndTE,decayMatrices)

                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)


                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 0
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex
#                        magneticVector = functionsForTask3.rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector)
                            for j in range(phantomSize):
                                   for k in range(phantomSize):
                                       if(k%2==0):
                                           rotateX = np.array([[np.cos(gxStep*j), np.sin(gxStep*j), 0],
                                                               [-np.sin(gxStep*j), np.cos(gxStep*j), 0],
                                                               [0, 0, 1]])
                                           rotateY = np.array([[np.cos(gyStep*k), np.sin(gyStep*(k-1), 0],
                                                               [-np.sin(gyStep*k), np.cos(gyStep*(k-1), 0],
                                                               [0, 0, 1]])
                                          magneticVector[j][k] = np.matmul(rotateX, magneticVector[j][k])
                                          magneticVector[j][k] = np.matmul(rotateY, magneticVector[j][k])
                                       else:
                                           rotateX = np.array([[np.cos(gxStep*j), np.sin(gxStep*j), 0],
                                                               [-np.sin(gxStep*j), np.cos(gxStep*j), 0],
                                                               [0, 0, 1]])
                                           rotateY = np.array([[np.cos(gyStep*k), np.sin(gyStep*k), 0],
                                                               [-np.sin(gyStep*k), np.cos(gyStep*k), 0],
                                                               [0, 0, 1]])
                                          magneticVector[j][k] = np.matmul(rotateX, magneticVector[j][k])
                                          magneticVector[j][k] = np.matmul(rotateY, magneticVector[j][k])


                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi,magneticVector)
                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gxStep = 0
                        gyStep = 2 * np.pi / phantomSize * kSpaceColumnIndex
                        magneticVector = functionsForTask3.rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector)
                        summationX = np.sum(magneticVector[:][:][0])
                        summationY = np.sum(magneticVector[:][:][1])
                        magnitude = np.complex(summationX,summationY)
                        self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += magnitude

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, np.pi/2)



            self.ui.convert_button.setEnabled(True)


##########################################################################################################################################
##########################################################################################################################################
    def Aliasing_kspace(self):


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



            self.kSpace = np.zeros((phantomSize, phantomSize), dtype=np.complex)

            magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

#            if(self.INVERSTION_RECOVERY):
#
#                magneticVector = preparationSequences.inversionRecovery(magneticVector,phantomSize,T1,self.preparation_value,exponentialOfT1AndTR)
#
#            if(self.T2PREP):
#
#                magneticVector = preparationSequences.T2Prep(magneticVector, phantomSize, self.preparation_value, T2, T1)
#
#            if(self.TAGGING):
#
#                magneticVector = preparationSequences.Tagging(magneticVector, phantomSize, self.preparation_value)


            if(self.GRE):    #Value coming from comboBox indicating GRE
                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)

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
                        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex


#                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, magneticVector, self.kSpace, kSpaceRowIndex, kSpaceColumnIndex)
                    for j in range(phantomSize):
                        for k in range(phantomSize):
                                alpha= gxStep*j*3+ gyStep*(k*3)
                            magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                            self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude
                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

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


                magneticVector = functionsForTask3.startUpCycle (magneticVector, phantomSize, flipAngle, exponentialOfT1AndTR, self.numOfDumm)


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
                else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)

                for kSpaceRowIndex in range(phantomSize-1):

                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,((-1)**kSpaceRowIndex)*flipAngle/2,magneticVector)
                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)
                    phaseEncodingMagneticVector = magneticVector
                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 2*np.pi / phantomSize * kSpaceColumnIndex
                        gxStep = 2 * np.pi / phantomSize * (kSpaceRowIndex+1)
#                        functionsForTask3.gradientMultiplicationFunction(phantomSize,gxStep,gyStep, phaseEncodingMagneticVector, self.kSpace, kSpaceRowIndex+1, kSpaceColumnIndex)
                        for j in range(phantomSize):
                            for k in range(phantomSize):
                                 alpha = gxStep*(3*j) + gyStep*(3*k)

                    magnitude = np.sqrt(magneticVector[j][k][0]*magneticVector[j][k][0] + magneticVector[j][k][1]*magneticVector[j][k][1])
                    kSpace[kSpaceRowIndex][kSpaceColumnIndex] += np.exp(np.complex(0, alpha))*magnitude

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    if (self.current_port == 1):
                        self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    else: self.ui.kspace_label2.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))

                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, flipAngle/2)


            if(self.SE):      #Value coming from comboBox indicating SE

                magneticVector = functionsForTask3.multiplyingPD_ByMagneticVector(magneticVector,self.I,phantomSize,flipAngle,exponentialOfT1AndTR)
                for kSpaceRowIndex in range(phantomSize):

                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi/2,magneticVector)
                    functionsForTask3.lookUpForDecay(phantomSize,T1,T2,TE/2,TR,exponentialOfT1AndTR,exponentialOfT1AndTE,exponentialOfT2AndTE,decayMatrices)

                    magneticVector = functionsForTask3.decayFunction(phantomSize,decayMatrices,magneticVector)


                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gyStep = 0
                        gxStep = 2 * np.pi / phantomSize * kSpaceRowIndex
#                        magneticVector = functionsForTask3.rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector)
                        for j in range(phantomSize):
                                   for k in range(phantomSize):

                                           rotateX = np.array([[np.cos(gxStep*j), np.sin(gxStep*j*3), 0],
                                                               [-np.sin(gxStep*j), np.cos(gxStep*j*3), 0],
                                                               [0, 0, 1]])
                                           rotateY = np.array([[np.cos(gyStep*k), np.sin(gyStep*(k*3), 0],
                                                               [-np.sin(gyStep*k), np.cos(gyStep*(k*3), 0],
                                                               [0, 0, 1]])
                                          magneticVector[j][k] = np.matmul(rotateX, magneticVector[j][k])
                                          magneticVector[j][k] = np.matmul(rotateY, magneticVector[j][k])


                    magneticVector = functionsForTask3.rotationAroundXFunction(phantomSize,np.pi,magneticVector)
                    for kSpaceColumnIndex in range(phantomSize):        # Column Index for kSpace
                        gxStep = 0
                        gyStep = 2 * np.pi / phantomSize * kSpaceColumnIndex
                        magneticVector = functionsForTask3.rotationInXYPlaneFunction(phantomSize, gxStep, gyStep, magneticVector)
                        summationX = np.sum(magneticVector[:][:][0])
                        summationY = np.sum(magneticVector[:][:][1])
                        magnitude = np.complex(summationX,summationY)
                        self.kSpace[kSpaceRowIndex][kSpaceColumnIndex] += magnitude

                    self.phantomFinal = self.kSpace
                    self.kSpace1 = np.abs(self.kSpace)
                    self.kSpace1 = (self.kSpace1-np.min(self.kSpace1))*255/(np.max(self.kSpace1)-np.min(self.kSpace1))
                    pixmap_of_kspace=qimage2ndarray.array2qimage(self.kSpace1)
                    pixmap_of_kspace=QPixmap.fromImage(pixmap_of_kspace)
                    self.ui.kspace_label.setPixmap(pixmap_of_kspace.scaled(512,512,Qt.KeepAspectRatio,Qt.FastTransformation))
                    magneticVector = functionsForTask3.spoilerMatrix(phantomSize, magneticVector, exponentialOfT1AndTR, np.pi/2)



            self.ui.convert_button.setEnabled(True)


##########################################################################################################################################
##########################################################################################################################################