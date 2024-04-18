# Spécification de l'api

## Description global de l'API

L'API fournit une interface pour observer la performance de modèles de clustering.

A Venir : possibilité d'entrainer les modeles avec les parametre demandé , de chercher les meilleurs meta-parametres.


### Endpoints :

    Page Principale (/) :
        Type: GET
        Description: Cette page renvoie la page principale de votre application web.
        Paramètres : Aucun
        Réponse : HTMLResponse contenant la page principale.

    Récupération des Images (/model/{model}) :
        Type: GET
        Description: Récupère l'image associée à un modèle spécifique.
        Paramètres :
            model : Le nom du modèle dont vous voulez récupérer l'image.
        Réponse : Le fichier image correspondant au modèle enregistré dans le répertoire images.

    Récupération des Métriques (/metric/{model}) :
        Type: GET
        Description: Récupère les métriques associées à un modèle spécifique.
        Paramètres :
            model : Le nom du modèle dont vous voulez récupérer les métriques.
        Réponse : Le fichier de métriques correspondant au modèle enregistré dans le répertoire metriques.

### Répertoires :

    Répertoire des Images (./images)
        Ce répertoire contient les images associées à chaque modèle.

    Répertoire des Métriques (./metriques)
        Ce répertoire contient les fichiers de métriques associés à chaque modèle.

### Fonctionnalités :

    Chargement des ressources :
        Les images et les fichiers de métriques sont chargés au démarrage de l'application à partir des répertoires spécifiés (images_folder et metrics_folder).
        Les Datas fournis sont changer dynamiquement en fonction de la selection du menu deroulant par l'utilisateur

    Gestion des Erreurs :
        Si un modèle spécifié n'existe pas dans les répertoires, l'API renverra une erreur.

    Formats de Fichier :
        Les images sont renvoyées avec le type de média "image/png".
        Les fichiers de métriques sont renvoyés avec le type de média "text/html".

    Serveur de Développement :
        L'API peut être exécutée localement en utilisant Uvicorn.
