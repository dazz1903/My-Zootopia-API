import json


def load_data(file_path):
    """Loads animal data from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


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
    """Generates the animal HTML page using the template."""
    animals_data = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template = template_file.read()

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    html_content = template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_content)

    print("Created animals.html")


if __name__ == "__main__":
    main()