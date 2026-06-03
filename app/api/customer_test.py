from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.core.dependencies import get_db

from app.models.customer import Customer

router = APIRouter()

@router.get("/customers-test")
def customers_test(
    db: Session = Depends(get_db)
):

    customers = (
        db.query(Customer)
        .limit(5)
        .all()
    )

    return [
        {
            "id": c.id,
            "name": c.fullName
        }
        for c in customers
    ]