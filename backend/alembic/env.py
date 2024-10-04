import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# ... (rest of the existing code)

# Import the Base object from your models
from app.models import Base
target_metadata = Base.metadata

# ... (rest of the existing code)