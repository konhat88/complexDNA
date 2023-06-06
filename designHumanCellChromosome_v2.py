#!/usr/bin/env python3

#ofile = open("human_cell_23chromo_position_7.txt","w+")
#ofile2 = open("human_cell_23chromo_position_7.txt","w+")
ofile2 = open("human_cell_23chromo_position_7.txt","a")


#get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt, numpy as np, random, time
from wkozi import *

# Choose dimentions / default 94 / meaning 94*75 + 38.5 = 7088.5 nm to fit 7100 of the original size
ko = 140 # x,z axes (ONLY INTEGERS)
ko2= 70 # 1/2 x,z axes (ONLY INTEGERS)
ko3= 47 # 1/3 x,z axes (ONLY INTEGERS)
ko4= 35 # 1/4 x,z axes (ONLY INTEGERS)
zi = 45 # y axis (ONLY INTEGERS)
zi3= 15 # 1/3 y axis (ONLY INTEGERS, lower than zi)

# Length of each chromosome (Copy this part to coordinatesToFractalDNA_v2_human_cell.py)
c1	=	61000
c2	=	77000
c3	=	60000
c4	=	39000
c5	=	41000
c6	=	34000
c7	=	19000
c8	=	95000
c9	=	52000
c10	=	56000
c11	=	51000
c12	=	52000
c13	=	54000
c14	=	44000
c15	=	94000
c16	=	66000
c17	=	74000
c18	=	64000 #70000
c19	=	30000
c20	=	25000
c21	=	24000
c22	=	29000
c23	=	18000
#c24 = 38000 #6000 #99000
#c25 = 36000 # small addition

#ax = plt.subplot(1, 1, 1, projection='3d')
#ax.set_zlim(-ko+1, ko+1)
#plt.xlim([-ko+1, ko+1])
#plt.ylim([-ko+1, ko+1])

programT1 = time.time()
'''
past = np.zeros((1,3))
walk = randomwalk3D(c1,ko,zi,ko,past,-ko,0,-zi,-zi3,-ko,-ko3)
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
np.savetxt(ofile2,past)


past = np.zeros((1,3))
walk = randomwalk3D(c2,ko,zi,ko,past,-ko,0,-zi,-zi3,-ko3,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
#toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c3,ko,zi,ko,past,-ko,0,-zi,-zi3,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
#toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c4,ko,zi,ko,past,0,ko2,-zi,-zi3,-ko,-ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c5,ko,zi,ko,past,0,ko2,-zi,-zi3,-ko3,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c6,ko,zi,ko,past,0,ko2,-zi,-zi3,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c7,ko,zi,ko,past,ko2,ko,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)


past = np.zeros((1,3))
walk = randomwalk3D(c8,ko,zi,ko,past,-ko,-ko2,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c9,ko,zi,ko,past,-ko2,0,-zi3,zi3,-ko,-ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c10,ko,zi,ko,past,-ko2,0,-zi3,zi3,-ko3,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c11,ko,zi,ko,past,-ko2,0,-zi3,zi3,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c12,ko,zi,ko,past,0,ko2,-zi3,zi3,-ko,-ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c13,ko,zi,ko,past,0,ko2,-zi3,zi3,-ko3,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c14,ko,zi,ko,past,0,ko2,-zi3,zi3,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c15,ko,zi,ko,past,ko2,ko,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c16,ko,zi,ko,past,-ko,0,zi3,zi,-ko,-ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c17,ko,zi,ko,past,-ko,0,zi3,zi,-ko3,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)
'''

past = np.zeros((1,3))
walk = randomwalk3D(c18,ko,zi,ko,past,-ko,0,zi3,zi,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c19,ko,zi,ko,past,0,ko2,zi3,zi,-ko,-ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c20,ko,zi,ko,past,0,ko2,zi3,zi,-ko3,0)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c21,ko,zi,ko,past,0,ko2,zi3,zi,0,ko3)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c22,ko,zi,ko,past,0,ko2,zi3,zi,ko3,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
np.savetxt(ofile2,past)

past = np.zeros((1,3))
walk = randomwalk3D(c23,ko,zi,ko,past,ko2,ko,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
#ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
#ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
past = np.delete(past,0,axis=0)
#toSave = np.concatenate((toSave,past))
np.savetxt(ofile2,past)

#plt.show()

#np.savetxt(ofile,toSave)
#ofile.close()
ofile2.close()
programTimeExecution = time.time() - programT1
print(programTimeExecution," seconds")

# In[ ]:

# To create projections of the new geometry
'''
for ii in range(0,360,1):
    ax.view_init(elev=20., azim=ii)
    plt.savefig("human_cell_movie_1/human_cell%03d.png" % ii)
'''
