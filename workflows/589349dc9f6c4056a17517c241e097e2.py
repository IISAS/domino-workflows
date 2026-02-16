from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-16T09:35:00', 'schedule': None, 'catchup': False, 'dag_id': '589349dc9f6c4056a17517c241e097e2'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    imagefilter_cec97ebb06ea41279e13502128a315e8 = Task(
        dag,
        task_id='imagefilter-cec97ebb06ea41279e13502128a315e8',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'httprequest-040758724d94477d93e9b073f6b2e8cb', 'output_arg': 'base64_bytes_data'}, 'sepia': False, 'black_and_white': False, 'brightness': False, 'darkness': False, 'contrast': False, 'red': False, 'green': False, 'blue': False, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()
    httprequest_040758724d94477d93e9b073f6b2e8cb = Task(
        dag,
        task_id='httprequest-040758724d94477d93e9b073f6b2e8cb',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'bearer_token': 'ZZZZZ', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

    imagefilter-cec97ebb06ea41279e13502128a315e8.set_upstream([globals()[t] for t in ['httprequest_040758724d94477d93e9b073f6b2e8cb']])
