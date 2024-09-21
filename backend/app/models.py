from sqlalchemy import Column, Integer, String, Float, DateTime
from .database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String)
    price = Column(Float)
    rating = Column(Float)

class Brochure(Base):
    __tablename__ = "brochures"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    views = Column(Integer)
    unique_visitors = Column(Integer)
    average_time_spent = Column(Float)
    click_through_rate = Column(Float)
    date = Column(DateTime)

class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = Column(Float)
    spend = Column(Float)
    impressions = Column(Integer)
    clicks = Column(Integer)
    conversions = Column(Integer)
    revenue = Column(Float)

class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String)
    total_sales = Column(Float)
    customer_density = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)