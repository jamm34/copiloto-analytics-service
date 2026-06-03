from pydantic import BaseModel
from typing import List, Optional


class CustomerResponse(
    BaseModel
):

    id: int

    name: str


class MetricsResponse(
    BaseModel
):

    total_orders: int

    total_spent: float

    avg_ticket: float

    days_since_last_purchase: Optional[int]

    purchase_frequency_days: Optional[float]

    customer_lifetime_value: float


class CommercialProfileResponse(
    BaseModel
):

    favorite_product: Optional[str]

    cross_sell_product: Optional[str]

    favorite_category: Optional[str]


class NextActionResponse(
    BaseModel
):

    action: str

    priority: str


class FullAnalysisResponse(
    BaseModel
):

    customer: CustomerResponse

    metrics: MetricsResponse

    commercial_profile: CommercialProfileResponse

    score: float

    segment: str

    risk: str

    purchase_probability: float

    churn_probability: float

    recommended_products: List[str]

    next_action: NextActionResponse

    explanation: str