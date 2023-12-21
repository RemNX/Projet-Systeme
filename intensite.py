import sys

# region #! fonction utilitaires --------------------------------
def Strtolist(strl):    #fonction pour faire passer un string ayant la forme d'une liste directement en liste (pour les dictionnaires)
    return strl.strip('][').split(', ')

def decoupagestring(stringentier,rem1,rem2):  #fonction strip/slice modifiée afin de n'enlever que le premier et dernier caractère
    if rem1=="" and rem2=="":
        pass
    elif stringentier.startswith(rem1) and stringentier.endswith(rem2):
        return stringentier[len(rem1):-len(rem2)]
    elif stringentier.startswith(rem1):
        return stringentier[len(rem1):]
    elif stringentier.endswith(rem2):
        return stringentier[:-len(rem2)]
    return stringentier

def universaldelitmiter(listwithdelimiter): #fonction pour trouver n'importe quel delimiteur, donne la liste en entrer et ressort les élements avant et après les valeurs puis le delimiteur
    aenlever1=""        #premiers caractères qui ne sont pas des nombres
    aenlever2=""        #deniers caractères qui ne sont pas des nombres
    delimiteur=""       #delimitateur entre les colonnes

    firstline=listwithdelimiter[0]     #on execute le script uniquement sur la première ligne pour ne pas surcharger

    i=0
    while not firstline[i].isdigit():       #fonction pour trouver les élements entre les lignes qui ne sont pas des valeurs par exemple les guillements dans "45.12","55.12"
        aenlever1+=firstline[i]
        i+=1

    i=-1
    while not firstline[i].isdigit():
        aenlever2+=firstline[i]
        i-=1

    newfirstline=decoupagestring(firstline,aenlever1,aenlever2)        #prise de la première lignes avec seulement les valeurs et les delimiteurs, pour l'exemple : 45.12","55.12
    print(firstline)
    firstnondigitencounter=False        #condition pour aller jusqu'au premier caractère qui n'est pas un chiffre (debut du delimiteur)
    seconddigitencounter=False          #condition pour aller jusqu'a la fin du delimiteur
    i=0
    while not (firstnondigitencounter and seconddigitencounter) and i<=len(newfirstline)-1:
        if not (newfirstline[i].isdigit() or newfirstline[i] in [",",".",":"] or firstnondigitencounter):   #verifier a partir de quand le caractère n'est plus la valeur
            firstnondigitencounter=True
        if firstnondigitencounter and not newfirstline[i].isdigit():                                    #ajouter les caractere au delimiteur jusqu'au prochain chiffre
            delimiteur+=newfirstline[i]
        elif firstnondigitencounter and newfirstline[i].isdigit():                                      #stop de le boucle a partir de la fin du delimiteur
            seconddigitencounter=True
        i+=1
        if i==len(newfirstline):
            print("il n'existe qu'une seule colonne de valeur veuillez entrer une plage de données acceptable")
    return aenlever1, aenlever2, delimiteur

def recherchedichotomique(listeafouiller,objetarechercher): #fonction permettant d'effectuer une recherche dichotomique sur la premiere colonne d'une plage de donnée a deux colonne sous forme de liste. prend en entrée la liste de 2 listes ainsi que la cible et renvoie en une dizaine d'étape maximum l'intervalle dans laquelle la valeur est compris.
    index=len(listeafouiller)//2
    milieu=listeafouiller[index]
    ajoutindice=index//2 #variable importante qui effectue le retrecissement sur l'index
    if objetarechercher<listeafouiller[0][0][0] or objetarechercher>listeafouiller[-1][0][-1]:
        print("la cible n'est pas compris dans la liste veuillez verifiez vos données")
        exit()
    while (objetarechercher<milieu[0][0] or objetarechercher>=milieu[0][-1]) and index<=len(listeafouiller): #condition pour savoir si la valeur est compris entre le premier et dernier membre de l'intervalleet que l'index ne sorte pas de la boucle
        if objetarechercher>milieu[0][-1] and ajoutindice not in [0,1]:  #cas ou le nombre recherché est plus grand que le centre
            index=index + ajoutindice
        elif objetarechercher>milieu[0][-1] and ajoutindice in [0,1]:  #cas particulier où l'ajout pour l'index est 0 ou 1 et donc sa division entière donne 0
            index+=1
        elif objetarechercher<milieu[0][0] and ajoutindice in [0,1]: #pareil mais vers le bas
            index-=1
        elif objetarechercher==listeafouiller[-1][0][-1]:   #cas particulier où la valeur recherché est la toute dernière de la liste
            index=len(listeafouiller)
            break
        elif objetarechercher==listeafouiller[0][0][0]:     #cas particulier où la valeur recherchée est la première de la liste
            index=0
            break
        else:
            index=index - ajoutindice  #cas ou le nombre recherché est plus petit que le centre
        milieu=listeafouiller[index]
        ajoutindice=ajoutindice//2  #retrecissement de moitié sur l'intervalle dans lequel est la valeur
    return milieu
