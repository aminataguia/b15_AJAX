from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse,FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn 
import os
import sys 





app=FastAPI()


# load css et template 
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# load images 

# Chemin complet vers le dossier d'images et de metriques 
# images_folder = os.path.join(os.getcwd(), "images")
# metrics_folder = os.path.join(os.getcwd(), "metriques")
# images_folder = r"C:\Users\Utilisateur\Desktop\projets\briefs\b15\github\AJAX-clustering/images"
# metrics_folder =r"C:\Users\Utilisateur\Desktop\projets\briefs\b15\github\AJAX-clustering/metriques"
images_folder = "./images"
metrics_folder ="./metriques"

# Liste des fichiers avec l'extension .png dans le dossier d'images
adresse_image = [images_folder+"/"+file for file in os.listdir(images_folder) if file.endswith(".png")]

# adresse_image = [file for file in os.listdir("./images/") if file.split(".")[-1]=="png"]
print(f"taille du fichier d'adresse image : {len(adresse_image)}")

# load metrics
# adresse_metrics = [ file for file in os.listdir("./metriques/") if file.split(".")[-1]=="txt"]
adresse_metrics = [metrics_folder+"/"+file for file in os.listdir(metrics_folder) if file.endswith(".txt")]
print(f"taille du fichier d'adresse metrics : {len(adresse_metrics)}")




# Main page 
@app.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("main_page.html",{"request": request})


# get image
@app.get("/model/{model}")
async def collect_data(model):
    image = [x for x in adresse_image if  model in x ][0]
    return  FileResponse(image, media_type="image/png")


# get metrics
@app.get("/metric/{model}")
async def collect_data(model):
    metric = [x for x in adresse_metrics if  model in x ][0]
    # return "mse"
    return FileResponse(metric, media_type="text/html")




if __name__=="__main__" : 
    uvicorn.run(app) 

