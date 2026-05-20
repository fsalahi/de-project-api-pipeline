
# We are creating db connection file
from sqlalchemy import create_engine

DB_USER = "postgres"
DB_PASSWORD = "112358"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "crypto_pipeline"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)