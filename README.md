# Projet de Clustering de Segmentation de Clientèle

## Introduction
Ce projet vise à développer une application web qui utilise des modèles de clustering pour segmenter les clients d'un centre commercial. L'application comprendra un back-end qui propose au moins trois modèles de clustering sur la base de données "Mall Customer Segmentation", ainsi qu'une interface web permettant de choisir dynamiquement entre différents modèles avec AJAX et d'afficher un indicateur de performance associé.

## Livrables

Backend :
Le back-end sera développé en Python et comprendra les éléments suivants :

3-Modèles.py : Le code Python contenant l'entraînement des trois modèles de clustering (KMeans, DBSCAN, Agglomerative Clustering).
Visualisation des modèles : Un graphique pour chaque modèle de clustering, illustrant les résultats du clustering.
Enregistrement des modèles : Chaque modèle entraîné sera enregistré dans un fichier .pkl pour une utilisation ultérieure.
Coefficients de silhouette : Un fichier texte contenant les coefficients de silhouette pour chaque modèle, évaluant la qualité des clusters formés.
.gitignore : Un fichier .gitignore pour exclure les fichiers et dossiers non nécessaires du suivi de version Git.

Frontend
Le front-end sera développé en utilisant HTML, CSS et JavaScript, et comprendra les éléments suivants :

Statics : Un dossier contenant les fichiers CSS pour le style de l'application.
Templates : Un dossier contenant les fichiers HTML pour les différentes pages de l'application, y compris main_page.html pour la page principale.
Autres fichiers
.git : Le dossier .git pour le suivi de version Git.
README.md : Un fichier README détaillant le projet, les instructions d'installation et d'utilisation, ainsi que toute autre information pertinente.
Conclusion


