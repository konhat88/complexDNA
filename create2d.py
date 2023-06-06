#!/usr/bin/env python3
ifile = open("human_cell_23chromosomes_final_7.txt","r")
kozi = "z" # Choose y or z to plot xz or xy respectively
ofile= open("plotPos_random_7_z.txt","w+")

cnt = 0
st  = 0
trn = 0

nbHst   = 38
nbHtrn  = 26
nbBPst  = 7331
nbBPtrn = 5024

for line in ifile:
    spl = line.split()
    if cnt>0:
        if spl[1]=="straight":
            st  += 1
        else:
            trn += 1

    cnt += 1
print("straights: ",st,"\t turns: ",trn)
print("straights: ",st/(st+trn),"%", "\t turns: ",trn/(st+trn),"%")


HistSt = st*nbHst
HistTrn = trn*nbHtrn
BPst = st*nbBPst
BPtrn = trn*nbBPtrn

totalH = HistSt + HistTrn
totalBP = BPst + BPtrn
#print(HistSt, HistTrn, totalH, BPst, BPtrn, totalBP)
print("Histones: ", totalH, "\t Base Pairs: ", totalBP)
print("ratio BP/Histone: ", totalBP/totalH)

cnt= 0
bp= 0
ws= " "

if kozi=="y":
    ko=3
else:
    ko=4
#print(ko)

ifile.seek(0)

for line in ifile:
    spl = line.split()
    if cnt>0:
        if float(spl[ko])<1 and float(spl[ko])>=0:
            nline = spl[2]+ws+spl[3]+ws+spl[4]+"\n"
            ofile.write(nline)
            if spl[1]=="straight":
                bp+=7331
            else:
                bp+=5024
    cnt += 1

print("BP in plane: ",bp)
ofile.close()
ifile.close()
