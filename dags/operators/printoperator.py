import json
import pathlib
import posixpath
import requests

import airflow
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class PrintOperator(BaseOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def execute(self, context):

        with open(f"/data/rocket_launches/ds={start_date}/launches.json") as f:
            data = json.load(f)
            rockets_launched = [launch["name"] for launch in data["launches"]]
            rockets_str = ""
            if rockets_launched:
                rockets_str = f" ({' & '.join(rockets_launched)})"
                print(f"{len(rockets_launched)} rocket launch(es) on {ds}{rockets_str}.")