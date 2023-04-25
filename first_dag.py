from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_dag_args = {
    'start_date': datetime(2023, 4, 25),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries':1,
    'retry_delay': timedelta(minutes=5),
    'project_id':1
}

with DAG("First_DAG", schedule_interval=None, default_args = default_dag_args) as dag:
    
    task_0 = BashOperator(task_id = 'bash_task', bash_command = "echo 'command executed from the Bash operator'")
    task_1 = BashOperator(task_id = 'bash_task_move_data', bash_command = "cp  C:/Muttaki/Data/data_center/data_lake/dataset_raw.txt C:/Muttaki/Data/data_center/clean_data")
    task_2 = BashOperator(task_id = 'bash_task_remove_data', bash_command = "del 'C:/Muttaki/Data/data_center/data_lake/dataset_raw.txt'")
    
    task_0 >> task_1 >> task_2
