import pytest

from .scrape import scrape


def test_scrape():
    assert scrape(keyword='placeholder', count=5) == 'placeholder'