from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-17T08:42:00', 'schedule': None, 'catchup': False, 'dag_id': '2140c4c9484e460da4b9cf9d17e09d85'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_6a3825137466474e9905daa325f37e6d = Task(
        dag,
        task_id='HttpReques_6a3825137466474e9905daa325f37e6d',
        workspace_id=2,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?w=1260&h=750', 'method': 'GET', 'bearer_token': 'XXX', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n', 'output_type': 'both'}
    )()
    ImageFilte_1ba51c6c80db4b26984987b4a375f152 = Task(
        dag,
        task_id='ImageFilte_1ba51c6c80db4b26984987b4a375f152',
        workspace_id=2,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_6a3825137466474e9905daa325f37e6d', 'output_arg': 'image_file_path'}, 'sepia': True, 'black_and_white': False, 'brightness': False, 'darkness': False, 'contrast': True, 'red': False, 'green': False, 'blue': True, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()

    ImageFilte_1ba51c6c80db4b26984987b4a375f152.set_upstream([globals()[t] for t in ['HttpReques_6a3825137466474e9905daa325f37e6d']])
