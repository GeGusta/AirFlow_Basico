from airflow import DAG
import pendulum
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import os
from os.path import join
import pandas as pd
from airflow.macros import ds_add

with DAG(
    "dados_climaticos",
    start_date=pendulum.datetime(2025,7,28, tz="UTC"),
    schedule_interval='0 0 * * 1', #executar toda segunda
)as dag:
    tarefa_1 = BashOperator(
        task_id = 'cria_pasta',
        bash_command='mkdir -p "/home/gustavo/Documents/pipelines/AirflowAlura/semana_{{data_interval_end.strftime("%Y-%m-%d")}}"'
    )

    def extrai_dados(data_interval_end):
        
        #Dados de localizacao de SCS e chave para acessar a API
        city = "-23.6226,-46.5489"
        key = "SUA_CHAVE"

        URL = join("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/", 
                f"{city}/{data_interval_end}/{ds_add(data_interval_end, 7)}?unitGroup=metric&include=days&key={key}&contentType=csv")

        dados = pd.read_csv(URL)

        #print(dados.head())

        file_path = f"/home/gustavo/Documents/pipelines/AirflowAlura/semana_{data_interval_end}/"
        

        dados.to_csv(file_path + "dados_brutos.csv")
        dados[["datetime", "tempmin", "temp", "tempmax"]].to_csv(file_path + "temperatura.csv")
        dados[["datetime", "description", "icon"]].to_csv(file_path+"condicoes.csv")

    tarefa_2 = PythonOperator(
        task_id = "extrai_dados",
        python_callable = extrai_dados,
        op_kwargs = {'data_interval_end':'{{data_interval_end.strftime("%Y-%m-%d")}}'}
    )

    tarefa_1 >> tarefa_2