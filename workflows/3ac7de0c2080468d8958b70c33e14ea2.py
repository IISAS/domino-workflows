from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-25T16:48:00', 'schedule': None, 'catchup': False, 'dag_id': '3ac7de0c2080468d8958b70c33e14ea2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_ab071f4006d34dd684461ea61aea4203 = Task(
        dag,
        task_id='HttpReques_ab071f4006d34dd684461ea61aea4203',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg', 'method': 'GET', 'bearer_token': 'SSSS', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n', 'output_type': 'both'}
    )()
    ImageFilte_1fb8ad93d1fb43a6ba33321b4b7092a5 = Task(
        dag,
        task_id='ImageFilte_1fb8ad93d1fb43a6ba33321b4b7092a5',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_ab071f4006d34dd684461ea61aea4203', 'output_arg': 'image_file_path'}, 'sepia': False, 'black_and_white': True, 'brightness': False, 'darkness': False, 'contrast': False, 'red': False, 'green': False, 'blue': True, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()

    ImageFilte_1fb8ad93d1fb43a6ba33321b4b7092a5.set_upstream([globals()[t] for t in ['HttpReques_ab071f4006d34dd684461ea61aea4203']])
