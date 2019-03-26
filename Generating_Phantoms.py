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
intestine=np.full((70, 70), 135)
## adding tissues to the phantom
square_phantom [50:165, 50:165]=kidney
square_phantom [50:300, 200:450]=liver
square_phantom [315:415, 412:512]=spleen
square_phantom [350:500, 100:250]=fat
square_phantom [200:270, 100:170]=intestine
## assign T1 and T2 to each tissue 
T1=np.full((512,512 ), 0) 

kidneyT1 =np.full((115,115 ), 400) 
liverT1=np.full((250, 250), 600)
spleenT1=np.full((100, 100), 550)
fatT1=np.full((150, 150), 250)
intestineT1=np.full((70, 70),300)

T1 [50:165, 50:165]=kidneyT1
T1[50:300, 200:450]=liverT1
T1[315:415, 412:512]=spleenT1
T1 [350:500, 100:250]=fatT1
T1[200:270, 100:170]=intestineT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)

T2=np.full((512,512 ), 0)  
kidneyT2 =np.full((115,115 ), 60) 
liverT2=np.full((250, 250), 100)
spleenT2=np.full((100, 100), 115)
fatT2=np.full((150, 150), 70)
intestineT2=np.full((70, 70), 135)

T2 [50:165, 50:165]=kidneyT2
T2[50:300, 200:450]=liverT2
T2[315:415, 412:512]=spleenT2
T2 [350:500, 100:250]=fatT2
T2[200:270, 100:170]=intestineT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
np.save('square_phantom.npy', All)
#np.savetxt('squrePhantom.txt' ,All, delimiter=',')
########################################################################
different_square_phantom = np.zeros ((n[1], n[1]))
#small squares with different intensity to simulate different tissues
kidney =np.full((75,75 ), 255) 
liver=np.full((35, 35), 200)
spleen=np.full((55, 55), 100)
fat=np.full((100,100), 50)
intestine=np.full((40,40),130)
## adding tissues to the phantom
different_square_phantom [20:95, 20:95]=kidney
different_square_phantom[ 20:55, 200:235]=liver
different_square_phantom[190:245, 100:155]=spleen
different_square_phantom [80:180 ,120:220]=fat
different_square_phantom [30:70 ,100:140]=intestine
# assign T1 and T2 to each tissue 
T1=np.full((n[1], n[1]), 0) 

kidneyT1 =np.full((75,75  ), 700) 
liverT1=np.full((35, 35), 400)
spleenT1=np.full((55, 55), 550)
fatT1=np.full((100,100), 250)
intestineT1=np.full((40,40), 600)

T1 [20:95, 20:95]=kidneyT1
T1[ 20:55, 200:235]=liverT1
T1[190:245, 100:155]=spleenT1
T1  [80:180 ,120:220]=fatT1
T1  [30:70 ,100:140]=intestineT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)
#
T2=np.full((n[1], n[1]) , 0)  
kidneyT2 =np.full((75,75),  60) 
liverT2=np.full((35, 35), 40)
spleenT2=np.full((55, 55), 90)
fatT2=np.full((100,100), 70)
intestineT2=np.full((40,40), 50)

T2 [20:95, 20:95]=kidneyT2
T2[ 20:55, 200:235]=liverT2
T2[190:245, 100:155]=spleenT2
T2 [80:180 ,120:220]=fatT2
T2 [30:70 ,100:140]=intestineT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((different_square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
#np.savetxt('DifferentSquarePhantom.txt' ,All, delimiter=',')
np.save('different_square_phantom.npy', All)
#############################################


Rectangle_phantom = np.zeros ((n[2], n[2]))
#small squares with different intensity to simulate different tissues
kidney =np.full((20,75 ), 255) 
liver=np.full((50, 35), 220)
spleen=np.full((30, 55), 130)
fat=np.full((10,60), 50)
intestine=np.full((37,20), 90)
## adding tissues to the phantom
Rectangle_phantom [20:40, 10:85]=kidney
Rectangle_phantom[ 45:95, 90:125 ]=liver
Rectangle_phantom[90:120, 20:75]=spleen
Rectangle_phantom [5:15 ,40:100]=fat
Rectangle_phantom [43:80 ,30:50]=intestine
# assign T1 and T2 to each tissue 
T1=np.full((n[2], n[2]), 0) 

kidneyT1 =np.full((20,75 ), 700) 
liverT1=np.full((50, 35), 400)
spleenT1=np.full((30, 55), 550)
fatT1=np.full((10,60), 250)
intestineT1=np.full((37,20), 700)

T1 [20:40, 10:85]=kidneyT1
T1[ 45:95, 90:125]=liverT1
T1[90:120,20:75]=spleenT1
T1  [5:15 ,40:100]=fatT1
T1  [43:80 ,30:50]=intestineT1
#to make it able to show as image
T1= (255*T1)/np.max(T1)
#
T2=np.full((n[2], n[2]) , 0)  

kidneyT2 =np.full((20,75 ),  60) 
liverT2=np.full((50, 35), 40)
spleenT2=np.full((30, 55), 100)
fatT2=np.full((10,60), 70)
intestineT2=np.full((37,20), 20)

T2 [20:40, 10:85]=kidneyT2
T2[ 45:95, 90:125]=liverT2
T2[90:120, 20:75]=spleenT2
T2 [5:15 ,40:100]=fatT2
T2 [43:80 ,30:50]=intestineT2

T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((Rectangle_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
#np.savetxt('RectanglePhantom.txt' ,All, delimiter=',')
np.save('Rectangle_phantom.npy', All)
new_num_arr = np.load('Rectangle_phantom.npy')

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
z=(len(new_num_arr)/3)

I=new_num_arr[1:int(z),:]
T1=new_num_arr[1+int(z):2*int(z),:]
T2=new_num_arr[1+2*int(z):3*int(z),:]
pl.imshow(I       , cmap='gray', vmin=0, vmax=255)




