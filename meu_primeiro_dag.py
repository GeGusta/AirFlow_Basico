from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash_operator import BashOperator

with DAG(
    'meu_primeiro_dag',
    start_date=days_ago(2),
    schedule_interval='@daily'
) as dag:
    
    tarefa_1 = EmptyOperator(task_id='Tarefa_1')
    tarefa_2 = EmptyOperator(task_id='Tarefa_2')
    tarefa_3 = EmptyOperator(task_id='Tarefa_3')
    tarefa_4 = BashOperator(
        task_id = 'cria_pasta',
        bash_command='mkdir -p "/home/gustavo/Documents/pipelines/AirflowAlura/pasta_{{data_interval_end}}"'
    )

    tarefa_1 >> [tarefa_2, tarefa_3]
    tarefa_3 >> tarefa_4