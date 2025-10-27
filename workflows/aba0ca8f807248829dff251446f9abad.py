from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2025-10-27T07:51:00', 'schedule': None, 'catchup': False, 'dag_id': 'aba0ca8f807248829dff251446f9abad'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    TimeSeries_8bd121dd77bd4f06910caac94d7baad7 = Task(
        dag,
        task_id='TimeSeries_8bd121dd77bd4f06910caac94d7baad7',
        workspace_id=1,
        workflow_shared_storage={'source': 'None', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': True},
        piece={'name': 'TimeSeriesClassificationTrainPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.5-group2', 'repository_url': 'https://github.com/iisas/spice_domino_pieces', 'repository_version': '0.2.5'},
        piece_input_kwargs={'train_data_path': 'https://raw.githubusercontent.com/hfawaz/cd-diagram/master/FordA/', 'num_layers': 3, 'filters_per_layer': [64, 64, 64], 'kernel_sizes': [3, 3, 3], 'batch_size': 32, 'epochs': 500}
    )()

