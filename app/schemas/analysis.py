from pydantic import BaseModel


class FullAnalysisRequest(
    BaseModel
):

    customer_id: int