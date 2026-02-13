from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-13T15:04:00', 'schedule': None, 'catchup': False, 'dag_id': 'ec07d11e971b438791fc562e6d309a48'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ImageFilte_20c6c49a223f4bf3b0814dd82dd21aef = Task(
        dag,
        task_id='imagefilte-20c6c49a223f4bf3b0814dd82dd21aef',
        workspace_id=7,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_3d27c836369a4bb18dc359c0be948d16', 'output_arg': 'base64_bytes_data'}, 'sepia': False, 'black_and_white': False, 'brightness': False, 'darkness': False, 'contrast': True, 'red': False, 'green': False, 'blue': True, 'cool': True, 'warm': False, 'output_type': 'both'}
    )()
    HttpReques_3d27c836369a4bb18dc359c0be948d16 = Task(
        dag,
        task_id='httpreques-3d27c836369a4bb18dc359c0be948d16',
        workspace_id=7,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'bearer_token': 'ZZZZZ', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

    ImageFilte_20c6c49a223f4bf3b0814dd82dd21aef.set_upstream([globals()[t] for t in ['HttpReques_3d27c836369a4bb18dc359c0be948d16']])
