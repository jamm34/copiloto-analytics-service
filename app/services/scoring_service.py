from app.services.rules.business_rules import (
    BusinessRules
)

class ScoringService:

    def recency_score(
        self,
        days_since_last_purchase: int
    ):

        if days_since_last_purchase is None:
            return 0

        if days_since_last_purchase <= 30:
            return 100
        if days_since_last_purchase <= 30:
            return 100

        if days_since_last_purchase <= 60:
            return 80

        if days_since_last_purchase <= 90:
            return 60

        if days_since_last_purchase <= 180:
            return 30

        return 10

    def frequency_score(
        self,
        total_orders: int
    ):
        if total_orders == 0:
            return {
                "score": 0,
                "segment": "NEW_LEAD",
                "recency_score": 0,
                "frequency_score": 0,
                "monetary_score": 0
            }
        if total_orders >= 20:
            return 100

        if total_orders >= 10:
            return 80

        if total_orders >= 5:
            return 60

        return 20

    def monetary_score(
        self,
        total_spent: float
    ):

        if total_spent >= 10000:
            return 100

        if total_spent >= 5000:
            return 80

        if total_spent >= 2000:
            return 60

        return 20

    def get_segment(
        self,
        score: float
    ):

        if score >= 90:
            return "VIP"

        if score >= 75:
            return "LOYAL"

        if score >= 60:
            return "ACTIVE"

        if score >= 40:
            return "OCCASIONAL"

        return "AT_RISK"

    def calculate_score(
        self,
        days_since_last_purchase: int,
        total_orders: int,
        total_spent: float
    ):
        if total_orders == 0:
            return {
                "score": 0,
                "segment": "NEW_LEAD",
                "recency_score": 0,
                "frequency_score": 0,
                "monetary_score": 0
            }

        recency = self.recency_score(
            days_since_last_purchase
        )

        frequency = self.frequency_score(
            total_orders
        )

        monetary = self.monetary_score(
            total_spent
        )

        final_score = (
            recency +
            frequency +
            monetary
        ) / 3

        segment = self.get_segment(
            final_score
        )

        segment = self.get_segment(
            final_score
        )

        segment = (
            BusinessRules
            .apply_segment_override(
                segment,
                days_since_last_purchase
            )
        )


        return {
            "score": round(final_score, 2),
            "segment": segment,
            "recency_score": recency,
            "frequency_score": frequency,
            "monetary_score": monetary
        }