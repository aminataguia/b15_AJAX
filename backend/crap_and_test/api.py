from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sklearn.cluster import KMeans
from joblib import load
import pandas as pd
from sklearn.metrics import silhouette_score

app = FastAPI()

# CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Load the trained KMeans model
model = load(r'C:\Users\Utilisateur\Documents\GitHub\b15-AJAX\AJAX-clustering\backend/kmeans_model.pkl')

# Define input data model
class InputData(BaseModel):
    spending_scores: List[float]
    annual_incomes: List[float]

# # Endpoint to make predictions
# @app.get("/api/predict")
# async def predict_clusters(spending_scores: List[float] = Query(...), annual_incomes: List[float] = Query(...)):
#     input_data = pd.DataFrame({
#         "Spending Score (1-100)": spending_scores,
#         "Annual Income (k$)": annual_incomes
#     })
#     y_predicted = model.predict(input_data)
#     return {"clusters": y_predicted.tolist()}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)

# df = pd.DataFrame({
#     "Spending Score (1-100)": [40, 60, 10, 90, 20],
#     "Annual Income (k$)": [50, 70, 20, 100, 30]
# })
@app.get("/api/mkl/models")
async def predict_clusters_and_score(spending_scores: list = Query(...), annual_incomes: list = Query(...)):
    input_data = pd.DataFrame({
        "Spending Score (1-100)": spending_scores,
        "Annual Income (k$)": annual_incomes
    })
    
    # Predict clusters
    y_predicted = model.predict(input_data)
    
    # Calculate silhouette score
    silhouette_avg = silhouette_score(input_data, y_predicted)
    
    return {"clusters": y_predicted.tolist(), "silhouette_score": silhouette_avg}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)