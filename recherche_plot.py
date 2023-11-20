import sys

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from intensite import *

#recup les données du intensite.py
dico=getdico()

listlambda=[]
listintensite=[]
#deb=float(sys.argv[1])
#fin=float(sys.argv[2])
deb=400
fin=422

for i in dico:
    clef1=float(Strtolist(i)[0])
    clef2=float(Strtolist(i)[1])
    # cherche tous les intervalles compris entre le début et la fin choisis par l'utilisateur
    if clef2>deb and clef1<fin:
        for j in range(len(getlambda())):                   #possiblité de faire avec seulement le premier et dernier intervalle [0] [-1]
            if (clef1>=getlambda()[j] and clef1<getlambda()[j+1]):
                debindex=getlambda().index(getlambda()[j+1])
            elif (clef2>=getlambda()[j] and clef2<getlambda()[j+1]):
                finindex=getlambda().index(getlambda()[j+1])
        for j in range(debindex,finindex):
            listlambda.append(getlambda()[j])
            listintensite.append(getintensite()[j])


nbintensite=len(listintensite)
valmin=listintensite[0]
valmax=listintensite[0]
valsum=0
for j in listintensite:
    if valmin>j:
        valmin=j
    if valmax<j:
        valmax=j
    valsum+=j
valmoyenne=round(valsum/nbintensite,3)

fig, ax = plt.subplots(figsize=(8,7))

ax.plot(listlambda,listintensite)
ax.set_xlabel("Longueur d'onde (nm)")
ax.set_ylabel("Intensité (coups)")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
plt.figtext(.2,.1,f"Nombres de valeurs : {nbintensite}")
plt.figtext(.5,.1,f"Moyenne des valeurs : {valmoyenne}")
plt.figtext(.2,.05,f"Valeur min : {valmin}")
plt.figtext(.5,.05,f"Valeur max : {valmax}")
plt.show()