# endregion

# region #! Ouvrir le fichier de données --------------------------
fichierdonnées=sys.argv[1]         #récupération du fichir
f=open(fichierdonnées,"r")
données=f.read()
listedonnées=données.split("\n")    # changer les données en une liste de chaque lignes

taillefenetre=float(sys.argv[2])    #récuperation du pas
# endregion

# region #! Initiation de liste vide ----------------------------------------------
commentaire=""      #variable contenant les commentaires dans lefichier
dicodonnées={}      #variable contenant le dictionnaire finale permettant de faire passer les données au programme de traitement
longueurdonde=[]    # liste longueurs d'ondes
intensite=[]        # liste intensités
templistinte=[]     # liste temporaire pour les intensité d'un intervalle
templistlamb=[]     #liste temporaire pour les longueur d'onde d'un intervalle
# endregion

# region #! Création de la liste des valeurs de lambda et d'intensité ----------------------------
newlist=[]
for i in listedonnées:          #parcours de la liste pour ne garder que les lignes contenant les valeurs
    if "#" not in i and ">" not in i:
        newlist.append(i)
    elif "#" == i[0]:                    #ajoute les commentaires pour un print final
        commentaire+=i+"\n"

rem1,rem2,delimiter=universaldelitmiter(newlist) #récuperation des caractère genants ainsi que du delimiteur

#verification si il y a 2 colonnes et demande à laquelle choisir si il y en a plus de 2
indexlambda=0
indexintensite=1
nombrescolonnes=len(decoupagestring(newlist[0],rem1,rem2).split(delimiter))
if nombrescolonnes>2:
    print("il existe plus de deux colonnes indiquez le numero de la colonne de longueur d'onde puis celle d'intensité")
    indexlambda=int(input("numero de la colonne longueur d'onde (1-"+str(nombrescolonnes)+") : "))-1
    indexintensite=int(input("numero de la colonne d'intensité (1-"+str(nombrescolonnes)+"): "))-1

#besoin de changer la liste en deux liste de valeur pour permettre d'effectuer des opérations algebrique (actuellement un string)
if rem1=="" and rem2=="": #méthode sans split pour gagner du temps dans la plupart des cas
    for i in newlist:
        listligne=i.split(delimiter)
        longueurdonde.append(round(float(listligne[indexlambda].replace(",",".")),3))   #gère les exceptions pour les fichier csv avec des virgules + arrondis les erreur de decimal
        intensite.append(round(float(listligne[indexintensite].replace(",",".")),3))
else:
    for i in newlist:
        listligne=decoupagestring(i,rem1,rem2).split(delimiter)
        longueurdonde.append(round(float(listligne[indexlambda].replace(",",".")),3))
        intensite.append(round(float(listligne[indexintensite].replace(",",".")),3))
# endregion

# region #! création du dictionnaire -----------------------------

minintervalle=longueurdonde[0]              #definition da la limite de l'intervalle en fonction du pas
maxintervalle=minintervalle+taillefenetre
for i in range(0,len(longueurdonde)):       #parcourir la liste des longueur d'onde et verifier si la valeur est compris dans l'intervalle puis ajouter les valeurs de lambda et d'intensité aux listes temporaires
    if minintervalle<=longueurdonde[i] and longueurdonde[i]<maxintervalle and (i+1!=len(longueurdonde)):
        templistinte.append(intensite[i])
        templistlamb.append(longueurdonde[i])

    else:           #quand la valeur de lambda sort de l'interval met les listes dans le dictionnaire avec l'intervalle en clef
        templistinte.append(intensite[i])
        templistlamb.append(longueurdonde[i])
        dicodonnées[str(templistlamb[0])+", "+str(templistlamb[-1])]=[templistlamb,templistinte]
        minintervalle=maxintervalle         #redefininr l'intervalle en fonction des nouvelle valeurs
        maxintervalle=minintervalle+taillefenetre
        templistinte=[]
        templistlamb=[]
        templistlamb.append(longueurdonde[i])
        templistinte.append(intensite[i])
# endregion

# region #! fonction transmission et affichage ------------------------------
print(commentaire)
print("intervalles possible entre "+ str(longueurdonde[0])+" et "+str(longueurdonde[-1]))
print("["+list(dicodonnées.keys())[0]+"[...["+list(dicodonnées.keys())[-1]+"[")

def getmin():
    return longueurdonde[0]  #verifier si l'intervalle donner correspond a des valeurs

def getmax():
    return longueurdonde[-1]

def getdico():
    return dicodonnées #permet de récuperer le dictionnaire de valeur
# endregion