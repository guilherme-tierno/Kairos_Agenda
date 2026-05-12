import requests


API_URL = "https://zenquotes.io/api/random"


def get_motivational_quote():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()[0]

        quote = data["q"]
        author = data["a"]

        return f'"{quote}" - {author}'

    except requests.RequestException:
        return (
            '"O sucesso é a soma de pequenos esforços repetidos diariamente." '
            "- Robert Collier"
        )