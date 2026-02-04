Ouvrir un terminal puis afficher le répertoire courant
Utiliser la commande ls sans option ni argument
Créer un nouveau dossier nommé Dossier1
Utiliser la commande ls sans option ni argument. Que remarquez-vous ?
Déplacez-vous dans le répertoire ./Dossier1
Vérifier que vous êtes bien arrivé !
Puis créer un fichier vide nommé fic1.txt dans ce dossier.
Revenir dans le répertoire /workspaces/GpeMercredi
Utiliser la commande ls -F . Que remarquez-vous ?
Réaliser deux copies de fic1.txt :
fic2.txt dans le répertoire ./Dossier1
fic3.txt dans le répertoire /workspaces/GpeMercredi
Renommer le fichier fic1.txt en fichierNSI . Commenter.
Utiliser la commande tree pour contrôler le résultat.
Utiliser la commande cd ../ puis pwd . Que remarquez-vous ?
Supprimer le dossier /workspaces/GpeMercredi/Dossier1 avec la commande rmdir. Commenter.
Utiliser la commande rm -ir /workspaces/GpeMercredi/Dossier1 . Répondez y(yes) ou n(no).
Afficher une aide sur la commande rm . Quel est le rôle de l’option -i ?
Créer les dossiers suivants :
/workspaces/GpeMercredi/DA
/workspaces/GpeMercredi/DA/DB
/workspaces/GpeMercredi/DA/DC`
Utiliser la commande tree pour contrôler.
Se déplacer dans le dossier /workspaces/GpeMercredi/DA/DC et vérifier que vous êtes bien arrivé !
Utiliser la commande cd ../../ et commenter.
Ouvrir le fichier fic3.txt avec l’éditeur nano
Ecrire 3 fois la ligne "J’aime NSI", 2 fois la ligne "J’aime bien lire aussi" et 1 fois "Bye"
Appuyer sur Ctrl+x pour demander à quitter l’éditeur et valider avec la touche y
Afficher les 4 premières lignes de fic3.txt
Afficher les 3 dernières lignes de fic3.txt
Afficher le contenu du fichier dans la console.
Rechercher le mot "aime" dans le fichier fic3.txt et commenter.
Appliquer la commande uniq à fic3.txt et commenter.
Appliquer la commande sort à fic3.txt et commenter.
Afficher le nombre de lignes et de mots dans fic3.txt
Afficher tous les fichiers et dossiers cachés du répertoire /workspaces/GpeMercredi

correction

- pwd
- ls
- mkdir ./Dossier1
- ls => Le nom Dossier1 apparait surligné en vert
- cd ./Dossier1
- pwd
- touch ./fic1.txt
- cd ../ ou cd /workspaces/GpeMercredi
- ls -F ajoute un slash après les dossiers
- cp ./Dossier1/fic1.txt ./Dossier1/fic2.txt puis cp ./Dossier1/fic1.txt ./fic3.txt
- mv ./Dossier1/fic1.txt ./Dossier1/fichierNSI (Les extensions de fichiers ne sont pas obligatoires)
tree
- cd ../ && pwd (on enchaine les commandes) : On est remonté d'un range dans l'arboresence
- rmdir ne supprime que des dossiers vides
- rm -i pose une question avant chaque opération
- mkdir ./DA/DC && pwd
- cd ../../ pour remonter de deux rangs
- On peut éditer le fichier avec nano pour écrire les lignes ou utiliser echo avec l'option -e
    echo -e "J'aime la NSI
> J'aime la NSI" > ./fic3.txt
- head -n 4 ./fic3.txt
- tail