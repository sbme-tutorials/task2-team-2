# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:26:23 2019

@author: Gamila
"""
import numpy as np



square_phantom = np.zeros ((32,32))

kidney =np.full((5,5 ), 255) 
liver=np.full((3,3), 200)
spleen=np.full((6,6), 100)
fat=np.full((7,7), 50)

## adding tissues to the phantom
square_phantom [21:26, 2:7]=kidney
square_phantom [28:31, 9:12]=liver
square_phantom [24:30, 14:20]=spleen
square_phantom [ 21:28, 21:28]=fat

# assign T1 and T2 to each tissue 
T1=np.full((32,32), 0) 

kidneyT1 =np.full((5,5  ), 100) 
liverT1=np.full((3,3), 200)
spleenT1=np.full((6,6), 300)
fatT1=np.full((7,7), 400)

T1 [21:26, 2:7]=kidneyT1
T1[28:31, 9:12]=liverT1
T1[24:30, 14:20]=spleenT1
T1 [ 21:28, 21:28]=fatT1

#to make it able to show as image
T1= (255*T1)/np.max(T1)

T2=np.full((32,32 ), 0)  
kidneyT2 =np.full((5,5  ), 50) 
liverT2=np.full((3,3), 80)
spleenT2=np.full((6,6), 150)
fatT2=np.full((7,7), 100)


T2 [21:26, 2:7]=kidneyT2
T2[28:31, 9:12]=liverT2
T2[24:30, 14:20]=spleenT2
T2  [21:28, 21:28]=fatT2


T2= (255*T2)/np.max(T2)
#pl.imshow(T2 , cmap='gray', vmin=0, vmax=255)

all=np.concatenate((square_phantom, T1,T2))
np.save('DrTamerNewPhantom.npy',all)