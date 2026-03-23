from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-23T12:38:00', 'schedule': None, 'catchup': False, 'dag_id': 'd4086f149595425fa09697521673b73c'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    RandomNumP_fd9acc94dfb14e23975d8f6f1d15f5c3 = Task(
        dag,
        task_id='RandomNumP_fd9acc94dfb14e23975d8f6f1d15f5c3',
        workspace_id=7,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'RandomNumPiece', 'source_image': 'ghcr.io/trmaxxx/speech_domino_pieces:0.0.1a-group1', 'repository_url': 'https://github.com/TrMaXXX/dicris_speech', 'repository_version': '0.0.1a'},
        piece_input_kwargs={'max_num': 100, 'min_num': 0}
    )()

