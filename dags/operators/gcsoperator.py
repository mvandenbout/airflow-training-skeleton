from dags.hooks.launchhook import LaunchHook

from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LaunchToGcsOperator(BaseOperator):

    @apply_defaults
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._launchhook = LaunchHook()

    def execute(self, context):
        results = self._launchhook.download(start_date, end_date)