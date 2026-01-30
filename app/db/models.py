from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Float

Base = declarative_base()


class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)
    payment_delay_days = Column(Integer)
    avg_weekly_usage_hours = Column(Float)
    tickets_raised = Column(Integer)
    days_since_last_login = Column(Integer)
