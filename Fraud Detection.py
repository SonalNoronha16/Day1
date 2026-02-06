# Fraud Detection Model Training

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import os

# Load dataset (Excel file)
df = pd.read_excel(r"C:\Users\sonal\Downloads\fraud_transactions_dataset.xlsx")

# Encode categorical columns
le_location = LabelEncoder()
le_device = LabelEncoder()

df['location'] = le_location.fit_transform(df['location'])
df['device'] = le_device.fit_transform(df['device'])

# Features and target
X = df[['amount', 'location', 'previous_transactions', 'device']]
y = df['is_fraud']

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model accuracy
pred = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, pred))

# Create folder if not exists
os.makedirs("models", exist_ok=True)

# Save model and preprocessing tools
pickle.dump(model, open("models/fraud_model.pkl", "wb"))
pickle.dump(scaler, open("models/scaler.pkl", "wb"))
pickle.dump(le_location, open("models/location_encoder.pkl", "wb"))
pickle.dump(le_device, open("models/device_encoder.pkl", "wb"))

print("✅ Model and tools saved successfully in 'models' folder.")


