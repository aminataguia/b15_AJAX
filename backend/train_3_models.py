#  import lib
import numpy as np 
import pandas as pd 
import sklearn.cluster as models

from ressources.fonctions import * 


data=pd.read_csv("ressources/Mall_Customers.csv")

df = preprocessing(data)

model=models.KMeans(n_clusters=5, random_state=0, n_init="auto").fit(df)
save(df,model)
model=models.DBSCAN(eps=9, min_samples=3).fit(df)
save(df,model)
model=models.AgglomerativeClustering(n_clusters=5).fit(df)
save(df,model)



