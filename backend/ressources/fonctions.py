#  import lib
import numpy as np 
import pandas as pd 
import pickle 
from sklearn.metrics import silhouette_score
import seaborn as sns
import matplotlib.pyplot as plt 



def preprocessing(df): 

    df['Gender'] = df['Gender'].replace({'Male': 1, 'Female': 0})
    df=df.drop(columns=['CustomerID'])

    return df 



# train
def train_model(df,model): 
    save(df,model)
    pass 

def train_modeles (liste): 
    for model in liste : 
        save(train_modeles(model))



def save(df,model):
    save_image(df,model)
    save_score(df,model)
    save_model(model)


def save_model (model) : 
    # recupere le nom du model 
    name=model.__doc__.split()[0]
    # open a file, where you ant to store the data
    file = open("./../modeles/"+name+".pkl", 'wb')
    # dump information to that file
    pickle.dump(model, file)



# image
def make_image (df,model):
    sns.scatterplot(x=df["Annual Income (k$)"],y=df["Spending Score (1-100)"],hue=model.labels_, palette='viridis')

def save_image(df,model):
    make_image (df,model)
    plt.savefig(f"./../images/{model}.png")



# metriques  
def make_score (df,model):
    silhouette_coefficient = silhouette_score(df, model.labels_)
    return f"Silhouette Coefficient{silhouette_coefficient}:"
     
def save_score(df,model):
    with open (f"./../metriques/{model}.txt","w") as f : 
        f.write (make_score(df,model))


