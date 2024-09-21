from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    category: str
    price: float = Field(..., gt=0)
    rating: float = Field(..., ge=0, le=5)

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = Field(None, gt=0)
    rating: float | None = Field(None, ge=0, le=5)

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductRecommendation(ProductBase):
    recommendation_reason: str

class PersonalizedRecommendations(BaseModel):
    user_id: int
    recommendations: List[ProductRecommendation]

class CampaignPerformance(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime
    budget: float = Field(..., gt=0)
    spend: float = Field(..., ge=0)
    impressions: int = Field(..., ge=0)
    clicks: int = Field(..., ge=0)
    conversions: int = Field(..., ge=0)
    revenue: float = Field(..., ge=0)
    ctr: float
    conversion_rate: float
    roas: float