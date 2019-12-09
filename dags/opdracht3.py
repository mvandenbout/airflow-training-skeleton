import airflow
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator

args = {
    'owner': 'Airflow',
    'start_date': airflow.utils.dates.days_ago(5),
}

with DAG(
        dag_id='opdracht2',
        default_args=args,
        dagrun_timeout=None,
        schedule_interval='45 13 * * 1,3,5',

) as dag:
    task1 = DummyOperator(task_id='task1')
    task2 = DummyOperator(task_id='task2')
    task3 = DummyOperator(task_id='task3')
    task4 = DummyOperator(task_id='task4')
    task5 = DummyOperator(task_id='task5')

task1 >> task2 >> [task3, task4] >> task5


