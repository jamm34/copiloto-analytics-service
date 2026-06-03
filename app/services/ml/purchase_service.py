import joblib
import pandas as pd


class PurchaseService:

    def __init__(self):

        self.model = joblib.load(
            "app/models/purchase_model.pkl"
        )

    def predict_purchase(
        self,
        analytics_data
    ):

        X = pd.DataFrame([{

            "total_orders":
                analytics_data["total_orders"],

            "total_spent":
                analytics_data["total_spent"],

            "avg_ticket":
                analytics_data["avg_ticket"],

            "days_since_last_purchase":
                analytics_data[
                    "days_since_last_purchase"
                ] or 999,

            "purchase_frequency_days":
                analytics_data[
                    "purchase_frequency_days"
                ] or 999,

            "score":
                analytics_data["score"]
        }])

        probability = (
            self.model
            .predict_proba(X)[0][1]
        )

        window = "LOW"

        if probability > 0.70:
            window = "30_DAYS"

        elif probability > 0.40:
            window = "60_DAYS"

        return {

            "purchase_probability":
                round(
                    float(probability),
                    4
                ),

            "purchase_window":
                window
        }