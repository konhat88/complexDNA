#!/usr/bin/env python3
kozi = "z" # Choose y or z to plot xz or xy respectively
ifile= open("plotPos_random_7_z.txt","r")

import numpy as np, matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

A = np.loadtxt(ifile)
DNA = A*75
print(A)
ifile.close()

fig = plt.figure()
ax = fig.add_subplot(111)
if kozi=="y":
    ax.scatter(DNA[:,0],DNA[:,2],marker=".",linewidths=0.1)
else:
    ax.scatter(DNA[:,0],DNA[:,1],marker=".",linewidths=0.1)
#plt.plot(DNA[:,0],DNA[:,2], linestyle='')
plt.show()
