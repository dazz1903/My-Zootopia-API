# My Zootopia API

A Python learning project that fetches animal information from the
API Ninjas Animals API and generates an HTML website.

Users can search for an animal and view its diet, first location,
and type when available. If no animals match, the website displays
a message.

## Installation

Clone the repository:

```bash
git clone https://github.com/dazz1903/My-Zootopia-API.git
cd My-Zootopia-API
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Sign up at https://api-ninjas.com/ to get an API key.

Create a `.env` file in the project folder containing:

```ini
API_KEY='your_api_key_here'
```

The `.env` file is ignored by Git. Keep your API key private.

## Usage

Run the website generator:

```bash
python animals_web_generator.py
```

Enter an animal name, such as `Fox` or `Snake`, when prompted.

Open `animals.html` in your browser to view the results.
After another search, refresh the browser to see the updated page.

On systems where Python uses the `python3` command, use that
instead of `python`.

## Project Files

- `data_fetcher.py`: Fetches animal data from the API.
- `animals_web_generator.py`: Converts animal data into HTML.
- `animals_template.html`: Defines the page layout and styles.
- `animals.html`: Generated website.
- `requirements.txt`: Lists external Python dependencies.