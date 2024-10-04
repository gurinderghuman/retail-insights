from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime, timedelta
import random

from .database import SessionLocal, engine
from . import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Welcome to the Retail Insights Platform API"}

@app.get("/api/brochure-analytics")
async def get_brochure_analytics():
    # Simulating data for the last 7 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    daily_data = []
    for i in range(7):
        date = start_date + timedelta(days=i)
        daily_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "views": random.randint(1000, 5000),
            "unique_visitors": random.randint(800, 3000),
            "average_time_spent": round(random.uniform(30, 180), 2),  # in seconds
            "click_through_rate": round(random.uniform(0.02, 0.15), 3)
        })
    
    top_products = [
        {"name": "Smartphone X", "views": random.randint(500, 2000)},
        {"name": "Laptop Pro", "views": random.randint(400, 1800)},
        {"name": "Wireless Earbuds", "views": random.randint(300, 1500)},
        {"name": "Smart TV 55\"", "views": random.randint(200, 1200)},
        {"name": "Coffee Maker Deluxe", "views": random.randint(100, 1000)}
    ]
    
    return {
        "total_views": sum(day["views"] for day in daily_data),
        "total_unique_visitors": sum(day["unique_visitors"] for day in daily_data),
        "average_time_spent": round(sum(day["average_time_spent"] for day in daily_data) / 7, 2),
        "average_click_through_rate": round(sum(day["click_through_rate"] for day in daily_data) / 7, 3),
        "daily_data": daily_data,
        "top_products": sorted(top_products, key=lambda x: x["views"], reverse=True)
    }

@app.get("/api/geospatial-analysis")
async def get_geospatial_analysis():
    # Simulating geospatial data for different regions
    regions = ["North", "South", "East", "West", "Central"]
    
    regional_data = []
    for region in regions:
        regional_data.append({
            "region": region,
            "total_sales": random.randint(100000, 1000000),
            "customer_density": random.randint(100, 1000),
            "store_count": random.randint(5, 50),
            "average_order_value": round(random.uniform(50, 200), 2),
            "top_selling_category": random.choice(["Electronics", "Clothing", "Home Goods", "Food", "Sports"])
        })
    
    store_locations = [
        {"id": i, "name": f"Store {i}", "lat": random.uniform(25, 50), "lon": random.uniform(-125, -65)}
        for i in range(1, 21)  # Generating 20 random store locations
    ]
    
    return {
        "regional_data": regional_data,
        "total_sales": sum(region["total_sales"] for region in regional_data),
        "total_stores": sum(region["store_count"] for region in regional_data),
        "average_customer_density": round(sum(region["customer_density"] for region in regional_data) / len(regions), 2),
        "store_locations": store_locations
    }

@app.get("/api/personalized-recommendations", response_model=schemas.PersonalizedRecommendations)
async def get_personalized_recommendations(user_id: int = Query(..., gt=0)):
    if random.random() < 0.1:  # Simulate user not found error (10% chance)
        raise HTTPException(status_code=404, detail="User not found")
    
    recommendations = []
    product_categories = ["Electronics", "Clothing", "Home Goods", "Sports", "Books", "Food"]
    for _ in range(5):  # Generating 5 recommendations
        recommendations.append(schemas.ProductRecommendation(
            product_name=f"Product {random.randint(1, 100)}",
            category=random.choice(product_categories),
            price=round(random.uniform(10, 500), 2),
            rating=round(random.uniform(3.5, 5), 1),
            recommendation_reason=random.choice([
                "Based on your purchase history",
                "Customers like you also bought",
                "Top seller in your area",
                "Matches your preferences"
            ])
        ))
    
    return schemas.PersonalizedRecommendations(user_id=user_id, recommendations=recommendations)

