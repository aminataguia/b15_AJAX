from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

images_folder = "./images"
metrics_folder = "./metriques"

adresse_image = [os.path.join(images_folder, file) for file in os.listdir(images_folder) if file.endswith(".png")]
adresse_metrics = [os.path.join(metrics_folder, file) for file in os.listdir(metrics_folder) if file.endswith(".txt")]

@app.get("/model/{model}")
async def collect_data(model: str):
    print(model)

    image_path = next((x for x in adresse_image if model in x), None)
    if image_path is None:
        raise HTTPException(status_code=404, detail="Image not found")
    return FileResponse(image_path, media_type="image/png")

@app.get("/metric/{model}")
async def collect_metrics(model: str):
    metric_path = next((x for x in adresse_metrics if model in x), None)
    if metric_path is None:
        raise HTTPException(status_code=404, detail="Metric not found")
    return FileResponse(metric_path, media_type="text/html")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

