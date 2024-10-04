from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, DateTime
from app.database import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category = Column(String)
    price = Column(Float)
    rating = Column(Float)

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, rating={self.rating})>"

class Brochure(Base):
    __tablename__ = 'brochures'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    views = Column(Integer)
    unique_visitors = Column(Integer)
    average_time_spent = Column(Float)
    click_through_rate = Column(Float)
    date = Column(DateTime)

    def __repr__(self):
        return f"<Brochure(id={self.id}, title='{self.title}', date={self.date})>"

class Campaign(Base):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    budget = Column(Float)
    spend = Column(Float)
    impressions = Column(Integer)
    clicks = Column(Integer)
    conversions = Column(Integer)
    revenue = Column(Float)

    def __repr__(self):
        return f"<Campaign(id={self.id}, name='{self.name}', start_date={self.start_date}, end_date={self.end_date})>"

class Store(Base):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    region = Column(String)
    total_sales = Column(Float)
    customer_density = Column(Integer)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
        return f"<Store(id={self.id}, name='{self.name}', region='{self.region}')>"

class Competitor(Base):
    __tablename__ = 'competitors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    market_share = Column(Float)
    customer_satisfaction = Column(Float)
    price_competitiveness = Column(Float)
    product_range = Column(Integer)

    def __repr__(self):
        return f"<Competitor(id={self.id}, name='{self.name}', market_share={self.market_share})>"