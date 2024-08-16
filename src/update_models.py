import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Dummy data for example
X_train_link = np.random.rand(100, 20)
y_train_link = np.random.randint(2, size=100)
X_train_trans = np.random.rand(100, 30)
y_train_trans = np.random.randint(2, size=100)

# Train models
scaler_link = StandardScaler()
X_train_link_scaled = scaler_link.fit_transform(X_train_link)
link_model = RandomForestClassifier().fit(X_train_link_scaled, y_train_link)

scaler_trans = StandardScaler()
X_train_trans_scaled = scaler_trans.fit_transform(X_train_trans)
transaction_model = RandomForestClassifier().fit(X_train_trans_scaled, y_train_trans)

# Save models and scalers
joblib.dump(scaler_link, 'C:/Users/Admin/Desktop/lekunutuai-extension/data/scaler_link.pkl')
joblib.dump(scaler_trans, 'C:/Users/Admin/Desktop/lekunutuai-extension/data/scaler_trans.pkl')
joblib.dump(link_model, 'C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_link_model.joblib')
joblib.dump(transaction_model, 'C:/Users/Admin/Desktop/lekunutuai-extension/models/fastapi_ensemble_transaction_model.joblib')

