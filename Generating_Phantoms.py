# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 14:30:53 2019

@author: Gamila
"""
#liver , kidney , spleen , fats 

import numpy as np
import matplotlib.pyplot as pl

n =[512, 256,128]
#crating square phantom
## creating blank black image
square_phantom = np.zeros ((n[0], n[0]))
#small squares with different intensity to simulate different tissues
kidney =np.full((115,115 ), 255) 
liver=np.full((250, 250), 200)
spleen=np.full((100, 100), 100)
fat=np.full((150, 150), 50)
## adding tissues to the phantom
square_phantom [50:165, 50:165]=kidney
square_phantom [50:300, 200:450]=liver
square_phantom [315:415, 412:512]=spleen
square_phantom [350:500, 100:250]=fat
## assign T1 and T2 to each tissue 
T1=np.full((512,512 ), 0) 

kidneyT1 =np.full((115,115 ), 400) 
liverT1=np.full((250, 250), 400)
spleenT1=np.full((100, 100), 550)
fatT1=np.full((150, 150), 250)

T1 [50:165, 50:165]=kidneyT1
T1[50:300, 200:450]=liverT1
T1[315:415, 412:512]=spleenT1
T1 [350:500, 100:250]=fatT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)

T2=np.full((512,512 ), 0)  
kidneyT2 =np.full((115,115 ), 60) 
liverT2=np.full((250, 250), 40)
spleenT2=np.full((100, 100), 60)
fatT2=np.full((150, 150), 70)

T2 [50:165, 50:165]=kidneyT2
T2[50:300, 200:450]=liverT2
T2[315:415, 412:512]=spleenT2
T2 [350:500, 100:250]=fatT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
np.savetxt('squrePhantom.txt' ,All, delimiter=',')
########################################################################
different_square_phantom = np.zeros ((n[1], n[1]))
#small squares with different intensity to simulate different tissues
kidney =np.full((75,75 ), 255) 
liver=np.full((35, 35), 200)
spleen=np.full((55, 55), 100)
fat=np.full((100,100), 50)
## adding tissues to the phantom
different_square_phantom [20:95, 20:95]=kidney
different_square_phantom[ 20:55, 200:235]=liver
different_square_phantom[190:245, 100:155]=spleen
different_square_phantom [80:180 ,120:220]=fat
# assign T1 and T2 to each tissue 
T1=np.full((n[1], n[1]), 0) 

kidneyT1 =np.full((75,75  ), 400) 
liverT1=np.full((35, 35), 400)
spleenT1=np.full((55, 55), 550)
fatT1=np.full((100,100), 250)

T1 [20:95, 20:95]=kidneyT1
T1[ 20:55, 200:235]=liverT1
T1[190:245, 100:155]=spleenT1
T1  [80:180 ,120:220]=fatT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)
#
T2=np.full((n[1], n[1]) , 0)  
kidneyT2 =np.full((75,75),  60) 
liverT2=np.full((35, 35), 40)
spleenT2=np.full((55, 55), 60)
fatT2=np.full((100,100), 70)

T2 [20:95, 20:95]=kidneyT2
T2[ 20:55, 200:235]=liverT2
T2[190:245, 100:155]=spleenT2
T2 [80:180 ,120:220]=fatT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((different_square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
np.savetxt('DifferentSquarePhantom.txt' ,All, delimiter=',')
#############################################


Rectangle_phantom = np.zeros ((n[2], n[2]))
#small squares with different intensity to simulate different tissues
kidney =np.full((20,75 ), 255) 
liver=np.full((50, 35), 220)
spleen=np.full((30, 55), 130)
fat=np.full((10,60), 50)
## adding tissues to the phantom
Rectangle_phantom [20:40, 10:85]=kidney
Rectangle_phantom[ 45:95, 90:125 ]=liver
Rectangle_phantom[190:245, 100:155]=spleen
Rectangle_phantom [5:15 ,40:100]=fat
# assign T1 and T2 to each tissue 
T1=np.full((n[2], n[2]), 0) 

kidneyT1 =np.full((20,75 ), 400) 
liverT1=np.full((50, 35), 400)
spleenT1=np.full((30, 55), 550)
fatT1=np.full((10,60), 250)

T1 [20:95, 20:95]=kidneyT1
T1[ 20:55, 200:235]=liverT1
T1[190:245, 100:155]=spleenT1
T1  [80:180 ,120:220]=fatT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)
#
T2=np.full((n[2], n[2]) , 0)  
kidneyT2 =np.full((20,75 ),  60) 
liverT2=np.full((50, 35), 40)
spleenT2=np.full((30, 55), 60)
fatT2=np.full((10,60), 70)

T2 [20:95, 20:95]=kidneyT2
T2[ 20:55, 200:235]=liverT2
T2[190:245, 100:155]=spleenT2
T2 [80:180 ,120:220]=fatT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((different_square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
np.savetxt('DifferentSquarePhantom.txt' ,All, delimiter=',')
#
#
#
#
#
#
#
#
#
##check for all
#x= np.loadtxt('squrePhantom.txt', delimiter=',')
#print(len(x))
#z=(len(x)/3)
#
#I=x[1:int(z),:]
#T1=x[1+int(z):2*int(z),:]
#T2=x[1+2*int(z):3*int(z),:]
pl.imshow(different_square_phantom , cmap='gray', vmin=0, vmax=255)




