import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Define test data
VALID_URL_FEATURES = {f"url_feature{i}": float(i) for i in range(1, 80)}  # Ensure 79 features
VALID_TRANSACTION_FEATURES = {f"feature{i}": float(i) for i in range(1, 31)}  # Ensure 30 features

INVALID_URL_FEATURES = {f"url_feature{i}": 'invalid' for i in range(1, 80)}
INVALID_TRANSACTION_FEATURES = {f"feature{i}": 'invalid' for i in range(1, 31)}

MISSING_URL_FEATURES = {f"url_feature{i}": float(i) for i in range(1, 50)}  # Missing features
MISSING_TRANSACTION_FEATURES = {f"feature{i}": float(i) for i in range(1, 28)}  # Less features

def test_predict_valid():
    response = client.post("/predict", json={
        "url_features": VALID_URL_FEATURES,
        "transaction_features": VALID_TRANSACTION_FEATURES
    })
    print("test_predict_valid:", response.json())
    assert response.status_code == 200

def test_predict_invalid_url_features():
    response = client.post("/predict", json={
        "url_features": INVALID_URL_FEATURES,
        "transaction_features": VALID_TRANSACTION_FEATURES
    })
    print("test_predict_invalid_url_features:", response.json())
    assert response.status_code == 400

def test_predict_invalid_transaction_features():
    response = client.post("/predict", json={
        "url_features": VALID_URL_FEATURES,
        "transaction_features": INVALID_TRANSACTION_FEATURES
    })
    print("test_predict_invalid_transaction_features:", response.json())
    assert response.status_code == 400

def test_predict_missing_data():
    response = client.post("/predict", json={
        "url_features": MISSING_URL_FEATURES,
        "transaction_features": VALID_TRANSACTION_FEATURES
    })
    print("test_predict_missing_data:", response.json())
    assert response.status_code == 400

def test_predict_missing_transaction_features():
    response = client.post("/predict", json={
        "url_features": VALID_URL_FEATURES,
        "transaction_features": MISSING_TRANSACTION_FEATURES
    })
    print("test_predict_missing_transaction_features:", response.json())
    assert response.status_code == 400
