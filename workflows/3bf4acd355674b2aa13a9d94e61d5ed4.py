from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2025-10-21T12:36:00', 'schedule': None, 'catchup': False, 'dag_id': '3bf4acd355674b2aa13a9d94e61d5ed4'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    LoremIpsum_ffb636ff8aec43528553728654593d74 = Task(
        dag,
        task_id='LoremIpsum_ffb636ff8aec43528553728654593d74',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'LoremIpsumGeneratorPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'items': 'words', 'number_of_items': 1}
    )()

