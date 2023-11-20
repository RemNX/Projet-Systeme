from intensite import *
import matplotlib.pyplot as plt
import sys

index=int(sys.argv[1])
dico=getdico()


clefchoisis=list(dico)[index]
print(clefchoisis)
print(dico.get(clefchoisis))

for i in dico:
    if Strtolist(i)



nbintensite=len(dicodonnées[i])
valmin=dico.get(clefchoisis)[0]
valmax=dico.get(clefchoisis)[0]
valsum=0
for j in dicodonnées[i]:
    if valmin>j:
        valmin=j
    if valmax<j:
        valmax=j
    valsum+=j
valmoyenne=valsum/nbintensite