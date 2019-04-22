# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:23:00 2019

@author: Gamila
"""

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
fatT2=np.full((150, 150), 20)
intestineT2=np.full((70, 70), 135)

T2 [50:165, 50:165]=kidneyT2
T2[50:300, 200:450]=liverT2
T2[315:415, 412:512]=spleenT2
T2 [350:500, 100:250]=fatT2
T2[200:270, 100:170]=intestineT2

#T2= (255*T2)/np.max(T2)

#concatentaion of all properties to save in file
All=np.concatenate ((square_phantom,T1,T2)) #concatentation row wise (fo2 b3d)
np.save('Newest Phantom.npy', All)