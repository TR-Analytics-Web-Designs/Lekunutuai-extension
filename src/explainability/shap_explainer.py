# /explainability/shap_explainer.py

import shap
import pandas as pd

class SHAPExplainer:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.explainer = shap.TreeExplainer(self.model)

    def explain_instance(self, instance):
        shap_values = self.explainer.shap_values(instance)
        return shap_values

# Usage
from sklearn.ensemble import RandomForestClassifier

link_data = pd.read_csv("data/main_link_data.csv")
transaction_data = pd.read_csv("data/main_transaction_data.csv")

X_link = link_data.drop(columns=["fraud_label"])
y_link = link_data["fraud_label"]

X_transaction = transaction_data.drop(columns=["fraud_label"])
y_transaction = transaction_data["fraud_label"]

model_link = RandomForestClassifier().fit(X_link, y_link)
model_transaction = RandomForestClassifier().fit(X_transaction, y_transaction)

explainer_link = SHAPExplainer(model_link, X_link)
shap_values_link = explainer_link.explain_instance(X_link.iloc[0])

explainer_transaction = SHAPExplainer(model_transaction, X_transaction)
shap_values_transaction = explainer_transaction.explain_instance(X_transaction.iloc[0])
