#!/usr/bin/env python3
# To run, change the links and definitions in this script and
# type in the terminal containing the file
# $python3 coordinatesToFractalDNA.py

# Author contact, Konstantinos Chatzipapas, chatzipa@cenbg.in2p3.fr, 01/03/2022

# INPUTS
ifile1= "human_cell_23chromo_position_7.txt"
ofile1= "human_cell_23chromosomes_7.txt"
ofile2= "human_cell_23chromosomes_final_7.txt"

# Length of each chromosome (THIS SHOULD BE THE SAME, AS IN THE designHumanCellChromosome.py)
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
#c24 = 99000
#c25 = 36000 # small addition


import sys, numpy as np, matplotlib.pyplot as plt
from pathlib import Path
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import interactive

try:
    # The voxelisation library produces the cubic voxelisation that
    # can be used to build DNA
    from fractaldna.structure_models import voxelisation as v

    # The hilbert module produces and handles L-Strings
    from fractaldna.structure_models import hilbert as h
except (ImportError, ModuleNotFoundError):
    sys.path.append(str(Path.cwd().parent.parent.parent))
    from fractaldna.structure_models import voxelisation as v
    from fractaldna.structure_models import hilbert as h


coord = np.loadtxt(ifile1)
print(coord)

x_curve = coord


chromo1  = np.zeros((c1,3))
chromo2  = np.zeros((c2,3))
chromo3  = np.zeros((c3,3))
chromo4  = np.zeros((c4,3))
chromo5  = np.zeros((c5,3))
chromo6  = np.zeros((c6,3))
chromo7  = np.zeros((c7,3))
chromo8  = np.zeros((c8,3))
chromo9  = np.zeros((c9,3))
chromo10 = np.zeros((c10,3))
chromo11 = np.zeros((c11,3))
chromo12 = np.zeros((c12,3))
chromo13 = np.zeros((c13,3))
chromo14 = np.zeros((c14,3))
chromo15 = np.zeros((c15,3))
chromo16 = np.zeros((c16,3))
chromo17 = np.zeros((c17,3))
chromo18 = np.zeros((c18,3))
chromo19 = np.zeros((c19,3))
chromo20 = np.zeros((c20,3))
chromo21 = np.zeros((c21,3))
chromo22 = np.zeros((c22,3))
chromo23 = np.zeros((c23,3))
#chromo24 = np.zeros((c24,3))
#chromo25 = np.zeros((c25,3)) ###

for k in range(c1):
    chromo1[k,:] = coord[k,:]
for k in range(c2):
    chromo2[k,:] = coord[k+c1,:]
for k in range(c3):
    chromo3[k,:] = coord[k+c1+c2,:]
for k in range(c4):
    chromo4[k,:] = coord[k+c1+c2+c3,:]
for k in range(c5):
    chromo5[k,:] = coord[k+c1+c2+c3+c4,:]
for k in range(c6):
    chromo6[k,:] = coord[k+c1+c2+c3+c4+c5,:]
for k in range(c7):
    chromo7[k,:] = coord[k+c1+c2+c3+c4+c5+c6,:]
for k in range(c8):
    chromo8[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7,:]
for k in range(c9):
    chromo9[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8,:]
for k in range(c10):
    chromo10[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9,:]
for k in range(c11):
    chromo11[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10,:]
for k in range(c12):
    chromo12[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11,:]
for k in range(c13):
    chromo13[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12,:]
for k in range(c14):
    chromo14[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13,:]
for k in range(c15):
    chromo15[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14,:]
for k in range(c16):
    chromo16[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15,:]
for k in range(c17):
    chromo17[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16,:]
for k in range(c18):
    chromo18[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17,:]
for k in range(c19):
    chromo19[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18,:]
for k in range(c20):
    chromo20[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19,:]
for k in range(c21):
    chromo21[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20,:]
for k in range(c22):
    chromo22[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21,:]
for k in range(c23):
    chromo23[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22,:]
#for k in range(c24):
#    chromo24[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23,:]
#for k in range(c25):
#    chromo25[k,:] = coord[k+c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23+c24,:]


print (chromo1)
#print (chromo2)
#print (chromo3)
#print (chromo4)

# For validation
print(len(coord))
print(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10+c11+c12+c13+c14+c15+c16+c17+c18+c19+c20+c21+c22+c23)#+c24)

