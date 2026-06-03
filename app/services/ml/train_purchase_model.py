import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

from app.core.database import SessionLocal
from app.services.customer_analytics_service import (
    CustomerAnalyticsService
)

db = SessionLocal()

analytics = CustomerAnalyticsService()

dataset = []

for customer_id in range(1,7001):

    try:

        data = analytics.analyze_customer(
            db,
            customer_id
        )

        purchase_label = 0

        if (
            data["days_since_last_purchase"]
            and
            data["purchase_frequency_days"]
        ):

            if (
                data["days_since_last_purchase"]
                <=
                data["purchase_frequency_days"]
            ):
                purchase_label = 1

        dataset.append({

            "total_orders":
                data["total_orders"],

            "total_spent":
                data["total_spent"],

            "avg_ticket":
                data["avg_ticket"],

            "days_since_last_purchase":
                data["days_since_last_purchase"] or 999,

            "purchase_frequency_days":
                data["purchase_frequency_days"] or 999,

            "score":
                data["score"],

            "purchase_label":
                purchase_label
        })

    except:
        continue


df = pd.DataFrame(dataset)

X = df[[

    "total_orders",

    "total_spent",

    "avg_ticket",

    "days_since_last_purchase",

    "purchase_frequency_days",

    "score"
]]

y = df["purchase_label"]

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X,y)

joblib.dump(
    model,
    "app/models/purchase_model.pkl"
)

print("PURCHASE MODEL TRAINED")