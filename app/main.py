import os
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Define the request model based on Iris dataset features
class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Define the response model
class PredictionResponse(BaseModel):
    prediction: int
    species: str

app = FastAPI(title="ML Auto Deployment API", description="API to serve Iris species predictions")

# Map integer predictions to species names
SPECIES_MAP = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

# Global variable to hold the model
model = None

@app.on_event("startup")
def load_model():
    global model
    model_path = os.path.join(os.path.dirname(__file__), 'model_data', 'model.joblib')
    if os.path.exists(model_path):
        model = joblib.load(model_path)
        print(f"Model loaded from {model_path}")
    else:
        print(f"Warning: Model not found at {model_path}. Make sure to train the model first.")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ML Auto Deployment API. Send a POST request to /predict to get a prediction."}

@app.get("/health")
def health_check():
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded. The API is not ready.")
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: IrisFeatures):
    if model is None:
        raise HTTPException(status_code=503, detail="Model is not loaded.")
    
    # Prepare the features as a DataFrame to match the training data
    input_data = pd.DataFrame([{
        "sepal length (cm)": features.sepal_length,
        "sepal width (cm)": features.sepal_width,
        "petal length (cm)": features.petal_length,
        "petal width (cm)": features.petal_width
    }])
    
    # Make prediction
    try:
        prediction_int = int(model.predict(input_data)[0])
        species_name = SPECIES_MAP.get(prediction_int, "unknown")
        return {"prediction": prediction_int, "species": species_name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