# Create path from the coordinates path
voxelised_fractal_1  = v.VoxelisedFractal.from_path(chromo1)
voxelised_fractal_2  = v.VoxelisedFractal.from_path(chromo2)
voxelised_fractal_3  = v.VoxelisedFractal.from_path(chromo3)
voxelised_fractal_4  = v.VoxelisedFractal.from_path(chromo4)
voxelised_fractal_5  = v.VoxelisedFractal.from_path(chromo5)
voxelised_fractal_6  = v.VoxelisedFractal.from_path(chromo6)
voxelised_fractal_7  = v.VoxelisedFractal.from_path(chromo7)
voxelised_fractal_8  = v.VoxelisedFractal.from_path(chromo8)
voxelised_fractal_9  = v.VoxelisedFractal.from_path(chromo9)
voxelised_fractal_10 = v.VoxelisedFractal.from_path(chromo10)
voxelised_fractal_11 = v.VoxelisedFractal.from_path(chromo11)
voxelised_fractal_12 = v.VoxelisedFractal.from_path(chromo12)
voxelised_fractal_13 = v.VoxelisedFractal.from_path(chromo13)
voxelised_fractal_14 = v.VoxelisedFractal.from_path(chromo14)
voxelised_fractal_15 = v.VoxelisedFractal.from_path(chromo15)
voxelised_fractal_16 = v.VoxelisedFractal.from_path(chromo16)
voxelised_fractal_17 = v.VoxelisedFractal.from_path(chromo17)
voxelised_fractal_18 = v.VoxelisedFractal.from_path(chromo18)
voxelised_fractal_19 = v.VoxelisedFractal.from_path(chromo19)
voxelised_fractal_20 = v.VoxelisedFractal.from_path(chromo20)
voxelised_fractal_21 = v.VoxelisedFractal.from_path(chromo21)
voxelised_fractal_22 = v.VoxelisedFractal.from_path(chromo22)
voxelised_fractal_23 = v.VoxelisedFractal.from_path(chromo23)
#voxelised_fractal_24 = v.VoxelisedFractal.from_path(chromo24)
#voxelised_fractal_25 = v.VoxelisedFractal.from_path(chromo25)


# This can be plotted
# %matplotlib qt
#voxelised_fractal_1.to_pretty_plot()
#voxelised_fractal_2.to_pretty_plot()
#voxelised_fractal_3.to_pretty_plot()
#voxelised_fractal_4.to_pretty_plot()


# And this can be returned as a data frame, or as text
# Text is also printed to file, to be used by the MolecularDNA example of Geant4-DNA
x1 = voxelised_fractal_1.to_text()
x2 = voxelised_fractal_2.to_text()
x3 = voxelised_fractal_3.to_text()
x4 = voxelised_fractal_4.to_text()
x5 = voxelised_fractal_5.to_text()
x6 = voxelised_fractal_6.to_text()
x7 = voxelised_fractal_7.to_text()
x8 = voxelised_fractal_8.to_text()
x9 = voxelised_fractal_9.to_text()
x10 = voxelised_fractal_10.to_text()
x11 = voxelised_fractal_11.to_text()
x12 = voxelised_fractal_12.to_text()
x13 = voxelised_fractal_13.to_text()
x14 = voxelised_fractal_14.to_text()
x15 = voxelised_fractal_15.to_text()
x16 = voxelised_fractal_16.to_text()
x17 = voxelised_fractal_17.to_text()
x18 = voxelised_fractal_18.to_text()
x19 = voxelised_fractal_19.to_text()
x20 = voxelised_fractal_20.to_text()
x21 = voxelised_fractal_21.to_text()
x22 = voxelised_fractal_22.to_text()
x23 = voxelised_fractal_23.to_text()
#x24 = voxelised_fractal_24.to_text()
#x25 = voxelised_fractal_25.to_text()

with open(ofile1, 'w+') as ofile:
    ofile.write(x1)
    ofile.write("\n")
    ofile.write(x2)
    ofile.write("\n")
    ofile.write(x3)
    ofile.write("\n")
    ofile.write(x4)
    ofile.write("\n")
    ofile.write(x5)
    ofile.write("\n")
    ofile.write(x6)
    ofile.write("\n")
    ofile.write(x7)
    ofile.write("\n")
    ofile.write(x8)
    ofile.write("\n")
    ofile.write(x9)
    ofile.write("\n")
    ofile.write(x10)
    ofile.write("\n")
    ofile.write(x11)
    ofile.write("\n")
    ofile.write(x12)
    ofile.write("\n")
    ofile.write(x13)
    ofile.write("\n")
    ofile.write(x14)
    ofile.write("\n")
    ofile.write(x15)
    ofile.write("\n")
    ofile.write(x16)
    ofile.write("\n")
    ofile.write(x17)
    ofile.write("\n")
    ofile.write(x18)
    ofile.write("\n")
    ofile.write(x19)
    ofile.write("\n")
    ofile.write(x20)
    ofile.write("\n")
    ofile.write(x21)
    ofile.write("\n")
    ofile.write(x22)
    ofile.write("\n")
    ofile.write(x23)
    #ofile.write("\n")
    #ofile.write(x24)
    #ofile.write("\n")
    #ofile.write(x25)



with open(ofile1, 'r') as ifile:
    with open(ofile2,"w+") as ofile:
        i = 0
        j = 0
        sp = " "
        for line in ifile:
            if i>0:
                spl = line.split(sp)
                if "#IDX" in spl[0]:
                    print(spl[0])
                else:
                    spl[0] = j
                    newline = str(spl[0])+sp+str(spl[1])+sp+str(spl[2])+sp+str(spl[3])+sp+str(spl[4])+sp+str(spl[5])+sp+str(spl[6])+sp+str(spl[7])
                    ofile.write(newline)
                    nb = spl[0]
                    j += 1
            else:
                ofile.write(line)
            i += 1
