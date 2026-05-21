import pandas as pd
from datetime import datetime

def transform_data(data):

    records = []

    for coin in data:
        records.append({
            "name": coin["name"],
            "symbol": coin["symbol"],
            "current_price": coin["current_price"],
            "market_cap": coin["market_cap"],
            "price_change_24h": coin["price_change_percentage_24h"]
        })

    df = pd.DataFrame(records)
    df["extraction_date"] = datetime.now().date()
    df["extracted_at"] = datetime.now()
    return df