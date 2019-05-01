# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:23:00 2019

@author: Gamila
"""

import numpy as np
import matplotlib.pyplot as pl




#crating square phantom
## creating blank black image
square_phantom = np.zeros ((64,64))
#small squares with different intensity to simulate different tissues
kidney =np.full((10,10 ), 100) 
liver=np.full((10,10), 150)
spleen=np.full((15,15),200)
fat=np.full((10,10), 250)

## adding tissues to the phantom
square_phantom [2:12,2:12]=kidney
square_phantom [35:45,35:45]=liver
square_phantom [15:30, 46:61]=spleen
square_phantom [15:25,15:25]=fat

squaremapped=(255*square_phantom)/np.max(square_phantom)
## assign T1 and T2 to each tissue 
T1=np.full((64,64 ), 0) 

kidneyT1 =np.full((10,10 ), 200) 
liverT1=np.full((10,10), 400)
spleenT1=np.full((15,15), 600)
fatT1=np.full((10,10), 800)


T1[2:12,2:12]=kidneyT1
T1[35:45,35:45]=liverT1
T1[15:30, 46:61]=spleenT1
T1 [15:25,15:25]=fatT1

#to make it able to show as image
T1mapped= (255*T1)/np.max(T1)

T2=np.full((64,64),0)  
kidneyT2 =np.full((10,10 ), 50) 
liverT2=np.full((10,10), 80)
spleenT2=np.full((15,15),100)
fatT2=np.full((10,10), 150)


T2[2:12,2:12]=kidneyT2
T2[35:45,35:45]=liverT2
T2[15:30, 46:61]=spleenT2
T2 [15:25,15:25]=fatT2

#print(size(square_phantom))
T2mapped= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((square_phantom,T1,T2, squaremapped, T1mapped, T2mapped)) #concatentation row wise (fo2 b3d)
np.save('FinalPhantom64.npy', All)
print(np.size(All))
pl.imshow(square_phantom      , cmap='gray', vmin=0, vmax=255)

