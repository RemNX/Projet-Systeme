import os
import sys

#,à changer-------
#fichierdonnées=sys.argv[1]
#taillefenetre=sys.argv[2]
fichierdonnées="temp.txt"
taillefenetre=10
#,----------


def Strtolist(strl):
    return strl.strip('][').split(', ')


#!ouvrir le fichier de données
f=open(fichierdonnées,"r")
données=f.read()
listedonnées=données.split("\n")    #2 changer les données en une liste de chaque lignes

#!initiation de liste vide
dicodonnées={}      #2 dico final
longueurdonde=[]    #2 liste longueurs d'ondes
intensite=[]        #2 liste intensités
templist=[]         #2 liste temporaire pour faire une liste d'intervalles



for i in listedonnées:
    #2 choisir seulement les lignes qui contiennent des données
    if "#" not in i and ">" not in i:
        #2 créer une liste de 2 élements longueur et intensité
        valeur2=i.split("\t")

        #2 faire une liste des intensité et une liste des longueures d'ondes
        longueurdonde.append(float(valeur2[0]))
        intensite.append(float(valeur2[1]))

#2 créer l'intervalle définie par le pas
minintervalle=longueurdonde[0]
maxintervalle=minintervalle+taillefenetre
#2 parcourir la liste des longueures d'onde et intensité
for i in range(0,len(longueurdonde)):
    #2 vérifier si la valeur est compris dans l'intervalle du pas
    if minintervalle<=longueurdonde[i] and longueurdonde[i]<maxintervalle and (i+1!=len(longueurdonde)):
        templist.append(intensite[i])
    #2 lorsque la valeur lambda sort de l'intervalle
    else:
        #2 créer la clef et ajoute de la liste temporaire au dictionnaire
        clef=str([minintervalle,maxintervalle])
        dicodonnées[clef]=templist
        #2 changer l'intervalle pour passer a l'intervalle suivant
        minintervalle=maxintervalle
        maxintervalle=minintervalle+taillefenetre
        templist=[]
        templist.append(intensite[i])

#2 création d'un string qui affiche tous les intervalles ainsi que leurs index
affichagedico=""
for i in dicodonnées:
    affichagedico+="valeurs entre : ["+Strtolist(i)[0]+", "+Strtolist(i)[1]+"["+"\n"+str(dicodonnées[i])+"\n\n"

if __name__ =='__main__':
    print(affichagedico)

def getdico():
    return dicodonnées

def getintensite():
    return intensite

def getlambda():
    return longueurdonde