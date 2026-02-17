from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-17T12:07:00', 'schedule': None, 'catchup': False, 'dag_id': 'c8e6054ac84544be9a37ec3f052067c5'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_9b65825b0c114506be8d4e91c4042165 = Task(
        dag,
        task_id='HttpReques_9b65825b0c114506be8d4e91c4042165',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?w=3000&h=1920', 'method': 'GET', 'bearer_token': 'ZZZZZ', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n', 'output_type': 'both'}
    )()
    ImageFilte_8c046b5524464c19bc2b376dc3d0f649 = Task(
        dag,
        task_id='ImageFilte_8c046b5524464c19bc2b376dc3d0f649',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_9b65825b0c114506be8d4e91c4042165', 'output_arg': 'image_file_path'}, 'sepia': True, 'black_and_white': True, 'brightness': False, 'darkness': True, 'contrast': False, 'red': False, 'green': False, 'blue': False, 'cool': False, 'warm': True, 'output_type': 'both'}
    )()

    ImageFilte_8c046b5524464c19bc2b376dc3d0f649.set_upstream([globals()[t] for t in ['HttpReques_9b65825b0c114506be8d4e91c4042165']])
