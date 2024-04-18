import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import pandas as pd 
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.metrics import silhouette_score
from sklearn.cluster import AgglomerativeClustering
import os
import pickle

# Ignorer les avertissements
import warnings
warnings.simplefilter(action='ignore', category=Warning)

# Charger les données
df = pd.read_csv("Mall_Customers.csv")

# preprocessing 
df.loc[df['Gender']=='Male']=1
df.loc[df['Gender']=='Female']=0

# Sélectionner les colonnes pour le clustering
X = df.drop(columns=['CustomerID'], axis=1).values #, 'Age', 'Gender'

# Modèle KMeans
wsse = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=2)
    kmeans.fit(X)
    wsse.append(kmeans.inertia_)

# Spécifiez et crée le chemin du dossier
dossier_plt = "plt"
chemin_dossier1 = os.path.join(os.getcwd(), dossier_plt)
os.makedirs(chemin_dossier1, exist_ok=True)

dossier_modeles = "modeles"
chemin_dossier_modeles = os.path.join(os.getcwd(), dossier_modeles)
os.makedirs(chemin_dossier_modeles, exist_ok=True)

dossier_silhouettes = "silhouettes"
chemin_dossier_silhouettes = os.path.join(os.getcwd(), dossier_silhouettes)
os.makedirs(chemin_dossier_silhouettes, exist_ok=True)

# Enregistrez le graphique
nom_fichier = "modele-kmeans.png"
chemin_fichier = os.path.join(chemin_dossier1, nom_fichier)

# Appliquer KMeans avec le nombre optimal de clusters
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

# Visualiser les clusters
plt.figure(figsize=(15, 8))
cluster_centers = kmeans.cluster_centers_
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='black', marker='o', s=200, label='Centres de clusters')
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=df['Cluster'], palette='viridis', s=100)
plt.title('Clustering KMeans')
plt.legend(title='Clusters', loc='upper right')

# Enregistrez le graphique avant de l'afficher
plt.savefig(chemin_fichier)

# Afficher le graphique
plt.show()

# Enregistrer le modèle KMeans
nom_fichier_kmeans = "kmeans_model.pkl"
chemin_fichier_kmeans = os.path.join(chemin_dossier_modeles, nom_fichier_kmeans)
with open(chemin_fichier_kmeans, 'wb') as f:
    pickle.dump(kmeans, f)

# Calcul du coefficient de silhouette pour évaluer la qualité des clusters
silhouette_coefficient = silhouette_score(X, kmeans.labels_)
print("Coefficient de Silhouette (KMeans):", silhouette_coefficient)

# Enregistrer le coefficient de silhouette pour KMeans
nom_fichier_silhouette_kmeans = "silhouette_kmeans.txt"
chemin_fichier_silhouette_kmeans = os.path.join(chemin_dossier_silhouettes, nom_fichier_silhouette_kmeans)
with open(chemin_fichier_silhouette_kmeans, 'w') as f:
    f.write(f"Coefficient de Silhouette (KMeans): {silhouette_coefficient}\n")

# Modèle DBSCAN
# Appliquer le clustering DBSCAN
dbscan = DBSCAN(eps=9, min_samples=3)
clusters = dbscan.fit_predict(X)

# Visualiser les clusters DBSCAN
plt.figure(figsize=(15, 8))
unique_labels = np.unique(clusters)
for label in unique_labels:
    if label == -1:
        plt.scatter(X[clusters == label, 0], X[clusters == label, 1], c='black', marker='o', label=f'Points isolés ({label})')
    else:
        plt.scatter(X[clusters == label, 0], X[clusters == label, 1], label=f'Cluster {label}')
plt.title('Clustering DBSCAN')
plt.xlabel('Revenu annuel (k$)')
plt.ylabel('Score de dépenses (1-100)')
plt.legend(title='Clusters (DBSCAN)', loc='upper right')

# Enregistrez le graphique avant de l'afficher
nom_fichier_dbscan = "clustering-dbscan.png"
chemin_fichier_dbscan = os.path.join(chemin_dossier1, nom_fichier_dbscan)
plt.savefig(chemin_fichier_dbscan)

# Afficher le graphique
plt.show()

# Enregistrer le modèle DBSCAN
nom_fichier_dbscan = "dbscan_model.pkl"
chemin_fichier_dbscan = os.path.join(chemin_dossier_modeles, nom_fichier_dbscan)
with open(chemin_fichier_dbscan, 'wb') as f:
    pickle.dump(dbscan, f)

# Évaluation des clusters DBSCAN
n_clusters_ = len(set(clusters)) - (1 if -1 in clusters else 0)  
n_noise_ = list(clusters).count(-1)
if n_clusters_ > 1 or n_noise_ > 0:
    silhouette_coefficient = silhouette_score(X, clusters)
    print("Coefficient de Silhouette (DBSCAN):", silhouette_coefficient)
else:
    print("Coefficient de Silhouette non applicable pour 1 cluster ou uniquement du bruit.")

# Enregistrer le coefficient de silhouette pour DBSCAN
nom_fichier_silhouette_dbscan = "silhouette_dbscan.txt"
chemin_fichier_silhouette_dbscan = os.path.join(chemin_dossier_silhouettes, nom_fichier_silhouette_dbscan)
with open(chemin_fichier_silhouette_dbscan, 'w') as f:
    f.write(f"Coefficient de Silhouette (DBSCAN): {silhouette_coefficient}\n")

# Clustering hiérarchique
# Définir le nombre de clusters pour le clustering hiérarchique agglomératif
n_clusters = 4

# Appliquer le clustering hiérarchique agglomératif
agg_clustering = AgglomerativeClustering(n_clusters=n_clusters).fit(X)
agg_clusters = agg_clustering.labels_

# Visualiser les clusters du clustering hiérarchique agglomératif
plt.figure(figsize=(15, 8))
sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=agg_clusters, palette='viridis', s=100)
plt.title('Clustering hiérarchique agglomératif')
plt.legend(title='Clusters', loc='upper right')

# Enregistrez le graphique avant de l'afficher
nom_fichier_agg = "clustering-hierarchique-agglomeratif.png"
chemin_fichier_agg = os.path.join(chemin_dossier1, nom_fichier_agg)
plt.savefig(chemin_fichier_agg)

# Afficher le graphique
plt.show()

# Enregistrer le modèle AgglomerativeClustering
nom_fichier_agg = "agg_model.pkl"
chemin_fichier_agg = os.path.join(chemin_dossier_modeles, nom_fichier_agg)
with open(chemin_fichier_agg, 'wb') as f:
    pickle.dump(agg_clustering, f)

# Calcul du coefficient de silhouette pour le clustering hiérarchique
silhouette_coefficient_agg = silhouette_score(X, agg_clusters)
print("Coefficient de Silhouette (Clustering hiérarchique agglomératif):", silhouette_coefficient_agg)

nom_fichier_silhouette_agg = "silhouette_agg.txt"
chemin_fichier_silhouette_agg = os.path.join(chemin_dossier_silhouettes, nom_fichier_silhouette_agg)
with open(chemin_fichier_silhouette_agg, 'w') as f:
    f.write(f"Coefficient de Silhouette (Clustering hiérarchique agglomératif): {silhouette_coefficient_agg}\n")
