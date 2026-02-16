from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-16T16:44:00', 'schedule': None, 'catchup': False, 'dag_id': 'fb3159968d8b44979fc20edc3f8577ab'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    imagefilter-3f78b4c5fb0c41f58be3fb0bdabfffb2 = Task(
        dag,
        task_id='imagefilter-3f78b4c5fb0c41f58be3fb0bdabfffb2',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'httprequest-edaf8e980a67491a92285160f200341b', 'output_arg': 'base64_bytes_data'}, 'sepia': False, 'black_and_white': False, 'brightness': True, 'darkness': False, 'contrast': False, 'red': False, 'green': True, 'blue': False, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()
    httprequest-edaf8e980a67491a92285160f200341b = Task(
        dag,
        task_id='httprequest-edaf8e980a67491a92285160f200341b',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'bearer_token': 'XXX', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

    imagefilter-3f78b4c5fb0c41f58be3fb0bdabfffb2.set_upstream([globals()[t] for t in ['httprequest-edaf8e980a67491a92285160f200341b']])
