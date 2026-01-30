from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-30T19:45:00', 'schedule': None, 'catchup': False, 'dag_id': '261cc4de21d3460ba166319f0b515316'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    HttpRequest_27dd10b0cd4b41a5bb118468b0a3c60b = Task(
        dag,
        task_id='httprequest-27dd10b0cd4b41a5bb118468b0a3c60b',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1', 'method': 'GET', 'bearer_token': 'XXXXX', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()
    ImageFilter_7a0d7be2528e4149831ad0a4308dcb62 = Task(
        dag,
        task_id='imagefilter-7a0d7be2528e4149831ad0a4308dcb62',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_27dd10b0cd4b41a5bb118468b0a3c60b', 'output_arg': 'base64_bytes_data'}, 'sepia': False, 'black_and_white': True, 'brightness': False, 'darkness': False, 'contrast': False, 'red': False, 'green': False, 'blue': False, 'cool': True, 'warm': False, 'output_type': 'both'}
    )()

    ImageFilter_7a0d7be2528e4149831ad0a4308dcb62.set_upstream([globals()[t] for t in ['HttpRequest_27dd10b0cd4b41a5bb118468b0a3c60b']])
