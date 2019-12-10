from launchhook import LaunchHook
import json
import pathlib
import posixpath
import airflow
import requests

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LaunchToGcsOperator(BaseOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._launchhook = LaunchHook()

    def execute(self, start_date, end_date):
        results = self._launchhook.download(start_date, end_date)