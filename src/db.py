
# # Version 1: We are creating db connection file, tentatively here, 
# # however this is not good practice
# from sqlalchemy import create_engine

# # DB_USER = "postgres"
# # DB_PASSWORD = "112358"
# # DB_HOST = "localhost"
# # DB_PORT = "5432"
# # DB_NAME = "crypto_pipeline"

# DATABASE_URL = (
#     f"postgresql://{DB_USER}:{DB_PASSWORD}"
#     f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# )

# engine = create_engine(DATABASE_URL)

# version 2: separating code and config

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)