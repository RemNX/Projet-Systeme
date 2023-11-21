# delimitateur
#1 pas la bonne extension
# si nombre fin plus grand que le debut
# si debut intervalle trop élevé ou fin trop bas

#option affiche tout le graph sans demander debut et fin



#region #!paramètre et desc
Help()
{
    echo "Programme prenant en entrée un jeu de donnée ainsi qu'un pas et en ressort les valeurs triés par intervalles de la taille du pas puis possiblité d'effectuer un graph d'un ou des intervalles choisis."
    echo
    echo "Syntax: scriptTemplate [-h|V]"
    echo "options:"
    echo "h     Affiche cette fenêtre."
    echo "V     Affiche la version"
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

#,verification sur les paramètres
if ! [[ $2 =~ ^[0-9.]+$ ]];then
    echo le pas n\'est pas un nombre positif
    exit
elif (( $2 == 0 ));then
    echo le pas ne peut pas être égal à \0
    exit
fi

#, verification de l'extension


#python3 intensite.py $1 $2

echo choissisez un début d\'intervalle
read deb

echo choissisez une fin d\'intervale
read fin

#, verification caractères intervalle
if ! ([[ $deb =~ ^[0-9.-]+$ ]] && [[ $fin =~ ^[0-9.]+$ ]]);then
    echo l\'intervalles n\'est pas un nombre
    exit
fi

#problème du intensite.py importé qui essaye d'utiliser le $deb et $fin en $1 et $2
python3 recherche_plot.py $1 $2 $deb $fin