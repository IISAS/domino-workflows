from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-13T14:57:00', 'schedule': None, 'catchup': False, 'dag_id': '0270696262fe499c915513135e73d7b2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    SleepPiece_d08f7ea4f35b49db935ced2c9ecfef77 = Task(
        dag,
        task_id='SleepPiece_d08f7ea4f35b49db935ced2c9ecfef77',
        workspace_id=7,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SleepPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'sleep_time': 1}
    )()

