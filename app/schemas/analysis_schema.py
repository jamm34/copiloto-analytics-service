from pydantic import BaseModel

class CustomerAnalysisRequest(BaseModel):
    customerId: int


class CustomerAnalysisResponse(BaseModel):
    customer_id: int
    customer_name: str

    total_orders: int

    total_spent: float

    avg_ticket: float

    days_since_last_purchase: int

    purchase_frequency_days: float

    favorite_category: str | None

    favorite_product: str | None

    lifetime_value: float