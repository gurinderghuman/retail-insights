from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from datetime import datetime, timedelta
import random

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Retail Insights Platform API"}

@app.get("/api/personalized-recommendations")
async def get_personalized_recommendations(user_id: int):
    # Simulating personalized recommendations for a user
    product_categories = ["Electronics", "Clothing", "Home Goods", "Sports", "Books", "Food"]
    recommendations = []
    
    for _ in range(5):  # Generating 5 recommendations
        recommendations.append({
            "product_name": f"Product {random.randint(1, 100)}",
            "category": random.choice(product_categories),
            "price": round(random.uniform(10, 500), 2),
            "rating": round(random.uniform(3.5, 5), 1),
            "recommendation_reason": random.choice([
                "Based on your purchase history",
                "Customers like you also bought",
                "Top seller in your area",
                "Matches your preferences"
            ])
        })
    
    return {
        "user_id": user_id,
        "recommendations": recommendations
    }

@app.get("/api/campaign-performance")
async def get_campaign_performance(campaign_id: int = None):
    # Simulating campaign performance data
    campaigns = []
    
    for i in range(1, 6):  # Generating data for 5 campaigns
        start_date = datetime.now() - timedelta(days=random.randint(1, 30))
        end_date = start_date + timedelta(days=random.randint(7, 14))
        
        campaign = {
            "id": i,
            "name": f"Campaign {i}",
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d"),
            "budget": round(random.uniform(5000, 50000), 2),
            "spend": round(random.uniform(1000, 40000), 2),
            "impressions": random.randint(10000, 1000000),
            "clicks": random.randint(1000, 100000),
            "conversions": random.randint(10, 1000),
            "revenue": round(random.uniform(1000, 100000), 2)
        }
        
        campaign["ctr"] = round(campaign["clicks"] / campaign["impressions"] * 100, 2)
        campaign["conversion_rate"] = round(campaign["conversions"] / campaign["clicks"] * 100, 2)
        campaign["roas"] = round(campaign["revenue"] / campaign["spend"], 2)
        
        campaigns.append(campaign)
    
    if campaign_id:
        campaign = next((c for c in campaigns if c["id"] == campaign_id), None)
        if not campaign:
            raise HTTPException(status_code=404, detail="Campaign not found")
        return campaign
    
    return {
        "total_campaigns": len(campaigns),
        "total_spend": sum(c["spend"] for c in campaigns),
        "total_revenue": sum(c["revenue"] for c in campaigns),
        "average_roas": round(sum(c["roas"] for c in campaigns) / len(campaigns), 2),
        "campaigns": campaigns
    }

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
    # TODO: Implement geospatial analysis logic
    return {"message": "Geospatial analysis endpoint"}

@app.get("/api/personalized-recommendations")
async def get_personalized_recommendations():
    # TODO: Implement recommendation engine logic
    return {"message": "Personalized recommendations endpoint"}

@app.get("/api/campaign-performance")
async def get_campaign_performance():
    # TODO: Implement campaign performance logic
    return {"message": "Campaign performance endpoint"}

@app.get("/api/competitor-analysis")
async def get_competitor_analysis():
    # TODO: Implement competitor analysis logic
    return {"message": "Competitor analysis endpoint"}