@app.get("/api/campaign-performance", response_model=schemas.CampaignPerformance)
async def get_campaign_performance(campaign_id: int = Query(..., gt=0)):
    # Simulating campaign performance data
    if random.random() < 0.1:  # Simulate campaign not found error (10% chance)
        raise HTTPException(status_code=404, detail="Campaign not found")
    
    start_date = datetime.now() - timedelta(days=random.randint(1, 30))
    end_date = start_date + timedelta(days=random.randint(7, 14))
    
    spend = round(random.uniform(1000, 40000), 2)
    impressions = random.randint(10000, 1000000)
    clicks = random.randint(1000, min(100000, impressions))
    conversions = random.randint(10, min(1000, clicks))
    revenue = round(random.uniform(1000, 100000), 2)
    
    return schemas.CampaignPerformance(
        id=campaign_id,
        name=f"Campaign {campaign_id}",
        start_date=start_date,
        end_date=end_date,
        budget=round(random.uniform(5000, 50000), 2),
        spend=spend,
        impressions=impressions,
        clicks=clicks,
        conversions=conversions,
        revenue=revenue,
        ctr=round(clicks / impressions * 100, 2),
        conversion_rate=round(conversions / clicks * 100, 2),
        roas=round(revenue / spend, 2)
    )

@app.get("/api/competitor-analysis")
async def get_competitor_analysis():
    # Simulating competitor analysis data
    competitors = ["CompetitorA", "CompetitorB", "CompetitorC", "CompetitorD"]
    metrics = ["Market Share", "Customer Satisfaction", "Price Competitiveness", "Product Range"]
    
    competitor_data = []
    for competitor in competitors:
        data = {
            "name": competitor,
            "market_share": round(random.uniform(5, 30), 2),
            "customer_satisfaction": round(random.uniform(3, 5), 1),
            "price_competitiveness": round(random.uniform(0.8, 1.2), 2),
            "product_range": random.randint(100, 10000)
        }
        competitor_data.append(data)
    
    market_trends = [
        {"trend": "Online Sales Growth", "value": f"{random.randint(5, 30)}% YoY"},
        {"trend": "Mobile Shopping Adoption", "value": f"{random.randint(40, 80)}%"},
        {"trend": "Sustainability Focus", "value": f"{random.randint(20, 60)}% of consumers prioritize"},
        {"trend": "Personalization Demand", "value": f"{random.randint(50, 90)}% expect personalized experiences"}
    ]
    
    return {
        "competitor_data": competitor_data,
        "market_trends": market_trends,
        "our_company": {
            "market_share": round(random.uniform(10, 40), 2),
            "customer_satisfaction": round(random.uniform(3.5, 5), 1),
            "price_competitiveness": 1.0,
            "product_range": random.randint(1000, 15000)
        }
    }

@app.get("/api/dashboard")
async def get_dashboard():
    # Aggregate data from other endpoints
    brochure_data = await get_brochure_analytics()
    geospatial_data = await get_geospatial_analysis()
    competitor_data = await get_competitor_analysis()
    
    # For personalized recommendations and campaign performance, we'll use sample data
    sample_recommendations = await get_personalized_recommendations(user_id=1)
    sample_campaign = await get_campaign_performance(campaign_id=1)
    
    return {
        "brochure_analytics": {
            "total_views": brochure_data["total_views"],
            "total_unique_visitors": brochure_data["total_unique_visitors"],
            "average_time_spent": brochure_data["average_time_spent"],
            "top_products": brochure_data["top_products"][:3]  # Top 3 products
        },
        "geospatial_overview": {
            "total_sales": geospatial_data["total_sales"],
            "total_stores": geospatial_data["total_stores"],
            "average_customer_density": geospatial_data["average_customer_density"]
        },
        "competitor_overview": {
            "our_market_share": competitor_data["our_company"]["market_share"],
            "top_competitor": max(competitor_data["competitor_data"], key=lambda x: x["market_share"]),
            "market_trends": competitor_data["market_trends"][:2]  # Top 2 market trends
        },
        "recent_recommendations": sample_recommendations.recommendations[:3],  # Top 3 recommendations
        "recent_campaign": {
            "name": sample_campaign.name,
            "impressions": sample_campaign.impressions,
            "clicks": sample_campaign.clicks,
            "conversions": sample_campaign.conversions,
            "revenue": sample_campaign.revenue
        }
    }

@app.post("/products/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)

@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.put("/products/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db, product_id, product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@app.delete("/products/{product_id}", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db, product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product