import random
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from faker import Faker
from app import models
from app.database import SessionLocal, engine

fake = Faker()

def create_fake_products(db: Session, num_products: int = 50):
    categories = ['Electronics', 'Clothing', 'Home & Garden', 'Books', 'Toys', 'Sports', 'Beauty', 'Food']
    for _ in range(num_products):
        product = models.Product(
            name=f"{fake.color_name()} {fake.word()} {random.choice(['Pro', 'Plus', 'Max', 'Ultra', 'Lite'])}",
            category=random.choice(categories),
            price=round(random.uniform(10, 1000), 2),
            rating=round(random.uniform(1, 5), 1)
        )
        db.add(product)
    db.commit()

def create_fake_brochures(db: Session, num_brochures: int = 20):
    for _ in range(num_brochures):
        brochure = models.Brochure(
            title=fake.sentence(nb_words=4),
            views=random.randint(100, 10000),
            unique_visitors=random.randint(50, 5000),
            average_time_spent=round(random.uniform(30, 300), 2),
            click_through_rate=round(random.uniform(0.01, 0.2), 3),
            date=fake.date_time_between(start_date="-1y", end_date="now")
        )
        db.add(brochure)
    db.commit()

def create_fake_campaigns(db: Session, num_campaigns: int = 10):
    for _ in range(num_campaigns):
        start_date = fake.date_time_between(start_date="-6M", end_date="now")
        end_date = start_date + timedelta(days=random.randint(7, 90))
        campaign = models.Campaign(
            name=fake.company() + " " + fake.word() + " Campaign",
            start_date=start_date,
            end_date=end_date,
            budget=round(random.uniform(1000, 50000), 2),
            spend=round(random.uniform(500, 40000), 2),
            impressions=random.randint(10000, 1000000),
            clicks=random.randint(100, 100000),
            conversions=random.randint(1, 1000),
            revenue=round(random.uniform(1000, 100000), 2)
        )
        db.add(campaign)
    db.commit()

def create_fake_stores(db: Session, num_stores: int = 30):
    for _ in range(num_stores):
        store = models.Store(
            name=fake.company() + " Store",
            region=fake.state(),
            total_sales=round(random.uniform(10000, 1000000), 2),
            customer_density=random.randint(10, 1000),
            latitude=float(fake.latitude()),
            longitude=float(fake.longitude())
        )
        db.add(store)
    db.commit()

def create_fake_competitors(db: Session, num_competitors: int = 5):
    for _ in range(num_competitors):
        competitor = models.Competitor(
            name=fake.company(),
            market_share=round(random.uniform(5, 30), 2),
            customer_satisfaction=round(random.uniform(3, 5), 1),
            price_competitiveness=round(random.uniform(0.8, 1.2), 2),
            product_range=random.randint(100, 10000)
        )
        db.add(competitor)
    db.commit()

def main():
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        print("Creating fake products...")
        create_fake_products(db)
        print("Creating fake brochures...")
        create_fake_brochures(db)
        print("Creating fake campaigns...")
        create_fake_campaigns(db)
        print("Creating fake stores...")
        create_fake_stores(db)
        print("Creating fake competitors...")
        create_fake_competitors(db)
        print("Fake data generation complete!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        db.close()

if __name__ == "__main__":
    main()