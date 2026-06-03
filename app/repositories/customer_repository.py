from sqlalchemy.orm import Session

from app.models.customer import Customer
from app.models.order import Order

from app.models.order_item import OrderItem
from app.models.product import Product
from app.models.category import Category

from sqlalchemy import func

class CustomerRepository:

    def get_customer(
        self,
        db: Session,
        customer_id: int
    ):
        return (
            db.query(Customer)
            .filter(Customer.id == customer_id)
            .first()
        )

    def get_orders(
        self,
        db: Session,
        customer_id: int
    ):
        return (
            db.query(Order)
            .filter(Order.customerId == customer_id)
            .all()
        )
    

    def get_favorite_product(
        self,
        db: Session,
        customer_id: int
    ):

        result = (
            db.query(
                Product.name,
                func.sum(OrderItem.quantity).label("total_quantity")
            )
            .join(
                OrderItem,
                Product.id == OrderItem.productId
            )
            .join(
                Order,
                Order.id == OrderItem.orderId
            )
            .filter(
                Order.customerId == customer_id
            )
            .group_by(
                Product.id,
                Product.name
            )
            .order_by(
                func.sum(OrderItem.quantity).desc()
            )
            .first()
        )

        return result
    
    def get_customer_orders_desc(
        self,
        db,
        customer_id: int
    ):
        return (
            db.query(Order)
            .filter(
                Order.customerId == customer_id
            )
            .order_by(
                Order.orderDate.desc()
            )
            .all()
        )
    
    def get_favorite_category(
        self,
        db,
        customer_id: int
    ):

        result = (
            db.query(
                Category.name,
                func.sum(OrderItem.quantity).label(
                    "total_quantity"
                )
            )
            .join(
                Product,
                Product.category_id == Category.id
            )
            .join(
                OrderItem,
                OrderItem.productId == Product.id
            )
            .join(
                Order,
                Order.id == OrderItem.orderId
            )
            .filter(
                Order.customerId == customer_id
            )
            .group_by(
                Category.id,
                Category.name
            )
            .order_by(
                func.sum(OrderItem.quantity).desc()
            )
            .first()
        )
    
        return result
    
    def get_cross_sell_product(
        self,
        db,
        customer_id: int
    ):

        result = (
            db.query(
                Product.name,
                func.sum(
                    OrderItem.quantity
                ).label("qty")
            )
            .join(
                OrderItem,
                Product.id == OrderItem.productId
            )
            .join(
                Order,
                Order.id == OrderItem.orderId
            )
            .filter(
                Order.customerId == customer_id
            )
            .group_by(
                Product.id,
                Product.name
            )
            .order_by(
                func.sum(
                    OrderItem.quantity
                ).desc()
            )
            .offset(1)
            .first()
        )

        return result
    
    def get_cross_sell_product(
        self,
        db,
        customer_id: int
    ):

        result = (
            db.query(
                Product.name,
                func.sum(
                    OrderItem.quantity
                ).label("qty")
            )
            .join(
                OrderItem,
                Product.id == OrderItem.productId
            )
            .join(
                Order,
                Order.id == OrderItem.orderId
            )
            .filter(
                Order.customerId == customer_id
            )
            .group_by(
                Product.id,
                Product.name
            )
            .order_by(
                func.sum(
                    OrderItem.quantity
                ).desc()
            )
            .offset(1)
            .first()
        )

        return result