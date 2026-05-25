# test connection:
# from db import engine
# print(engine)

# test extraction
# data = extract_crypto_data()
# print(data[0])

# to test transformation of data
# raw_data = extract_crypto_data()

# df = transform_data(raw_data)

# print(df.head())

# # debug
# import sys
# # Prints the path to the active venv (or the global Python path if no venv)
# print(sys.prefix)

# # Returns True if you are inside a venv, False if not
# is_venv = sys.prefix != sys.base_prefix
# print(f"Is Venv Active: {is_venv}")

# connecting the entire pipeline
from extract import extract_crypto_data
raw_data = extract_crypto_data()

from transform import transform_data
df = transform_data(raw_data)


from load import load_data
load_data(df)

print("Pipeline completed")


# Logging
import logging
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO
)

logging.info("Pipeline started")