import airflow
from airflow.models import DAG

from gcsoperator import LaunchToGcsOperator
from printoperator import PrintOperator


args = {
    "owner": "mvandenbout@bol.com",
    "start_date": airflow.utils.dates.days_ago(10)
}

with DAG(
        dag_id="download_rocket_launches",
        default_args=args,
        description="DAG downloading rocket launches from Launch Library.",
        schedule_interval="0 0 * * *"
) as dag:

    gcs_operator = LaunchToGcsOperator(task_id='fetch_to_gcs', name='fetch_to_gcs')
    print_operator = PrintOperator(task_id='print_results', name='print_results')

gcs_operator >> print_operator