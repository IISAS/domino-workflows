from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-30T13:09:00', 'schedule': None, 'catchup': False, 'dag_id': 'c44114ecd0a247e7858ed91141d05a78'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_e36ba8845fa54fe6871421e5f49c8824 = Task(
        dag,
        task_id='HttpReques_e36ba8845fa54fe6871421e5f49c8824',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'url': 'http://sadsadsad', 'method': 'GET', 'bearer_token': 'XXXXX', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

