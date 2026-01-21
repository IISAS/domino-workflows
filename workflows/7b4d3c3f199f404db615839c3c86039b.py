from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-21T07:22:00', 'schedule': None, 'catchup': False, 'dag_id': '7b4d3c3f199f404db615839c3c86039b'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    StringOper_b205b5da2ed849ee8836cda1f425fef6 = Task(
        dag,
        task_id='StringOper_b205b5da2ed849ee8836cda1f425fef6',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'None', 'provider_options': {'bucket': 'sadsadasd', 'base_folder': ''}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'StringOperationsPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'first_argument': 'sadsad', 'operations': [{'operation': 'lower_case', 'second_argument': 'asdsad', 'auxiliary_argument': 'sadsad'}]}
    )()

