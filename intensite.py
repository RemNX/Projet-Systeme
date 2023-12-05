import sys

fichierdonnées=sys.argv[1]         #récupération des donnnées lors de l'exectution du script
taillefenetre=float(sys.argv[2])

# region #! fonction utilitaires
def Strtolist(strl):    #fonction pour faire passer un string ayant la forme d'une liste directement en liste (pour les dictionnaires)
    return strl.strip('][').split(', ')

# endregion

# region #! Ouvrir le fichier de données
f=open(fichierdonnées,"r")
données=f.read()
listedonnées=données.split("\n")    # changer les données en une liste de chaque lignes

# endregion

# region #! Initiation de liste vide
dicodonnées={}      # dico final
longueurdonde=[]    # liste longueurs d'ondes
intensite=[]        # liste intensités
templistinte=[]     # liste temporaire pour les intensité d'un intervalle
templistlamb=[]     #liste temporaire pour les longueur d'onde d'un intervalle
# endregion

# region #! Création de la liste des valeurs de lambda et d'intensité
for i in listedonnées:
    if "#" not in i and ">" not in i:     #enlever toutes les lignes qui contiennent du commentaire

        valeur2=i.split("\t")           #créer une liste des longueurs d'ondes et des intensités
        longueurdonde.append(round(float(valeur2[0]),3))
        intensite.append(round(float(valeur2[1]),3))
# endregion

# region #! création du dictionnaire
minintervalle=longueurdonde[0]              #definition da la limite de l'intervalle en fonction du pas
maxintervalle=minintervalle+taillefenetre
for i in range(0,len(longueurdonde)):       #parcourir la liste des longueur d'onde et verifier si la valeur est compris dans l'intervalle puis ajouter les valeurs de lambda et d'intensité aux listes temporaires
    if minintervalle<=longueurdonde[i] and longueurdonde[i]<maxintervalle and (i+1!=len(longueurdonde)):
        templistinte.append(intensite[i])
        templistlamb.append(longueurdonde[i])

    else:           #quand la valeur de lambda sort de l'interval met les listes dans le dictionnaire avec lambda en clef et les intensités en valeurs
        dicodonnées[str(templistlamb)]=templistinte
        minintervalle=maxintervalle         #redefininr l'intervalle en fonction des nouvelle valeurs
        maxintervalle=minintervalle+taillefenetre
        templistinte=[]
        templistlamb=[]
        templistlamb.append(longueurdonde[i])
        templistinte.append(intensite[i])
# endregion

# region #! affichage du dictionnaire dans bash
#création d'un string qui affiche tous les intervalles ainsi que leurs index
affichagedico=""
for i in dicodonnées:
    affichagedico+="valeurs entre : ["+Strtolist(i)[0]+", "+Strtolist(i)[-1]+"["+"\n"+str(dicodonnées[i])+"\n\n"
# endregion

# region #! fonction transmission
if __name__ =='__main__':
    print(affichagedico)
    print("intervalles possible entre "+ str(longueurdonde[0])+" et "+str(longueurdonde[-1]))

def getmin():
    return longueurdonde[0]

def getmax():
    return longueurdonde[-1]

def getdico():
    return dicodonnées
# endregion