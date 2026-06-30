import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("transactions.csv")

# Features and target
X = data.drop("fraud", axis=1)
y = data["fraud"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model trained successfully!")