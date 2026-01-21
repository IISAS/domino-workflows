from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-21T07:06:00', 'schedule': None, 'catchup': False, 'dag_id': '526c1c80b4af4492a521626900347d31'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    SleepPiece_9fd0da2607e142e39f77053138caff44 = Task(
        dag,
        task_id='SleepPiece_9fd0da2607e142e39f77053138caff44',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SleepPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'sleep_time': 1}
    )()
    SleepPiece_eefbd3df100e4d7a886c8d3d175babcb = Task(
        dag,
        task_id='SleepPiece_eefbd3df100e4d7a886c8d3d175babcb',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'SleepPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'sleep_time': 1}
    )()

    SleepPiece_eefbd3df100e4d7a886c8d3d175babcb.set_upstream([globals()[t] for t in ['SleepPiece_9fd0da2607e142e39f77053138caff44']])
