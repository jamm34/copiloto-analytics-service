import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier

from app.core.database import SessionLocal
from app.services.customer_analytics_service import (
    CustomerAnalyticsService
)

from app.services.rules.business_rules import (
    BusinessRules
)

db = SessionLocal()

analytics = CustomerAnalyticsService()

dataset = []

# ejemplo MVP
for customer_id in range(1, 7001):

    try:

        data = analytics.analyze_customer(
            db,
            customer_id
        )

        churn = (
            BusinessRules
            .generate_churn_label(
                data[
                    "days_since_last_purchase"
                ]
            )
        ) 


        dataset.append({

            "total_orders":
                data["total_orders"],

            "total_spent":
                data["total_spent"],

            "avg_ticket":
                data["avg_ticket"],

            "days_since_last_purchase":
                data["days_since_last_purchase"] or 999,

            "score":
                data["score"],

            "churn":
                churn
        })

    except:
        continue


df = pd.DataFrame(dataset)

X = df[[
    "total_orders",
    "total_spent",
    "avg_ticket",
    "days_since_last_purchase",
    "score"
]]

y = df["churn"]

model = RandomForestClassifier()

model.fit(X, y)

joblib.dump(
    model,
    "app/models/churn_model.pkl"
)

print("MODEL TRAINED")