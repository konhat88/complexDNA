#!/usr/bin/env python3

#ofile = open("human_cell_23chromo_position_6.txt","w+")
ofile2 = open("human_cell_23chromo_position_6_test_1.txt","a")


#get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt, numpy as np, random, time
from wkozi import *

# Choose dimentions / default 94 / meaning 94*75 + 38.5 = 7088.5 nm to fit 7100 of the original size
ko = 94 # x,z axes (ONLY INTEGERS)
ko2= 46 # 1/2 x,z axes (ONLY INTEGERS)
zi = 32 # y axis (ONLY INTEGERS)
zi3= 11 # 1/3 y axis (ONLY INTEGERS, lower than zi)

# Length of each chromosome (Copy this part to coordinatesToFractalDNA_v2_human_cell.py)
c1  = 24000 #88000
c2  = 45000 #87000
c3  = 45000 #17000
c4  = 24000 #71500
c5  = 20000 #32500
c6  = 18000 #69000
c7  = 11000 #21000
c8  = 26000 #65000
c9  = 26000 #23500
c10 = 13000 #61000
c11 = 15000 #41500
c12 = 15000 #57000
c13 = 34000 #48000
c14 = 32000 #48500
c15 = 30000 #39000
c16 = 28000 #48000
c17 = 21000 #36500
c18 = 14000 #52000
c19 =  9000 #51000
c20 = 30000 #28500
c21 = 16000 #27500
c22 = 36000 #23500
c23 = 10000 #18000
c24 = 24000 #6000 #99000
#c25 = 36000 # small addition

#ax = plt.subplot(1, 1, 1, projection='3d')
#ax.set_zlim(-ko+1, ko+1)
#plt.xlim([-ko+1, ko+1])
#plt.ylim([-ko+1, ko+1])

programT1 = time.time()
past = np.zeros((1,3))

walk = randomwalk3D(c18,ko,zi,ko,past,-ko,-ko2,zi3,zi,-ko,ko)
programTimeExecution = time.time() - programT1
print(programTimeExecution," seconds")
past = np.delete(past,0,axis=0)
past = np.concatenate((past,walk))

walk = randomwalk3D(c19,ko,zi,ko,past,-ko,-ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)
past = np.zeros((1,3))


walk = randomwalk3D(c20,ko,zi,ko,past,-ko2,0,zi3,zi,-ko,ko)
past = np.delete(past,0,axis=0)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c21,ko,zi,ko,past,-ko2,0,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)
past = np.zeros((1,3))


walk = randomwalk3D(c22,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.delete(past,0,axis=0)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c23,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)
past = np.zeros((1,3))


walk = randomwalk3D(c24,ko,zi,ko,past,ko2,ko,zi3,zi,-ko,ko)
past = np.delete(past,0,axis=0)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)

programTimeExecution = time.time() - programT1
print(programTimeExecution," seconds")

#plt.show()


ofile2.close()
