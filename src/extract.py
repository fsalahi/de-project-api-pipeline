# Let's send request to coingecko with the following parameters
import requests
import logging

URL = "https://api.coingecko.com/api/v3/coins/markets"

PARAMS = {
    "vs_currency": "usd", # This is the only required param to send request to API,
    "order": "market_cap_desc", # The other params determine how you want to store them (apperantly)
    "per_page": 20,
    "page": 1
}
# then save and return the response
def extract_crypto_data():
    try:
        response = requests.get(URL, params=PARAMS)

        response.raise_for_status()

        logging.info("API extraction successful")

        return response.json()

    except requests.exceptions.RequestException as e:

        logging.error(f"API extraction failed: {e}")

        raise