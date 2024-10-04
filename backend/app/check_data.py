import os
import sys

# Add the current directory and the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.extend([current_dir, parent_dir])

from dotenv import load_dotenv
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from models import Product, Brochure, Campaign, Store, Competitor
from database import Base

# Load environment variables
load_dotenv(dotenv_path=os.path.join(parent_dir, '.env'))

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def check_table_count(model):
    count = session.query(func.count(model.id)).scalar()
    print(f"Number of {model.__name__}s: {count}")
    if count > 0:
        first_item = session.query(model).first()
        print(f"Sample {model.__name__}: {first_item}")
    print()

if __name__ == "__main__":
    print("Checking database contents:\n")
    check_table_count(Product)
    check_table_count(Brochure)
    check_table_count(Campaign)
    check_table_count(Store)
    check_table_count(Competitor)

session.close()