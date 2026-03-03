from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-03T10:43:00', 'schedule': None, 'catchup': False, 'dag_id': '88cdd3de5f1f4770b196a7f6367915d9'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    CreateIgni_1487aedea616444a8b04a94ceb70adfa = Task(
        dag,
        task_id='CreateIgni_1487aedea616444a8b04a94ceb70adfa',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.29-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.29'},
        piece_input_kwargs={'gps_text': '49.06581, 18.4925', 'epsg_code': '5514'}
    )()

