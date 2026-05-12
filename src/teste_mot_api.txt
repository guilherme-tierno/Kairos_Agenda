import requests


API_URL = "https://zenquotes.io/api/random"


def get_motivational_quote():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()

        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        return f'"{quote}" - {author}'

    except requests.RequestException:
        return "Não foi possível obter frase motivacional no momento."