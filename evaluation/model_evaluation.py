import os
import time
import numpy as np
import pandas as pd
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix, accuracy_score
import joblib  # Updated import for joblib

# Setup logging
logging.basicConfig(filename='model_evaluation.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load models
def load_model_safely(model_path):
    try:
        logger.info(f"Loading model from {model_path}...")
        return joblib.load(model_path)
    except Exception as e:
        logger.error(f"Error loading model {model_path}: {e}")
        return None

ensemble_transaction_model = load_model_safely('C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_transaction_model.joblib')
ensemble_link_model = load_model_safely('C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_link_model.joblib')

if not ensemble_transaction_model or not ensemble_link_model:
    raise RuntimeError("One or both models failed to load. Please check the log for details.")

# Load and preprocess data
logger.info("Loading data...")
transaction_data = pd.read_csv("C:/Users/Admin/Desktop/lekunutuai-extension/data/main_transaction_data.csv")
link_data = pd.read_csv("C:/Users/Admin/Desktop/lekunutuai-extension/data/main_link_data.csv")
logger.info("Data loaded")

# Separate features and labels
X_transaction = transaction_data.drop(columns=['Class'])
y_transaction = transaction_data['Class']
X_link = link_data.drop(columns=['URL_Type_obf_Type'])
y_link = link_data['URL_Type_obf_Type']

# Handle missing values
X_transaction.replace([np.inf, -np.inf], np.nan, inplace=True)
X_transaction.fillna(X_transaction.mean(), inplace=True)
X_link.replace([np.inf, -np.inf], np.nan, inplace=True)
X_link.fillna(X_link.mean(), inplace=True)

# Encode categorical labels
label_encoder_link = LabelEncoder()
y_link = label_encoder_link.fit_transform(y_link)

# Split data into training and test sets
X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(X_transaction, y_transaction, test_size=0.3, random_state=42, stratify=y_transaction)
X_train_link, X_test_link, y_train_link, y_test_link = train_test_split(X_link, y_link, test_size=0.3, random_state=42, stratify=y_link)

# Standardize the features
scaler_trans = StandardScaler()
X_train_trans = scaler_trans.fit_transform(X_train_trans)
X_test_trans = scaler_trans.transform(X_test_trans)
scaler_link = StandardScaler()
X_train_link = scaler_link.fit_transform(X_train_link)
X_test_link = scaler_link.transform(X_test_link)

# Evaluate models
def evaluate_model(model, X_test, y_test, model_name):
    try:
        logger.info(f"Evaluating {model_name}...")
        start_time = time.time()
        predictions = model.predict(X_test)
        end_time = time.time()
        prediction_time = end_time - start_time
        
        # Handle different target types
        if len(np.unique(y_test)) > 2:
            report = classification_report(y_test, predictions, target_names=label_encoder_link.classes_)
            auc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovo')
        else:
            report = classification_report(y_test, predictions, target_names=['Non-Fraud', 'Fraud'])
            auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
        
        matrix = confusion_matrix(y_test, predictions)
        accuracy = accuracy_score(y_test, predictions)

        logger.info(f"{model_name} Classification Report:\n{report}")
        logger.info(f"{model_name} ROC AUC Score: {auc}")
        logger.info(f"{model_name} Confusion Matrix:\n{matrix}")
        logger.info(f"{model_name} Accuracy: {accuracy}")
        logger.info(f"{model_name} Prediction Time: {prediction_time} seconds")

    except Exception as e:
        logger.error(f"Error during evaluation of {model_name}: {e}")

# Load and evaluate ensemble models
logger.info("Evaluating ensemble models...")

evaluate_model(ensemble_transaction_model, X_test_trans, y_test_trans, 'Ensemble Transaction Model')
evaluate_model(ensemble_link_model, X_test_link, y_test_link, 'Ensemble Link Model')

logger.info("Model evaluation complete.")
