import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

os.makedirs("models", exist_ok=True)

df = pd.read_csv("data/flood_dataset.csv")

X = df[["rainfall", "river_level", "population_density"]]
y = df["flood_risk"]

model = RandomForestClassifier(n_estimators=100)

model.fit(X, y)

joblib.dump(model, "models/flood_model.pkl")

print("Model Trained Successfully")