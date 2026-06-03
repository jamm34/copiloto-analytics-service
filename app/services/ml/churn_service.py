import joblib
import numpy as np


class ChurnService:

    def __init__(self):

        self.model = joblib.load(
            "app/models/churn_model.pkl"
        )

    def predict_churn(
        self,
        analytics_data
    ):

        X = np.array([[
            analytics_data["total_orders"],

            analytics_data["total_spent"],

            analytics_data["avg_ticket"],

            analytics_data[
                "days_since_last_purchase"
            ] or 999,

            analytics_data["score"]
        ]])

        probability = (
            self.model
            .predict_proba(X)[0][1]
        )
        print(probability)

        risk = "LOW"

        if probability > 0.70:
            risk = "HIGH"

        elif probability > 0.40:
            risk = "MEDIUM"

        return {

            "churn_probability":
                round(float(probability),4),

            "churn_risk":
                risk
        }