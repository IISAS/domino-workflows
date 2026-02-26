from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-26T17:04:00', 'schedule': None, 'catchup': False, 'dag_id': 'a293f01df641422db2c2f17d1f4b57ca'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_0923421bd84d4640aa662a41f874357b = Task(
        dag,
        task_id='ExecuteFar_0923421bd84d4640aa662a41f874357b',
        workspace_id=2,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.2-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.2'},
        piece_input_kwargs={'lcp_path': '/work/in.lcp', 'inputs_path': '/work/in.input', 'ignition_shp_path': '/work/ignit.shp', 'barrier_shp_path': '0', 'output_basename': '/work/out/run1', 'outputs_type': 1}
    )()

