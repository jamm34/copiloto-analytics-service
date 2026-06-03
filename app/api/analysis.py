from fastapi import APIRouter
from sqlalchemy.orm import Session

from app.core.database import get_db

from fastapi import Depends

from app.schemas.analysis import (
    FullAnalysisRequest
)

from app.services.customer_analytics_service import (
    CustomerAnalyticsService
)

from app.schemas.analysis_response import (
    FullAnalysisResponse
)

router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)

analytics_service = (
    CustomerAnalyticsService()
)


@router.post(
    "/customer/full",
    response_model=
        FullAnalysisResponse
)

def analyze_customer_full(
    request: FullAnalysisRequest,
    db: Session = Depends(
        get_db
    )
):

    result = (
        analytics_service
        .analyze_customer(
            db,
            request.customer_id
        )
    )

    return result