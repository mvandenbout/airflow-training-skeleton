import json
import pathlib
import posixpath
import airflow
import requests

class LaunchHook(BaseHook):

    def __init__(self):
        super().__init__(source=None)

    def download(self, start_date, end_data):
        query = f"https://launchlibrary.net/1.4/launch?startdate={start_date}&enddate={end_data}"
        result_path = f"/data/rocket_launches/ds={start_date}"
        pathlib.Path(result_path).mkdir(parents=True, exist_ok=True)
        response = requests.get(query)
        with open(posixpath.join(result_path, "launches.json"), "w") as f:
            f.write(response.text)