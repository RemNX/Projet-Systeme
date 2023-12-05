# delimitateur
# ajout csv
#afficher les commentaires du fichier

#option affiche tout le graph sans demander debut et fin
#commentaire git instruction


#region #!paramètre et desc
Help()
{
    echo "Programme prenant en entrée un jeu de donnée ainsi qu'un pas et en ressort les valeurs triés par intervalles de la taille du pas puis possiblité d'effectuer un graph d'un ou des intervalles choisis."
    echo
    echo "Syntax: scriptTemplate [-h|V|a]"
    echo "options:"
    echo "h     Affiche cette fenêtre."
    echo "V     Affiche la version"
    echo "a     Affiche l'integralité des valeurs sans demander d'intervalles"
    echo
}

while getopts ":h" option; do
    case $option in
        h)
        Help
        exit;;
    esac
done
#endregion

#region #!----Verification sur intensite.py-----
#,verification sur les paramètres
if ! [[ $2 =~ ^[0-9.]+$ ]];then
    echo le pas n\'est pas un nombre positif
    exit
elif (( $2 == 0 ));then
    echo le pas ne peut pas être égal à \0
    exit
fi

#, verification de l'extension
ext=${1##*.}
if [[ $ext != txt ]];then
    echo les seules extensions acceptés sont .txt
    exit
fi
#endregion

python3 intensite.py $1 $2

echo choissisez un début d\'intervalle
read deb

echo choissisez une fin d\'intervale
read fin

#region #!----Verification sur recherch_plot.py-------
#, verification caractères intervalle
if ! ([[ $deb =~ ^[0-9.-]+$ ]] && [[ $fin =~ ^[0-9.]+$ ]]);then
    echo l\'intervalles n\'est pas un nombre
    exit
fi

if (( $deb >= $fin ));then
    echo la fin d\'intervalle doit être plus grand que le début
    exit
fi
#endregion

#problème du intensite.py importé qui essaye d'utiliser le $deb et $fin en $1 et $2
python3 recherche_plot.py $1 $2 $deb $fin