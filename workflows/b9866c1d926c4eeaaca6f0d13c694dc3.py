from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-02T08:59:00', 'schedule': None, 'catchup': False, 'dag_id': 'b9866c1d926c4eeaaca6f0d13c694dc3'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_47b8ef8712fa4e278d065452ef95716d = Task(
        dag,
        task_id='ExecuteFar_47b8ef8712fa4e278d065452ef95716d',
        workspace_id=4,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.19-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.19'},
        piece_input_kwargs={'lcp_path': '/work/test/final.lcp', 'inputs_path': '/work/test/Zavada.input', 'ignition_shp_path': '/work/test/ignition.shp', 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()

