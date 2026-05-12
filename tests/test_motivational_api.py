from src.motivational_api import get_motivational_quote


def test_get_motivational_quote():
    quote = get_motivational_quote()

    assert isinstance(quote, str)
    assert len(quote) > 0