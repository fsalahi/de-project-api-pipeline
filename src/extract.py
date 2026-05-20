# Let's send request to coingecko with the following parameters
import requests

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd", # This is the only required param to send request to API,
    "order": "market_cap_desc", # The other params determine how you want to store them (apperantly)
    "per_page": 20,
    "page": 1
}
# then save and return the response
def extract_crypto_data():
    response = requests.get(URL, params=PARAMS)

    if response.status_code != 200:
        raise Exception("API request failed")

    return response.json()