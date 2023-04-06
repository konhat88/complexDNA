#!/usr/bin/env python3

#ofile = open("human_cell_23chromo_position_6.txt","w+")
ofile2 = open("lamda_v2.txt","a") #"w+")


#get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt, numpy as np, random, time
from wkozi import *

# Choose dimentions / default 94 / meaning 94*75 + 38.5 = 7088.5 nm to fit 7100 of the original size
ko = 45 # x,z axes (ONLY INTEGERS)
ko2= 22 # 1/2 x,z axes (ONLY INTEGERS)
zi = 45 # y axis (ONLY INTEGERS)
zi3= 12 # 1/3 y axis (ONLY INTEGERS, lower than zi)

# Length of each chromosome (Copy this part to coordinatesToFractalDNA_v2_human_cell.py)
c1  = 6930

#ax = plt.subplot(1, 1, 1, projection='3d')
#ax.set_zlim(-ko+1, ko+1)
#plt.xlim([-ko+1, ko+1])
#plt.ylim([-ko+1, ko+1])

programT1 = time.time()

past = np.zeros((1,3))
walk = randomwalk3D(c1,ko,zi,ko,past,-ko,ko,-zi,zi,-ko,ko)
programTimeExecution = time.time() - programT1
print(programTimeExecution," seconds")
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
#plt.show()

print(past)
past = np.delete(past,0,axis=0)
print(past)
# Save before going to the next area
#toSave = past

# Geometric correction specific for lambda DNA geometries
new = past
n=0
#print(past)
for i in new:
    #print(i)
    j = i*3
    #print(j)
    new[n]=j
    n += 1
print(new)
np.savetxt(ofile2,new)

#plt.show()



#np.savetxt(ofile,toSave)
#ofile.close()
ofile2.close()

# In[ ]:

# To create projections of the new geometry
'''
for ii in range(0,360,1):
    ax.view_init(elev=20., azim=ii)
    plt.savefig("human_cell_movie_1/human_cell%03d.png" % ii)
'''
