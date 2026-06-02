# Let's send request to coingecko with the following parameters
import requests
import logging

def extract_crypto_data(url, params):
    try:
        response = requests.get(url, params)

        response.raise_for_status()

        logging.info("API extraction successful")

        return response.json()

    except requests.exceptions.RequestException as e:

        logging.error(f"API extraction failed: {e}")

        raise



def normalize_response(response_json):
    pass


def save_raw_data(df, path):
    pass