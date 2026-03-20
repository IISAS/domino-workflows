from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-20T08:01:00', 'schedule': None, 'catchup': False, 'dag_id': 'b1aedc4c4a6043d88967b2895c7abdec'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    CreateIgni_52f0de2cf61f4428baa0bb4e7d1c8cce = Task(
        dag,
        task_id='CreateIgni_52f0de2cf61f4428baa0bb4e7d1c8cce',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'gps_text': '49.066, 18.490', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

