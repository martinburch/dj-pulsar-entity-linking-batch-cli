import pandas as pd
from .annotate import link
import json
from sklearn.metrics import precision_score, recall_score, f1_score

DATASET = pd.read_csv("resources/golden_dataset.csv")


def metrics(url):
    """Calculates metrics for the linking

    Arguments:
        url {string} -- The url of the linking service

    Returns:
        dict -- A dict with the value results for the metrics
    """
    df = json.loads(DATASET.to_json(orient="records"))
    results = pd.DataFrame([link(entry, url) for entry in df])

    expected_fcode = DATASET["Fcode"].fillna("").tolist()
    obtained_iri = results["iri"].fillna("").tolist()
    obtained_fcode = [item.split("/")[-1] for item in obtained_iri]

    precision = precision_score(expected, obtained, average="micro")
    recall = recall_score(expected, obtained, average="micro")
    f1 = f1_score(expected, obtained, average="micro")

    return {"precision": precision, "recall": recall, "f1": f1}
