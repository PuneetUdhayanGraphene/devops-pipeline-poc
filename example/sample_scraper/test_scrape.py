import pytest

from .scrape import scrape


def test_scrape():
    assert scrape(keyword='bob', count=5) == 'no'