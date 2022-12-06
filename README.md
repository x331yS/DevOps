# Docker

## 1. Docker Install

1. Installer Docker et Docker-Compose sur Ubuntu (https://docs.docker.com/get-docker/ &
   https://docs.docker.com/compose/install/)

2. Quelques commandes à tester
   - docker run hello-world
   Hello-world d’exemple avec Docker
   - docker run -it ubuntu bash
   Création d’un conteneur et utilisation d’un bash en interactif
   exit ou Ctrl+D - Pour sortir du conteneur
   - docker images
   Afficher les images Docker disponibles en local
   - docker ps -a
   Affiche tous les conteneurs (en exécution ou pas, grâce à l’option -a)
   - docker run -p 80:80 nginx et docker run -p -d 80:80 nginx
   Démarre un serveur web disponible sur votre navigateur à l’adresse
   localhost:80

3. Ressources supplémentaires pour découvrir Docker
   - https://docs.docker.com/get-started/02_our_app/
   - Et les autres articles du “Getting Started” Docker

## 2. Docker TP

4. Début du TP
   Initialiser un nouveau repository git qui vous permettra de sauvegarder les fichiers
   créés pendant le TP. Vous enverrez un zip du repository à la fin du TP avec vos
   réponses aux questions / exécutions et résultats sur la console dans des fichiers
   texte (Markdown par exemple) par e-mail.
   Utilisez git progressivement ! (Ne pas faire qu’un seul commit à la fin)

5. Exécuter un serveur web (apache, nginx, …) dans un conteneur docker
   a. Récupérer l’image sur le Docker Hub
![img.png](img.png)

   b. Vérifier que cette image est présente en local
![img_1.png](img_1.png)

   c. Créer un fichier index.html simple
   [index.html](index.html)

   d. Démarrer un conteneur et servir la page html créée précédemment à l’aide
   d’un volume (option -v de docker run)

   e. Supprimer le conteneur précédent et arriver au même résultat que
   précédemment à l’aide de la commande docker cp