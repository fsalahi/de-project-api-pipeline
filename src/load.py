# let's load transformed dataframe into a postgresql table
from db import engine

# version 1
# def load_data(df):

#     df.to_sql(
#         "crypto_market",
#         engine,
#         if_exists="replace",
#         index=False
#     )

#     print("Data loaded successfully")

# version 2
def load_data(df):

    df.to_sql(
        "crypto_market",
        engine,
        if_exists="append",
        index=False
    )

    print("Data loaded successfully")