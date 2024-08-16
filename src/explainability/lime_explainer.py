# /explainability/lime_explainer.py

import lime
import lime.lime_tabular
import pandas as pd

class LIMEExplainer:
    def __init__(self, model, data):
        self.model = model
        self.data = data
        self.explainer = lime.lime_tabular.LimeTabularExplainer(self.data.values, mode='classification')

    def explain_instance(self, instance):
        exp = self.explainer.explain_instance(instance.values, self.model.predict_proba)
        return exp.as_list()

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

explainer_link = LIMEExplainer(model_link, X_link)
explanation_link = explainer_link.explain_instance(X_link.iloc[0])

explainer_transaction = LIMEExplainer(model_transaction, X_transaction)
explanation_transaction = explainer_transaction.explain_instance(X_transaction.iloc[0])
