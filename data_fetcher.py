import os

import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.environ.get("API_KEY", "")
API_URL = "https://api.api-ninjas.com/v1/animals"


class DataFetchError(Exception):
    """Raised when animal data cannot be fetched."""


def fetch_data(animal_name):
    """Returns a list of animal dictionaries matching the name."""
    if not API_KEY.strip():
        raise DataFetchError(
            "The ANIMALS_API_KEY environment variable is missing."
        )

    try:
        response = requests.get(
            API_URL,
            params={"name": animal_name},
            headers={"X-Api-Key": API_KEY.strip()},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as error:
        raise DataFetchError(str(error)) from error
