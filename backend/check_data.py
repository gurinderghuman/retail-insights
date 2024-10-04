from sqlalchemy import create_engine, text
from app.database import SQLALCHEMY_DATABASE_URL

# Create an engine instance
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Connect to the database
with engine.connect() as connection:
    # Check the number of products
    result = connection.execute(text("SELECT COUNT(*) FROM products"))
    print(f"Number of products: {result.scalar()}")

    # Check the number of stores
    result = connection.execute(text("SELECT COUNT(*) FROM stores"))
    print(f"Number of stores: {result.scalar()}")

    # Check the number of competitors
    result = connection.execute(text("SELECT COUNT(*) FROM competitors"))
    print(f"Number of competitors: {result.scalar()}")

    # View some sample data
    print("\nSample products:")
    result = connection.execute(text("SELECT * FROM products LIMIT 5"))
    for row in result:
        print(row)

    print("\nSample stores:")
    result = connection.execute(text("SELECT * FROM stores LIMIT 5"))
    for row in result:
        print(row)

    print("\nSample competitors:")
    result = connection.execute(text("SELECT * FROM competitors LIMIT 5"))
    for row in result:
        print(row)