import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from intensite import *

#recup les données du intensite.py
dico=getdico()

# region #! valeurs et listes intiliales
listlambda=[]
listintensite=[]
listintervalles=[]
deb=float(sys.argv[3])
fin=float(sys.argv[4])
# endregion

# region #! verifier les valeurs (impossible en bash)
if deb>getmax() or fin<getmin():
    print("intervalle non compris dans les données possibles")
    exit()

# endregion

# region #! remplis les listes avec les valeurs des intervalles
for i in dico:
    clef1=float(Strtolist(i)[0])
    clef2=float(Strtolist(i)[-1])
    lamb=Strtolist(i)
    # cherche tous les intervalles compris entre le début et la fin choisis par l'utilisateur
    if clef2>deb and clef1<fin:
        listintervalles.append(i)
        listlambda+=lamb
        listintensite+=dico.get(i)
# endregion

# region #! calcul des valeurs (moyennes, max, etc)
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
if len(listintervalles)==1:
    textintervalles=f"les valeurs sont comprises dans [{Strtolist(listintervalles[0])[0]} ; {Strtolist(listintervalles[0])[-1]}["
elif len(listintervalles)>1:
    textintervalles=f"Les valeurs sont comprises entre les intervalles [{Strtolist(listintervalles[0])[0]} ; {Strtolist(listintervalles[0])[-1]}[ et [{Strtolist(listintervalles[-1])[0]} ; {Strtolist(listintervalles[-1])[-1]}["

# endregion

# region #! interface matplotlib
fig, ax = plt.subplots(figsize=(8,7))

ax.plot(listlambda,listintensite)

#léger problème incomprehensible sur le nombre de valeurs affiché en abscisse
listvaleuraaaffiche=[0,.2*len(listlambda),.4*len(listlambda),.6*len(listlambda),.8*len(listlambda),.99*len(listlambda)]
plt.xticks(listvaleuraaaffiche)

ax.set_xlabel("Longueur d'onde (nm)")
ax.set_ylabel("Intensité (coups)")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
plt.figtext(.2,.13,f"Nombres de valeurs : {nbintensite}")
plt.figtext(.5,.13,f"Moyenne des valeurs : {valmoyenne}")
plt.figtext(.2,.08,f"Valeur min : {valmin}")
plt.figtext(.5,.08,f"Valeur max : {valmax}")
plt.figtext(.2,.02,textintervalles)
plt.show()
# endregion