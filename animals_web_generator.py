from html import escape
from getpass import getpass

import requests


def fetch_animals(animal_name, api_key):
    """Fetches matching animals from the Animals API."""
    response = requests.get(
        "https://api.api-ninjas.com/v1/animals",
        params={"name": animal_name},
        headers={"X-Api-Key": api_key},
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def serialize_animal(animal_obj):
    """Returns an HTML card for a single animal."""
    output = '<li class="cards__item">\n'

    if "name" in animal_obj:
        output += (
            f'  <div class="card__title">{animal_obj["name"]}</div>\n'
        )

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        output += (
            f'    <strong>Diet:</strong> '
            f'{characteristics["diet"]}<br/>\n'
        )

    locations = animal_obj.get("locations", [])
    if locations:
        output += (
            f"    <strong>Location:</strong> {locations[0]}<br/>\n"
        )

    if "type" in characteristics:
        output += (
            f'    <strong>Type:</strong> '
            f'{characteristics["type"]}<br/>\n'
        )

    output += "  </p>\n"
    output += "</li>\n"
    return output


def main():
    """Generates the animal HTML page using API data."""
    api_key = getpass("Enter your API key: ")
    animal_name = input("Enter a name of an animal: ").strip()

    try:
        animals_data = fetch_animals(animal_name, api_key)
    except requests.RequestException as error:
        print(f"Could not fetch animals: {error}")
        return

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    output = ""

    if animals_data:
        for animal_obj in animals_data:
            output += serialize_animal(animal_obj)
    else:
        safe_name = escape(animal_name)
        output = (
            '<li class="cards__item">'
            f'<h2>The animal "{safe_name}" doesn\'t exist.</h2>'
            '</li>'
        )

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()
