from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-11T08:47:00', 'schedule': None, 'catchup': False, 'dag_id': 'bb7688be521a4e9b8fdc93c4054854f2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpReques_db9b72336a854200b9fcd41b48d69024 = Task(
        dag,
        task_id='httpreques-db9b72336a854200b9fcd41b48d69024',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'bearer_token': 'SSSS', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()
    ImageFilte_03288d1e8caf4426932809fadcb7edb7 = Task(
        dag,
        task_id='imagefilte-03288d1e8caf4426932809fadcb7edb7',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'httpreques-db9b72336a854200b9fcd41b48d69024', 'output_arg': 'base64_bytes_data'}, 'sepia': True, 'black_and_white': False, 'brightness': False, 'darkness': False, 'contrast': False, 'red': False, 'green': True, 'blue': False, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()
    SaveImageP_96574846d789416c8f4f8885bea5411c = Task(
        dag,
        task_id='saveimageo_96574846d789416c8f4f8885bea5411c',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'SaveImagePiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'base64_data': {'type': 'fromUpstream', 'upstream_task_id': 'imagefilte-03288d1e8caf4426932809fadcb7edb7', 'output_arg': 'image_base64_string'}}
    )()

    ImageFilte_03288d1e8caf4426932809fadcb7edb7.set_upstream([globals()[t] for t in ['HttpReques_db9b72336a854200b9fcd41b48d69024']])
    SaveImageP_96574846d789416c8f4f8885bea5411c.set_upstream([globals()[t] for t in ['ImageFilte_03288d1e8caf4426932809fadcb7edb7']])
