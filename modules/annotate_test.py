import requests
import json
import os
import pandas as pd
from .annotate import link, annotate
from io import StringIO


entry = {"company_name": "Google, Inc", "country": "USA"}
entry_expected = {"company_name": "Google, Inc", "country": "USA", "iri": "http://data.dowjones.com/entity/GOOG"}
url = "http://test.com"
payload = {"link": {"format": "http://data.dowjones.com/entity/GOOG"}}


def test_link(requests_mock):
    requests_mock.get(url, json=payload)
    response = requests.get(url)
    assert link(entry, url) == entry_expected
