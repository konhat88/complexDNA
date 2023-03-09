#!/usr/bin/env python3

ofile = open("human_cell_23chromo_position_5.txt","w+")

#get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt, numpy as np, random, time
from wkozi import *
past = np.zeros((1,3))

# Choose dimentions / default 94 / meaning 94*75 + 38.5 = 7088.5 nm to fit 7100 of the original size
ko = 94 # x,z axes (ONLY INTEGERS)
ko2= 46 # 1/2 x,z axes (ONLY INTEGERS)
zi = 32 # y axis (ONLY INTEGERS)
zi3= 11 # 1/3 y axis (ONLY INTEGERS, lower than zi)

# Length of each chromosome (Copy this part to coordinatesToFractalDNA_v2_human_cell.py)
c1  = 88000
c2  = 87000
c3  = 17000
c4  = 71500
c5  = 32500
c6  = 69000
c7  = 21000
c8  = 65000
c9  = 23500
c10 = 61000
c11 = 41500
c12 = 57000
c13 = 48000
c14 = 48500
c15 = 39000
c16 = 48000
c17 = 36500
c18 = 52000
c19 = 51000
c20 = 28500
c21 = 27500
c22 = 23500
c23 = 18000
c24 = 99000
#c25 = 36000 # small addition

ax = plt.subplot(1, 1, 1, projection='3d')
ax.set_zlim(-ko+1, ko+1)
plt.xlim([-ko+1, ko+1])
plt.ylim([-ko+1, ko+1])

programT1 = time.time()
walk = randomwalk3D(c1,ko,zi,ko,past,-ko,-ko2,-zi,-zi3,-ko,ko)
programTimeExecution = time.time() - programT1
print(programTimeExecution," seconds")
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])
#plt.show()

print(past)
past = np.delete(past,0,axis=0)
print(past)


walk = randomwalk3D(c2,ko,zi,ko,past,-ko2,0,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c3,ko,zi,ko,past,-ko2,0,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c4,ko,zi,ko,past,0,ko2,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c5,ko,zi,ko,past,0,ko2,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c6,ko,zi,ko,past,ko2,ko,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c7,ko,zi,ko,past,ko2,ko,-zi,-zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])


# In[ ]:



walk = randomwalk3D(c8,ko,zi,ko,past,ko2,ko,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c9,ko,zi,ko,past,ko2,ko,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c10,ko,zi,ko,past,0,ko2,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c11,ko,zi,ko,past,0,ko2,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c12,ko,zi,ko,past,-ko2,0,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c13,ko,zi,ko,past,-ko2,0,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c14,ko,zi,ko,past,-ko,-ko2,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c15,ko,zi,ko,past,-ko,-ko2,-zi3,zi3,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])


# In[ ]:



walk = randomwalk3D(c16,ko,zi,ko,past,-ko,-ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c17,ko,zi,ko,past,-ko,-ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c18,ko,zi,ko,past,-ko2,0,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c19,ko,zi,ko,past,-ko2,0,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c20,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c21,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c22,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c23,ko,zi,ko,past,0,ko2,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

walk = randomwalk3D(c24,ko,zi,ko,past,ko2,ko,zi3,zi,-ko,ko)
past = np.concatenate((past,walk))
ax.plot(walk[:,0], walk[:,1], walk[:,2], alpha=0.9)
ax.scatter(walk[-1,0], walk[-1,1], walk[-1,2])

plt.show()




np.savetxt(ofile,past)


# In[ ]:





# In[30]:

'''
for ii in range(0,360,1):
    ax.view_init(elev=20., azim=ii)
    plt.savefig("human_cell_movie_1/human_cell%03d.png" % ii)
'''
