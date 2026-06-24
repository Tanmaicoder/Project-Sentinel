import joblib
import pandas as pd

model = joblib.load("models/flood_model.pkl")

def predict_flood_risk(
        rainfall,
        river_level,
        population_density
):

    input_df = pd.DataFrame({
        "rainfall": [rainfall],
        "river_level": [river_level],
        "population_density": [population_density]
    })

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    return prediction, round(probability * 100, 2)