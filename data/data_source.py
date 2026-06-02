# where to extract data and what params
def data_source():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd", # This is the only required param to send request to API,
        "order": "market_cap_desc", # The other params determine how you want to store them (apperantly)
        "per_page": 20,
        "page": 1
    }
    return (url, params)