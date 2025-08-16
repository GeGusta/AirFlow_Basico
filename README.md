# AirFlow_Basico
## Objetivo
Uma empresa de turismo precisa ter a informação da temperatura em uma certa localidade, atualizada mensalmente com a previsão dos próximos 7 dias. Como solução vai ser construido uma pipeline no AirFlow que automatize o processo de extração dessa informação e disponibilização dela.
## Método
Foi desenvolvida uma DAG no AirFlow que consulta a API https://www.visualcrossing.com/ trazendo a previsão de 7 dias da cidade de São Caetano do Sul, alvo da empresa de turismo e, disponibilizando a informação em 3 arquivos na pasta nomeada com a data de previsão. Sendo agendado para executar toda segunda-feira.
## Resultado
* **dados_climaticos.py** - Script Python que implementa uma DAG no Airflow. Utiliza os operadores BASH e Python. É necessário trocar o parâmetro "key" para conseguir consultar a API;
* **semana_2025-08-04**: resultado do script, pasta com a data que foi feita a consulta e a previsão dos próximos 7 dias.
* **dados_brutos.csv**: dados brutos da consulta da API;
* **condicoes.csv**: dados separados da previsão da condição do clima;
* **temperatura.csv**: dados separados da previsão de temperatura.
