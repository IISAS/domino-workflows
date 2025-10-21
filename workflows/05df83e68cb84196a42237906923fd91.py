from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2025-10-21T08:27:00', 'schedule': None, 'catchup': False, 'dag_id': '05df83e68cb84196a42237906923fd91'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    PageScrapp_f449fdb358ec4c6aa6640c7d84e9b2b3 = Task(
        dag,
        task_id='PageScrapp_f449fdb358ec4c6aa6640c7d84e9b2b3',
        workspace_id=2,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'PageScrapperPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'search_items': [{'class_name': '', 'tag': 'p'}]}
    )()

