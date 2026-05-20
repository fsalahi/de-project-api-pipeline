# let's load transformed dataframe into a postgresql table
from db import engine

def load_data(df):

    df.to_sql(
        "crypto_market",
        engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully")