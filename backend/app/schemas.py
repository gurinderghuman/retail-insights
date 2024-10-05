from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# Product schemas
class ProductBase(BaseModel):
    name: str
    category: str
    price: float = Field(..., gt=0)
    rating: float = Field(..., ge=0, le=5)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    category: Optional[str] = None
    price: Optional[float] = Field(None, gt=0)
    rating: Optional[float] = Field(None, ge=0, le=5)

class Product(ProductBase):
    id: int

    class Config:
        from_attributes = True

class ProductRecommendation(ProductBase):
    recommendation_reason: str

class PersonalizedRecommendations(BaseModel):
    user_id: int
    recommendations: List[ProductRecommendation]

# Brochure schemas
class BrochureBase(BaseModel):
    title: str
    views: int = Field(..., ge=0)
    unique_visitors: int = Field(..., ge=0)
    average_time_spent: float = Field(..., ge=0)
    click_through_rate: float = Field(..., ge=0, le=1)
    date: datetime

class BrochureCreate(BrochureBase):
    pass

class Brochure(BrochureBase):
    id: int

    class Config:
        from_attributes = True

# Campaign schemas
class CampaignBase(BaseModel):
    name: str
    start_date: datetime
    end_date: datetime
    budget: float = Field(..., gt=0)
    spend: float = Field(..., ge=0)
    impressions: int = Field(..., ge=0)
    clicks: int = Field(..., ge=0)
    conversions: int = Field(..., ge=0)
    revenue: float = Field(..., ge=0)

class CampaignCreate(CampaignBase):
    pass

class Campaign(CampaignBase):
    id: int

    class Config:
        from_attributes = True

class CampaignPerformance(CampaignBase):
    id: int
    ctr: float
    conversion_rate: float
    roas: float

# Store schemas
class StoreBase(BaseModel):
    name: str
    region: str
    total_sales: float = Field(..., ge=0)
    customer_density: int = Field(..., ge=0)
    latitude: float
    longitude: float

class StoreCreate(StoreBase):
    pass

class Store(StoreBase):
    id: int

    class Config:
        from_attributes = True

# Competitor schemas
class CompetitorBase(BaseModel):
    name: str
    market_share: float = Field(..., ge=0, le=100)
    customer_satisfaction: float = Field(..., ge=0, le=5)
    price_competitiveness: float = Field(..., gt=0)
    product_range: int = Field(..., ge=0)

class CompetitorCreate(CompetitorBase):
    pass

class Competitor(CompetitorBase):
    id: int

    class Config:
        from_attributes = True