import logging
from extract import extract_crypto_data
from transform import transform_data
from extract import extract_crypto_data
from extract import extract_crypto_data
from transform import transform_data
from load import load_data

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

# connecting the entire pipeline
raw_data = extract_crypto_data()

df = transform_data(raw_data)

load_data(df)

print("Pipeline completed")


# Logging
logging.basicConfig(
    filename='logs/pipeline.log',
    level=logging.INFO
)

logging.info("Pipeline started")