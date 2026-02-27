from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-27T14:57:00', 'schedule': None, 'catchup': False, 'dag_id': 'c2cd0979533842aab0b7ea6f7af84c22'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_a8fca21efbd347d3aafe6524123a691a = Task(
        dag,
        task_id='ExecuteFar_a8fca21efbd347d3aafe6524123a691a',
        workspace_id=4,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.10-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.10'},
        piece_input_kwargs={'lcp_path': '/home/domino/pieces_repository/pieces/ExecuteFarsitePiece/assets/test/final.lcp', 'inputs_path': '/home/domino/pieces_repository/pieces/ExecuteFarsitePiece/assets/test/Zavada.input', 'ignition_shp_path': 'pieces_repository', 'barrier_shp_path': '0', 'output_basename': 'run1', 'outputs_type': 1}
    )()

