import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from intensite import * #execute le intensite.py et récupère toutes ses fonctions

#recup les données du intensite.py
dico=getdico()

if len(dico)<5:     #verification que le pas n'est pas un peu trop petit
    print("le pas parait petit pour les valeurs données voulez vous arretez le programme et recommencer avec un pas plus adapté ?")
    print("nombres d'intervalles : "+str(len(dico)))
    relance=input("(y/n) : ")
    if relance=="y":
        exit()


# region #! valeurs et listes intiliales
listlambda=[]   #liste des longueur d'onde et des intensité compris dans l'intervalle donner
listintensite=[]    #pareil pour les intentsité
listintervalles=[]  #liste des intervalles contenant les valeurs souhaités
deb=float(input("Choississez un début d'intervalle : "))
fin=float(input("choississeez une fin d'intervalle : "))
# endregion

# region #! verifier les valeurs
if deb>getmax() or fin<getmin():
    print("intervalle non compris dans les données possibles, vueillez reverifiez les valeurs ci dessus")
    exit()

if deb<getmin():    #change les valeurs pour si les valeurs demandés sont plus petite ou plus grande que la valeur max
    deb=getmin()
if fin>getmax():
    fin=getmax()
# endregion

# region #! remplis les listes avec les valeurs des intervalles
for i in dico :
    listintervalles.append(dico.get(i)) #transformation du dictionnaire en liste car le dictionnaire ne peut pas être indexé pour la dichotomie (surement un moyen de résoudre ce problème ce qui eviterait de parcourir tout le dictionnaire puis la liste de ce dictionnaire)

premierintervalle=recherchedichotomique(listintervalles,deb)    #utilisation de la fonction dichotomique pour trouver les intervalles contenant la premiere et dernire valeur
for i in range(len(premierintervalle[0])):  #decoupage du premier intervalle pour obtenir que les valeur utiles
    if deb<=premierintervalle[0][i]<fin:
        listlambda.append(premierintervalle[0][i])
        listintensite.append(premierintervalle[1][i])
#si la valeur de début et de fin sont dans le même intervalle alors c'est terminé

if premierintervalle[0][-1]<fin: #cas où la valeur de fin est dans un autre intervalle
    dernierintervalle=recherchedichotomique(listintervalles,fin)
    for i in range(listintervalles.index(premierintervalle)+1,listintervalles.index(dernierintervalle)):    #ajout de l'entierté des intervalles entre le premier et dernier (ne fait rien si ils se suivent)
        listlambda+=listintervalles[i][0]
        listintensite+=listintervalles[i][1]
    for j in range(len(dernierintervalle[0])):  #découpage du dernier intervalle de la même manière que le premier
        if deb<=dernierintervalle[0][j]<fin:
            listlambda.append(dernierintervalle[0][j])
            listintensite.append(dernierintervalle[1][j])
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
# endregion

# region #! interface matplotlib
fig, ax = plt.subplots(figsize=(8,7))

ax.plot(listlambda,listintensite)
ax.set_xlabel("Longueur d'onde (nm)")
ax.set_ylabel("Intensité (coups)")
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
plt.figtext(.2,.13,f"Nombres de valeurs : {nbintensite}")
plt.figtext(.5,.13,f"Moyenne des valeurs : {valmoyenne}")
plt.figtext(.2,.08,f"Valeur min : {valmin}")
plt.figtext(.5,.08,f"Valeur max : {valmax}")
plt.show()
# endregion