#TODO traduction anglais


#region #!paramètre et description
Help()
{
    echo "Programme permettant d'afficher un graph d'intensité en fonction d'une longueur d'onde depuis un fichier de valeurs.
prend en entrée le fichier puis un pas qui si non specifié est par défaut de 10nm.
exemple : ./main.sh Spectre_photoluminescence.txt 8"
    echo
    echo "Syntax: scriptTemplate [-h|V]"
    echo "options:"
    echo "h     Affiche cette fenêtre."
    echo "V     Affiche la version"
    echo
}

if [ $# -eq 0 ]; then   #renvoie l'aide si le programme est lancé sans paramètre
    Help
    exit 1
    fi

if [ $# -eq 1 ];then    #donne un pas par défaut de 10 si celui ci n'est pas préciser
    pas=10
else
    pas=$2
fi

fichier=$1  #premier argument est le nom du fichier


while getopts ":hV" option; do
    case $option in
        h)
        Help
        exit;;
        V)
        echo 1.0.0
        exit;;
    esac
done
#endregion

#region #!----Verification sur intensite.py-----
#,verification sur les paramètres
if ! [[ $pas =~ ^[0-9.]+$ ]];then
    echo le pas n\'est pas un nombre positif
    exit
elif (( $pas == 0 ));then
    echo le pas ne peut pas être égal à \0
    exit
fi

#, verification de l'extension
ext=${fichier##*.}
if [[ $ext != txt ]] && [[ $ext != csv ]];then
    echo les seules extensions acceptés sont .txt et .csv
    exit
fi
#endregion

python3 recherche_plot.py $fichier $pas