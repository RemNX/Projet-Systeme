#nombre negatifs en entré
#erreur caractère dans l'entrée
#delimitateur
#pas la bonne extension
#si nombre fin plus grand que le debut
#si debut intervalle trop élevé ou fin trop bas

#option affiche tout le graph sans demander debut et fin


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

python3 intensite.py $1 $2

echo choissisez un début d\'intervalle
read deb

echo choissisez une fin d\'intervale
read fin

#problème du intensite.py importé qui essaye d'utiliser le $deb et $fin en $1 et $2
python3 recherche_plot.py $1 $2 $deb $fin