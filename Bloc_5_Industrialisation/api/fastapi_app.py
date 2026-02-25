from fastapi import FastAPI
import joblib
import pandas as pd
import os

from .schemas import PredictionInput, PredictionOutput


app = FastAPI(
    title="Getaround Pricing Prediction API"
)


current_dir = os.path.dirname(__file__)
model_path = os.path.join(current_dir, "model", "model.joblib")

model = joblib.load(model_path)


@app.post("/predict", response_model=PredictionOutput)
def predict(data: PredictionInput):

    df = pd.DataFrame(
        data.input,
        columns=[
            "mileage",
            "engine_power",
            "fuel",
            "paint_color",
            "car_type",
            "private_parking_available",
            "has_gps",
            "has_air_conditioning",
            "automatic_car",
            "has_getaround_connect",
            "has_speed_regulator",
            "winter_tires"
        ]
    )

    preds = model.predict(df)

    return {
        "prediction": preds.tolist()
    }