from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-21T07:37:00', 'schedule': None, 'catchup': False, 'dag_id': '013f83d5ecf2475692c111428f73b086'}

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
    LogPiece_228382ca75574560a8219931752f7a5e = Task(
        dag,
        task_id='LogPiece_228382ca75574560a8219931752f7a5e',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {'bucket': 'sadsadasd', 'base_folder': ''}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'LogPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'input_str': 'default value', 'input_int': 10, 'input_float': 10.5, 'input_bool': False, 'input_enum': 'option1', 'input_date': '2023-01-01', 'input_time': '16:20:00', 'input_datetime': '2023-01-01T16:20:00', 'input_array': ['default_1', 'default_2', 'default_3'], 'input_code': "print('Hello world!')"}
    )()
    print("XXXXXXXXX: ", LogPiece_228382ca75574560a8219931752f7a5e)
    LogPiece_228382ca75574560a8219931752f7a5e.set_upstream([globals()[t] for t in ['StringOper_b205b5da2ed849ee8836cda1f425fef6']])
