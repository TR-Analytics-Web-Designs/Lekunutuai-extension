from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib
import logging

app = FastAPI()

# Load models
ensemble_link_model = joblib.load('C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_link_model.joblib')
ensemble_transaction_model = joblib.load('C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_transaction_model.joblib')


# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define expected feature counts
EXPECTED_URL_FEATURES = 79
EXPECTED_TRANSACTION_FEATURES = 30

# Request models
class PredictRequest(BaseModel):
    url_features: dict
    transaction_features: dict

def validate_features(features: dict, expected_count: int, feature_type: str):
    if len(features) != expected_count:
        raise HTTPException(status_code=400, detail=f"Invalid number of {feature_type} features: expected {expected_count}, got {len(features)}")
    for key, value in features.items():
        try:
            float(value)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Invalid data: '{value}' for feature '{key}' is not a float")

@app.post("/predict")
async def predict(request: PredictRequest):
    try:
        # Validate and convert URL features
        validate_features(request.url_features, EXPECTED_URL_FEATURES, "URL")
        url_features = np.array(list(request.url_features.values())).astype(float).reshape(1, -1)

        # Validate and convert transaction features
        validate_features(request.transaction_features, EXPECTED_TRANSACTION_FEATURES, "transaction")
        transaction_features = np.array(list(request.transaction_features.values())).astype(float).reshape(1, -1)

        # Make predictions
        url_prediction = ensemble_link_model.predict(url_features)
        transaction_prediction = ensemble_transaction_model.predict(transaction_features)

        return {
            "url_prediction": int(url_prediction[0]),
            "transaction_prediction": int(transaction_prediction[0])
        }
    except HTTPException as he:
        logger.error(f"HTTPException: {he.detail}")
        raise he
    except Exception as e:
        logger.error(f"Error making predictions: {e}")
        raise HTTPException(status_code=500, detail="Prediction error")


