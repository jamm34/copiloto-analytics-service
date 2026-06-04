from app.services.recommendation_service import RecommendationService
from app.repositories.customer_repository import CustomerRepository
from app.services.scoring_service import ScoringService
from datetime import datetime

from app.services.category_recommendation_service import (
    CategoryRecommendationService
)
from app.services.rules.business_rules import (
    BusinessRules
)
from app.services.action_service import (
    ActionService
)

from app.services.explainability_service import (
    ExplainabilityService
)

from app.services.opportunity_service import (
    OpportunityService
)

from app.services.ml.churn_service import ChurnService
from app.services.ml.purchase_service import PurchaseService


class CustomerAnalyticsService:    

    def __init__(self):
        self.scoring_service = ScoringService()
        self.recommendation_service = RecommendationService()
        self.repository = CustomerRepository()
        self.category_recommendation_service = (CategoryRecommendationService())
        self.churn_service = ChurnService()
        self.purchase_service = PurchaseService()
        self.action_service = (ActionService())
        self.explainability_service = (ExplainabilityService())
        self.opportunity_service = (OpportunityService())

    def analyze_customer(
        self,
        db,
        customer_id: int
    ):

        customer = self.repository.get_customer(
            db,
            customer_id
        )

        orders = self.repository.get_orders(
            db,
            customer_id
        )

        orders_desc = (
            self.repository
            .get_customer_orders_desc(
                db,
                customer_id
            )
        )

        favorite_product = (
            self.repository
            .get_favorite_product(
                db,
                customer_id
            )
        )

        cross_sell_product = (
            self.repository
            .get_cross_sell_product(
                db,
                customer_id
            )
        )

        favorite_category = (
            self.repository
            .get_favorite_category(
                db,
                customer_id
            )
        )

        total_orders = len(orders)

        total_spent = sum(
            float(order.totalAmount)
            for order in orders
        )

        favorite_category_name = None

        if favorite_category:
            favorite_category_name = (
                favorite_category.name
            )

        category_recommendation = (
            self.category_recommendation_service
            .get_category_recommendation(
                favorite_category_name
            )
        )

        
        avg_ticket = 0

        if total_orders > 0:
            avg_ticket = (
                total_spent / total_orders
            )

        last_purchase_date = None

        if orders:
            last_purchase_date = max(
                order.orderDate
                for order in orders
            )

        days_since_last_purchase = None

        if last_purchase_date:
            days_since_last_purchase = (
                datetime.now() -
                last_purchase_date
            ).days

        score_data = self.scoring_service.calculate_score(
            days_since_last_purchase=
                days_since_last_purchase,
            total_orders=
                total_orders,
            total_spent=
                total_spent
        )

        recommendation_data = (
            self.recommendation_service
            .get_recommendation(
                score_data["segment"]
            )
        )

        purchase_frequency_days = None
        if len(orders) > 1:

            dates = sorted(
                [
                    order.orderDate
                    for order in orders
                ]
            )

            intervals = []

            for i in range(1, len(dates)):

                diff = (
                    dates[i] -
                    dates[i - 1]
                ).days

                intervals.append(diff)

            purchase_frequency_days = (
                sum(intervals) /
                len(intervals)
            )
        
        customer_lifetime_value = total_spent

        customer_status = (
            BusinessRules
            .get_customer_status(
                days_since_last_purchase
            )
        )
        
        favorite_product_name = None

        if favorite_product:
            favorite_product_name = favorite_product.name
        
        purchase_trend = "UNKNOWN"

        if len(orders_desc) >= 6:

            recent = orders_desc[:3]

            previous = orders_desc[3:6]

            recent_avg = (
                sum(
                    float(o.totalAmount)
                    for o in recent
                ) / len(recent)
            )

            previous_avg = (
                sum(
                    float(o.totalAmount)
                    for o in previous
                ) / len(previous)
            )

            if recent_avg > previous_avg * 1.10:
                purchase_trend = "GROWING"

            elif recent_avg < previous_avg * 0.90:
                purchase_trend = "DECLINING"

            else:
                purchase_trend = "STABLE"

        cross_sell_name = None

        if cross_sell_product:
            cross_sell_name = (
                cross_sell_product.name
            )

        analytics_data = {

            "total_orders": total_orders,

            "total_spent": total_spent,

            "avg_ticket": avg_ticket,

            "days_since_last_purchase":
                days_since_last_purchase,

            "score":
                score_data["score"]
        }

        churn_data = (
            self.churn_service
            .predict_churn(
                analytics_data
            )
        )

        purchase_data = (
            self.purchase_service
            .predict_purchase({

                "total_orders":
                    total_orders,

                "total_spent":
                    total_spent,

                "avg_ticket":
                    avg_ticket,

                "days_since_last_purchase":
                    days_since_last_purchase,

                "purchase_frequency_days":
                    purchase_frequency_days,

                "score":
                    score_data["score"]
            })
        )

        action_data = (
            self.action_service
            .get_action(

                score_data["segment"],

                churn_data[
                    "churn_probability"
                ],

                purchase_data[
                    "purchase_probability"
                ]
            )
        )

        explanation = (
            self.explainability_service
            .explain_action(

                score_data["segment"],

                churn_data[
                    "churn_probability"
                ],

                purchase_data[
                    "purchase_probability"
                ],

                favorite_category_name
            )
        )

        opportunity_score = (
            self.opportunity_service
            .calculate_score(

                score_data["segment"],

                purchase_data[
                    "purchase_probability"
                ],

                churn_data[
                    "churn_probability"
                ],

                score_data["score"]
            )
        )

        return {

            "customer": {

                "id":
                    customer.id,

                "name":
                    customer.fullName
            },

            "metrics": {

                "total_orders":
                    total_orders,

                "total_spent":
                    round(total_spent, 2),

                "avg_ticket":
                    round(avg_ticket, 2),

                "days_since_last_purchase":
                    days_since_last_purchase,

                "purchase_frequency_days":
                    purchase_frequency_days,

                "customer_lifetime_value":
                    round(customer_lifetime_value, 2)
            },

            "commercial_profile": {

                "favorite_product":
                    favorite_product_name,

                "cross_sell_product":
                    cross_sell_name,

                "favorite_category":
                    favorite_category_name
            },

            "score":
                score_data["score"],

            "segment":
                score_data["segment"],

            "risk":
                churn_data[
                    "churn_risk"
                ],

            "purchase_probability":
                purchase_data[
                    "purchase_probability"
                ],

            "churn_probability":
                churn_data[
                    "churn_probability"
                ],

            "recommended_products":[

                cross_sell_name
            ],

            "next_action": {

                "action":
                    action_data[
                        "recommended_action"
                    ],

                "priority":
                    action_data[
                        "sales_priority"
                    ]
            },

            "explanation":
                explanation
        }