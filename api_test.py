from getpass import getpass

import requests


def main():
    """Searches the Animals API and prints the results."""
    api_key = getpass("Enter your API key: ")
    animal_name = input("Enter an animal name: ").strip()

    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        params={"name": animal_name},
        headers={"X-Api-Key": api_key},
        timeout=30,
    )

    print("Status code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    main()