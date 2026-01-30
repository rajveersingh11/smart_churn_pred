# app/services/model_service.py

import joblib
import os

MODEL_PATH = "data/models/best_model.pkl"


class ModelService:

    def __init__(self):

        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError("Model not found")

        self.model = joblib.load(MODEL_PATH)

    def predict_probability(self, features: list):

        prob = self.model.predict_proba([features])[0][1]

        return round(float(prob), 4)
