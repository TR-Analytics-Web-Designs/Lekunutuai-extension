# /real_time_processing/real_time_processing.py

import time
import random
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

class RealTimeProcessing:
    def __init__(self, model, text_column):
        self.model = model
        self.text_column = text_column
        self.tfidf = TfidfVectorizer(max_features=100)

    def process_stream(self, data_stream):
        for data in data_stream:
            text_data = data[self.text_column]
            text_features = self.tfidf.transform([text_data]).toarray()
            prediction = self.model.predict(text_features)
            print(f"Prediction for {text_data}: {prediction}")
            time.sleep(random.uniform(0.1, 0.5))

# Usage
link_data = pd.read_csv("data/main_link_data.csv")
transaction_data = pd.read_csv("data/main_transaction_data.csv")

X_link = link_data["link_text"]
y_link = link_data["fraud_label"]

X_transaction = transaction_data["transaction_description"]
y_transaction = transaction_data["fraud_label"]

model_link = RandomForestClassifier().fit(X_link, y_link)
model_transaction = RandomForestClassifier().fit(X_transaction, y_transaction)

real_time_processor_link = RealTimeProcessing(model_link, text_column="link_text")
real_time_processor_transaction = RealTimeProcessing(model_transaction, text_column="transaction_description")

# Simulating data streams
data_stream_link = [X_link.iloc[i] for i in range(10)]
data_stream_transaction = [X_transaction.iloc[i] for i in range(10)]

real_time_processor_link.process_stream(data_stream_link)
real_time_processor_transaction.process_stream(data_stream_transaction)
