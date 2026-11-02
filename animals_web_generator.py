from html import escape

import data_fetcher


def serialize_animal(animal_obj):
    """Returns an HTML card for a single animal."""
    output = '<li class="cards__item">\n'

    if "name" in animal_obj:
        name = escape(animal_obj["name"])
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <p class="card__text">\n'

    characteristics = animal_obj.get("characteristics", {})

    if "diet" in characteristics:
        diet = escape(characteristics["diet"])
        output += f"    <strong>Diet:</strong> {diet}<br/>\n"

    locations = animal_obj.get("locations", [])
    if locations:
        location = escape(locations[0])
        output += f"    <strong>Location:</strong> {location}<br/>\n"

    if "type" in characteristics:
        animal_type = escape(characteristics["type"])
        output += f"    <strong>Type:</strong> {animal_type}<br/>\n"

    output += "  </p>\n"
    output += "</li>\n"
    return output


def main():
    """Generates an animal website using the data fetcher."""
    animal_name = input("Enter a name of an animal: ").strip()

    try:
        animals_data = data_fetcher.fetch_data(animal_name)
    except data_fetcher.DataFetchError as error:
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