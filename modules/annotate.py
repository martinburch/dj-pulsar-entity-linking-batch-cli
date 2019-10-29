import pandas as pd
import requests
import json


def link(entry, url):
    """Finds ID for one single entry

    Arguments:
        entry {string} -- Name of company we want to link
        url {url} -- Url of the remote service linking

    Returns:
        dict -- Dictionary with the original entry with the extra iri field
    """
    params = {"company_name": entry["company_name"], "country": entry["country"]}
    iri = requests.get(url, params=params).json()["link"]["format"]
    entry["iri"] = iri
    return entry


def annotate(csv, url):
    """It reads the CSV provided and annotates it in bulk using a call to the link function

    Arguments:
        csv {string} -- path to the CSV you want to annotate
        url {string} -- url of the remote linking service
    """
    df = json.loads(pd.read_csv(csv).to_json(orient="records"))
    pd.DataFrame([link(entry, url) for entry in df]).to_csv(f"{csv[:-4]}_annotated.csv")
