#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:04:39 2019

@author: crow
"""


import numpy as np
import math
import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

def drawRF(rf_plot,recoveryTime,echoTime,GRE_FLAG,SSFP_FLAG,SE_FLAG):
    if GRE_FLAG:
        flat_line = np.full((recoveryTime+math.floor(recoveryTime*0.15),),-1)
        data = np.zeros((recoveryTime+math.floor(recoveryTime*0.15),))
        temp = np.full((2*math.ceil(recoveryTime*0.075),),0)
        flat_line[0:temp.size,] = temp
        flat_line[recoveryTime - math.ceil(recoveryTime*0.075) : recoveryTime + math.ceil(recoveryTime*0.075), ] = temp
        x = np.linspace(-6,6,math.floor(recoveryTime*0.15))
        equation = np.sin(2*x)/x
        data[0:equation.size,] = equation
        data[(recoveryTime - math.ceil(recoveryTime*0.075))+1 : (recoveryTime - math.ceil(recoveryTime*0.075))+1+equation.size, ] = equation
        rf = np.heaviside(flat_line,data)
        rf_plot.setXRange(0,recoveryTime)
        rf_plot.setYRange(-0.5,2)
        rf_plot.plot(rf/2)

    elif SSFP_FLAG:
        # flat_line is an array that's going to fill the whole x-axis of the plot (0:recoveryTime+recoveryTime*0.15)
        # The purpose of this array is to manipulate the plot using the function np.heaviside that takes another array
        # with the flat_line and the manipulation takes place in specific conditions
        #                                  0   if flat_line < 0
        # heaviside(flat_line, data) =  data   if flat_line == 0
        #                                  1   if flat_line > 0
        # temp is created to fill flat_line array with zeros at the specific indices I want to plot data at
        # that will achieve the above condition!
        # the variable x and equation are related to the sinc function drawing

        flat_line = np.full((recoveryTime+math.floor(recoveryTime*0.15),),-1)
        data = np.zeros((recoveryTime+math.floor(recoveryTime*0.15),))
        temp = np.full((2*math.ceil(recoveryTime*0.075),),0)
        flat_line[0:temp.size,] = temp
        flat_line[recoveryTime - math.ceil(recoveryTime*0.075) : recoveryTime + math.ceil(recoveryTime*0.075), ] = temp
        x = np.linspace(-6,6,math.floor(recoveryTime*0.15))
        equation = np.sin(2*x)/x
        data[0:equation.size,] = equation
        data[(recoveryTime - math.ceil(recoveryTime*0.075))+1 : recoveryTime + math.ceil(recoveryTime*0.075), ] = equation
        rf = np.heaviside(flat_line,data)
        rf_plot.setXRange(0,recoveryTime)
        rf_plot.setYRange(-0.5,2)
        rf_plot.plot(rf/2)

    elif SE_FLAG:
        TE_centerline = (math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15)
        flat_line = np.full((recoveryTime+math.floor(recoveryTime*0.15),),-1)
        data = np.zeros((recoveryTime+math.floor(recoveryTime*0.15),))
        temp = np.full((2*math.ceil(recoveryTime*0.075),),0)
        flat_line[0:math.ceil(temp.size/2),] = temp[0:math.ceil(temp.size/2)]
        flat_line[recoveryTime - math.ceil(recoveryTime*0.075) : recoveryTime + math.ceil(recoveryTime*0.075), ] = temp
        flat_line[math.ceil(TE_centerline/2 - recoveryTime*0.015)+1 : math.ceil(TE_centerline/2 - recoveryTime*0.015)+1+math.ceil(temp.size/2),] = temp[0:math.ceil(temp.size/2)]
        x = np.linspace(-6,6,math.floor(recoveryTime*0.075))
        equation = np.sin(2*x)/x
        data[0:equation.size,] = equation
        data[(recoveryTime - math.ceil(recoveryTime*0.075/2))+1 : recoveryTime + math.ceil(recoveryTime*0.075/2), ] = equation
        x = np.linspace(-6,6,math.floor(recoveryTime*0.15/2))
        equation = np.sin(2*x)/x
        data[math.ceil(TE_centerline/2 - recoveryTime*0.015)+1 : math.ceil(TE_centerline/2 - recoveryTime*0.015)+1+equation.size,] = 2*equation
        rf = np.heaviside(flat_line,data)
        rf_plot.setXRange(0,recoveryTime)
        rf_plot.setYRange(-0.5,2)
        rf_plot.plot(rf/2)



def drawGZ(gz_plot,mode,recoveryTime,echoTime,GRE_FLAG,SSFP_FLAG,SE_FLAG):
    if GRE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[0:temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        gz_plot.setXRange(0,recoveryTime)
        gz_plot.setYRange(-1,1)
        gz_plot.plot(step)
    elif SSFP_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        data = np.zeros((recoveryTime,))
        data[((recoveryTime - math.ceil(recoveryTime*0.075))+1) - math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075))+1),] = np.full((math.ceil(recoveryTime*0.15),),-1)
        temp = np.full((math.ceil(recoveryTime*0.15),),1)
        flat_line[0:temp.size,] = temp
        flat_line[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075))+1),] = np.zeros((math.ceil(recoveryTime*0.15),))
        gz = np.heaviside(flat_line,data)
        gz_plot.setXRange(0,recoveryTime)
        gz_plot.setYRange(-1,1)
        gz_plot.plot(gz)
    elif SE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[0:math.ceil(temp.size/2),] = temp[0:math.ceil(temp.size/2)]
        TE_centerline = (math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15)
        flat_line[math.ceil(TE_centerline/2 - recoveryTime*0.015)+1 : math.ceil(TE_centerline/2 - recoveryTime*0.015)+1+math.floor(recoveryTime*0.15/2),] = temp[0:math.floor(recoveryTime*0.15/2)]
        step = np.heaviside(flat_line,flat_line)
        gz_plot.setXRange(0,recoveryTime)
        gz_plot.setYRange(-1,1)
        gz_plot.plot(step)



def drawGY(gy_plot,mode,recoveryTime,echoTime,GRE_FLAG,SSFP_FLAG,SE_FLAG):
    if GRE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[math.floor(recoveryTime*0.15):math.floor(recoveryTime*0.15)+temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        gy_plot.setXRange(0,recoveryTime)
        gy_plot.setYRange(-1,1)
        gy_plot.plot(step)
    elif SSFP_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        data1 = np.zeros((recoveryTime,))
        data1[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.ones((math.ceil(recoveryTime*0.15),))
        data2 = np.zeros((recoveryTime,))
        data2[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),0.8)
        data3 = np.zeros((recoveryTime,))
        data3[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),0.6)
        data4 = np.zeros((recoveryTime,))
        data4[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),0.4)
        data5 = np.zeros((recoveryTime,))
        data5[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),0.2)
        data6 = np.zeros((recoveryTime,))
        data6[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),0)
        data7 = np.zeros((recoveryTime,))
        data7[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),-0.2)
        data8 = np.zeros((recoveryTime,))
        data8[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),-0.4)
        data9 = np.zeros((recoveryTime,))
        data9[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),-0.6)
        data10 = np.zeros((recoveryTime,))
        data10[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),-0.8)
        data11 = np.zeros((recoveryTime,))
        data11[math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15),] = np.full((math.ceil(recoveryTime*0.15),),-1)
        temp = np.full((math.floor(recoveryTime*0.15,)),0)
        flat_line[math.ceil(recoveryTime*0.15):math.ceil(recoveryTime*0.15)+temp.size,] = temp
        flat_line[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : (((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15))+temp.size,] = temp
        step1 = np.heaviside(flat_line,data1)
        step2 = np.heaviside(flat_line,data2)
        step3 = np.heaviside(flat_line,data3)
        step4 = np.heaviside(flat_line,data4)
        step5 = np.heaviside(flat_line,data5)
        step6 = np.heaviside(flat_line,data6)
        step7 = np.heaviside(flat_line,data7)
        step8 = np.heaviside(flat_line,data8)
        step9 = np.heaviside(flat_line,data9)
        step10 = np.heaviside(flat_line,data10)
        step11 = np.heaviside(flat_line,data11)
        gy_plot.setXRange(0,recoveryTime)
        gy_plot.setYRange(-1,1)
        gy_plot.plot(step1)
        gy_plot.plot(step2)
        gy_plot.plot(step3)
        gy_plot.plot(step4)
        gy_plot.plot(step5)
        gy_plot.plot(step6)
        gy_plot.plot(step7)
        gy_plot.plot(step8)
        gy_plot.plot(step9)
        gy_plot.plot(step10)
        gy_plot.plot(step11)
        arrow1 = pg.ArrowItem(angle=90, tipAngle=30, baseAngle=0, headLen=35, tailLen=None, brush=pg.mkBrush('g'), pen=pg.mkPen('g'))
        arrow1.setPos(3*math.ceil(recoveryTime*0.15)/2,1)
        gy_plot.addItem(arrow1)

        data12 = np.zeros((recoveryTime,))
        data12[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.ones((math.ceil(recoveryTime*0.15),))
        data13 = np.zeros((recoveryTime,))
        data13[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),0.8)
        data14 = np.zeros((recoveryTime,))
        data14[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),0.6)
        data15 = np.zeros((recoveryTime,))
        data15[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),0.4)
        data16 = np.zeros((recoveryTime,))
        data16[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),0.2)
        data17 = np.zeros((recoveryTime,))
        data17[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),0)
        data18 = np.zeros((recoveryTime,))
        data18[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),-0.2)
        data19 = np.zeros((recoveryTime,))
        data19[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),-0.4)
        data20 = np.zeros((recoveryTime,))
        data20[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),-0.6)
        data21 = np.zeros((recoveryTime,))
        data21[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),-0.8)
        data22 = np.zeros((recoveryTime,))
        data22[(((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15)) : ((recoveryTime - math.ceil(recoveryTime*0.075)))+1,] = np.full((math.ceil(recoveryTime*0.15),),-1)

        step12 = np.heaviside(flat_line,data12)
        step13= np.heaviside(flat_line,data13)
        step14 = np.heaviside(flat_line,data14)
        step15 = np.heaviside(flat_line,data15)
        step16 = np.heaviside(flat_line,data16)
        step17 = np.heaviside(flat_line,data17)
        step18 = np.heaviside(flat_line,data18)
        step19 = np.heaviside(flat_line,data19)
        step20 = np.heaviside(flat_line,data20)
        step21 = np.heaviside(flat_line,data21)
        step22 = np.heaviside(flat_line,data22)

        gy_plot.plot(step12)
        gy_plot.plot(step13)
        gy_plot.plot(step14)
        gy_plot.plot(step15)
        gy_plot.plot(step16)
        gy_plot.plot(step17)
        gy_plot.plot(step18)
        gy_plot.plot(step19)
        gy_plot.plot(step20)
        gy_plot.plot(step21)
        gy_plot.plot(step22)

        arrow2 = pg.ArrowItem(angle=-90, tipAngle=30, baseAngle=0, headLen=35, tailLen=None, brush=pg.mkBrush('r'), pen=pg.mkPen('r'))
        arrow2.setPos(((((recoveryTime - math.ceil(recoveryTime*0.075)))-(((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15)))/2)+(((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15)),-1)
        gy_plot.addItem(arrow2)

    elif SE_FLAG:
        TE_centerline = (math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15)
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[math.ceil(temp.size/2):math.ceil(TE_centerline/2 - recoveryTime*0.015)+1,] = temp[0:math.ceil(TE_centerline/2 - recoveryTime*0.015)+1 - math.ceil(temp.size/2)]
        step = np.heaviside(flat_line,flat_line)
        gy_plot.setXRange(0,recoveryTime)
        gy_plot.setYRange(-1,1)
        gy_plot.plot(step)




def drawGX(gx_plot,mode,recoveryTime,echoTime,GRE_FLAG,SSFP_FLAG,SE_FLAG):
    if GRE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((1,math.floor(recoveryTime*0.15)),1)
        flat_line[math.floor(2*recoveryTime*0.15):math.floor(2*recoveryTime*0.15)+temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        gx_plot.setXRange(0,recoveryTime)
        gx_plot.setYRange(-1,1)
        gx_plot.plot(step)
    elif SSFP_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        data = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+temp.size,] = temp
        temp = np.full((math.floor(recoveryTime*0.15),),0)
        flat_line[((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15) : (((recoveryTime - math.ceil(recoveryTime*0.075))+1)- math.ceil(recoveryTime*0.15))+temp.size,] = temp
        step = np.heaviside(flat_line,data)
        gx_plot.setXRange(0,recoveryTime)
        gx_plot.setYRange(-1,1)
        gx_plot.plot(step)
    if SE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((1,math.floor(recoveryTime*0.15)),1)
        flat_line[math.floor(2*recoveryTime*0.15):math.floor(2*recoveryTime*0.15)+temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        gx_plot.setXRange(0,recoveryTime)
        gx_plot.setYRange(-1,1)
        gx_plot.plot(step)



def drawReadOut(readout_plot,mode,recoveryTime,echoTime,GRE_FLAG,SSFP_FLAG,SE_FLAG):

    if GRE_FLAG:
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15,)),1)
        flat_line[math.floor(2*recoveryTime*0.15):math.floor(2*recoveryTime*0.15)+temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        readout_plot.setXRange(0,recoveryTime)
        readout_plot.setYRange(-1,1)
        readout_plot.plot(step)
    elif SSFP_FLAG:
        x = np.linspace(0,360,math.floor(recoveryTime*0.15))
        y = np.linspace(0,2,math.floor(recoveryTime*0.15))
        attenuatedSine = np.sin(10*x*np.pi/180)*np.exp(-y)
        data = np.zeros((recoveryTime,))
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),0)
        flat_line[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+temp.size,] = temp
        data[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+attenuatedSine.size,] = attenuatedSine
        step = np.heaviside(flat_line,data)
        readout_plot.setXRange(0,recoveryTime)
        readout_plot.setYRange(-1,1)
        readout_plot.plot(step)
    elif SE_FLAG:
        x = np.linspace(0,360,math.floor(recoveryTime*0.15))
        y = np.linspace(0,2,math.floor(recoveryTime*0.15))
        attenuatedSine = np.sin(10*x*np.pi/180)*np.exp(-y)
        data = np.zeros((recoveryTime,))
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),0)
        flat_line[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+temp.size,] = temp
        data[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+attenuatedSine.size,] = attenuatedSine
        step = np.heaviside(flat_line,data)
        readout_plot.setXRange(0,recoveryTime)
        readout_plot.setYRange(-1,1)
        readout_plot.plot(step)


def drawIndicators(rf_plot,gz_plot,gy_plot,gx_plot,readout_plot,recoveryTime,echoTime,flipAngle):
    ## Drawing lines for TE and TR
    vLine1 = pg.InfiniteLine(angle=90, movable=False)
    vLine2 = pg.InfiniteLine(angle=90, movable=False)
    vLine3 = pg.InfiniteLine(angle=90, movable=False)
    vLine4 = pg.InfiniteLine(angle=90, movable=False)
    vLine5 = pg.InfiniteLine(angle=90, movable=False)
    vLine1.setPos((math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15))
    vLine2.setPos((math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15))
    vLine3.setPos((math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15))
    vLine4.setPos((math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15))
    vLine5.setPos((math.floor(recoveryTime*0.15)/2)+2*math.ceil(recoveryTime*0.15))
    rf_plot.addItem(vLine1,ignoreBounds=True)
    gz_plot.addItem(vLine2,ignoreBounds=True)
    gy_plot.addItem(vLine3,ignoreBounds=True)
    gx_plot.addItem(vLine4,ignoreBounds=True)
    readout_plot.addItem(vLine5,ignoreBounds=True)
    vLine6 = pg.InfiniteLine(angle=90, movable=False)
    vLine7 = pg.InfiniteLine(angle=90, movable=False)
    vLine8 = pg.InfiniteLine(angle=90, movable=False)
    vLine9 = pg.InfiniteLine(angle=90, movable=False)
    vLine10 = pg.InfiniteLine(angle=90, movable=False)
    vLine6.setPos(recoveryTime)
    vLine7.setPos(recoveryTime)
    vLine8.setPos(recoveryTime)
    vLine9.setPos(recoveryTime)
    vLine10.setPos(recoveryTime)
    rf_plot.addItem(vLine6,ignoreBounds=True)
    gz_plot.addItem(vLine7,ignoreBounds=True)
    gy_plot.addItem(vLine8,ignoreBounds=True)
    gx_plot.addItem(vLine9,ignoreBounds=True)
    readout_plot.addItem(vLine10,ignoreBounds=True)

    ## Drawing Indicating text
    text1 = pg.TextItem(text="TE = " + str(echoTime), color= (0,200,0),anchor = (1,0), angle=0)
    text2 = pg.TextItem(text="TR = " + str(recoveryTime), color= (0,200,0),anchor = (1,0), angle=0)
    text3 = pg.TextItem(text="TE = " + str(echoTime), color= (0,200,0),anchor = (1,0), angle=0)
    text4 = pg.TextItem(text="TR = " + str(recoveryTime), color= (0,200,0),anchor = (1,0), angle=0)
    text5 = pg.TextItem(text="TE = " + str(echoTime), color= (0,200,0),anchor = (1,0), angle=0)
    text6 = pg.TextItem(text="TR = " + str(recoveryTime), color= (0,200,0),anchor = (1,0), angle=0)
    text7 = pg.TextItem(text="TE = " + str(echoTime), color= (0,200,0),anchor = (1,0), angle=0)
    text8 = pg.TextItem(text="TR = " + str(recoveryTime), color= (0,200,0),anchor = (1,0), angle=0)
    text9 = pg.TextItem(text="TE = " + str(echoTime), color= (0,200,0),anchor = (1,0), angle=0)
    text10 = pg.TextItem(text="TR = " + str(recoveryTime), color= (0,200,0),anchor = (1,0), angle=0)
    text11 = pg.TextItem(text=str(flipAngle) , color= (0,200,0),anchor = (1,0), angle=0)
    text12 = pg.TextItem(text=str(flipAngle) , color= (0,200,0),anchor = (1,0), angle=0)
    rf_plot.addItem(text1)
    rf_plot.addItem(text2)
    rf_plot.addItem(text11)
    rf_plot.addItem(text12)
    gz_plot.addItem(text3)
    gz_plot.addItem(text4)
    gx_plot.addItem(text5)
    gx_plot.addItem(text6)
    gy_plot.addItem(text7)
    gy_plot.addItem(text8)
    readout_plot.addItem(text9)
    readout_plot.addItem(text10)

    ## Setting Text Positions
    text1.setPos(math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02)+ math.floor(recoveryTime*0.15)/2, 0.5)
    text2.setPos(recoveryTime, 0.5)
    text3.setPos(math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02)+ math.floor(recoveryTime*0.15)/2, 0.5)
    text4.setPos(recoveryTime, 0.5)
    text5.setPos(math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02)+ math.floor(recoveryTime*0.15)/2, 0.5)
    text6.setPos(recoveryTime, 0.5)
    text7.setPos(math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02)+ math.floor(recoveryTime*0.15)/2, 0.5)
    text8.setPos(recoveryTime, 0.5)
    text9.setPos(math.floor(2*recoveryTime*0.15 + 2*recoveryTime*0.02)+ math.floor(recoveryTime*0.15)/2, 0.5)
    text10.setPos(recoveryTime, 0.5)
    text11.setPos(math.floor(recoveryTime*0.15)/2,2.1)
    text12.setPos(recoveryTime, 2.1)

def drawPreparation(rf_preparation_plot, gz_preparation_plot, gy_preparation_plot, gx_preparation_plot, recoveryTime, prep_type, prep_parameter):
    if prep_type == 1:  ## Inversion Time
        ## RF
        flat_line = np.full((recoveryTime+math.floor(recoveryTime*0.15),),-1)
        data = np.zeros((recoveryTime+math.floor(recoveryTime*0.15),))
        temp = np.full((2*math.ceil(recoveryTime*0.075),),0)
        flat_line[0:temp.size,] = temp
        flat_line[recoveryTime - math.ceil(recoveryTime*0.075) : recoveryTime + math.ceil(recoveryTime*0.075), ] = temp
        x = np.linspace(-6,6,math.floor(recoveryTime*0.15))
        equation = np.sin(2*x)/x
        data[0:equation.size,] = equation
        rf = np.heaviside(flat_line,data)
        rf_preparation_plot.setXRange(0,recoveryTime)
        rf_preparation_plot.setYRange(2.5,-1*0.2)
        rf_preparation_plot.plot(rf)
        drawPreparationIndicators(rf_preparation_plot, gz_preparation_plot, gy_preparation_plot, gx_preparation_plot, recoveryTime, prep_type, prep_parameter)

        ## Gz
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),1)
        flat_line[0:temp.size,] = temp
        step = np.heaviside(flat_line,flat_line)
        gz_preparation_plot.setXRange(0,recoveryTime)
        gz_preparation_plot.setYRange(-1,1)
        gz_preparation_plot.plot(step)

    if prep_type == 2: ## T2 Prep
        # Gx
        x = np.linspace(0,360,math.floor(recoveryTime*0.15))
        y = np.linspace(0,2,math.floor(recoveryTime*0.15))
        attenuatedSine = np.sin(10*x*np.pi/180)*np.exp(-y)
        data = np.zeros((recoveryTime,))
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15),),0)
        flat_line[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+temp.size,] = temp
        data[2*math.ceil(recoveryTime*0.15):2*math.ceil(recoveryTime*0.15)+attenuatedSine.size,] = attenuatedSine
        step = np.heaviside(flat_line,data)
        gx_preparation_plot.setXRange(0,recoveryTime)
        gx_preparation_plot.setYRange(-1,1)
        gx_preparation_plot.plot(step)

        #Gy
        gy_preparation_plot.setXRange(0,recoveryTime)
        gy_preparation_plot.setYRange(-1,1)
        gy_preparation_plot.plot(step)

    if prep_type == 3: ## Tagging
        # RF
        flat_line = np.full((recoveryTime,),-1)
        temp = np.full((math.floor(recoveryTime*0.15/10),),1)
        flat_line[0:temp.size,] = temp
        flat_line[temp.size+prep_parameter:2*temp.size+prep_parameter,] = temp
        flat_line[2*temp.size+2*prep_parameter:3*temp.size+2*prep_parameter,] = temp
        flat_line[3*temp.size+3*prep_parameter:4*temp.size+3*prep_parameter,] = temp
        flat_line[4*temp.size+4*prep_parameter:5*temp.size+4*prep_parameter,] = temp
        flat_line[5*temp.size+5*prep_parameter:6*temp.size+5*prep_parameter,] = temp
        flat_line[6*temp.size+6*prep_parameter:7*temp.size+6*prep_parameter,] = temp
        step = np.heaviside(flat_line,flat_line)
        rf_preparation_plot.setXRange(0,recoveryTime)
        rf_preparation_plot.setYRange(-1,1)
        rf_preparation_plot.plot(step)


def drawPreparationIndicators(rf_preparation_plot, gz_preparation_plot, gy_preparation_plot, gx_preparation_plot, recoveryTime, prep_type, prep_parameter):
    text11 = pg.TextItem(text="180" , color= (0,200,0),anchor = (1,0), angle=0)
    rf_preparation_plot.addItem(text11)
    text11.setPos(math.floor(recoveryTime*0.15)/2,2)
    text12 = pg.TextItem(text="Inversion Time= " + str(prep_parameter) + " ms" , color= (0,200,0),anchor = (1,0), angle=0)
    rf_preparation_plot.addItem(text12)
    text12.setPos(recoveryTime,1)
