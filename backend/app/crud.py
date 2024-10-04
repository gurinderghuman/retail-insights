from sqlalchemy.orm import Session
from . import models, schemas

# Product operations (existing code)
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, product: schemas.ProductUpdate):
    db_product = get_product(db, product_id)
    if db_product:
        update_data = product.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product

# Brochure operations
def get_brochure(db: Session, brochure_id: int):
    return db.query(models.Brochure).filter(models.Brochure.id == brochure_id).first()

def get_brochures(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Brochure).offset(skip).limit(limit).all()

def create_brochure(db: Session, brochure: schemas.BrochureCreate):
    db_brochure = models.Brochure(**brochure.dict())
    db.add(db_brochure)
    db.commit()
    db.refresh(db_brochure)
    return db_brochure

# Campaign operations
def get_campaign(db: Session, campaign_id: int):
    return db.query(models.Campaign).filter(models.Campaign.id == campaign_id).first()

def get_campaigns(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Campaign).offset(skip).limit(limit).all()

def create_campaign(db: Session, campaign: schemas.CampaignCreate):
    db_campaign = models.Campaign(**campaign.dict())
    db.add(db_campaign)
    db.commit()
    db.refresh(db_campaign)
    return db_campaign

# Store operations
def get_store(db: Session, store_id: int):
    return db.query(models.Store).filter(models.Store.id == store_id).first()

def get_stores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Store).offset(skip).limit(limit).all()

def create_store(db: Session, store: schemas.StoreCreate):
    db_store = models.Store(**store.dict())
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store

# Competitor operations
def get_competitor(db: Session, competitor_id: int):
    return db.query(models.Competitor).filter(models.Competitor.id == competitor_id).first()

def get_competitors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Competitor).offset(skip).limit(limit).all()

def create_competitor(db: Session, competitor: schemas.CompetitorCreate):
    db_competitor = models.Competitor(**competitor.dict())
    db.add(db_competitor)
    db.commit()
    db.refresh(db_competitor)
    return db_competitor