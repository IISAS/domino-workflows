from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-16T19:19:00', 'schedule': None, 'catchup': False, 'dag_id': 'c99e600d3c3a4f3aa7f1ca2659a6df65'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ImageFilte_a2493188ba5348419adff676bb372305 = Task(
        dag,
        task_id='ImageFilte_a2493188ba5348419adff676bb372305',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'ImageFilterPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'input_image': {'type': 'fromUpstream', 'upstream_task_id': 'HttpReques_f27e3dfd8d014fa892ef6dc5707a0b22', 'output_arg': 'base64_bytes_data'}, 'sepia': True, 'black_and_white': False, 'brightness': False, 'darkness': False, 'contrast': False, 'red': True, 'green': False, 'blue': False, 'cool': False, 'warm': False, 'output_type': 'both'}
    )()
    HttpReques_f27e3dfd8d014fa892ef6dc5707a0b22 = Task(
        dag,
        task_id='HttpReques_f27e3dfd8d014fa892ef6dc5707a0b22',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'HttpRequestPiece', 'source_image': 'ghcr.io/iisas/default_domino_pieces:0.9.0-group0', 'repository_url': 'https://github.com/IISAS/default_domino_pieces', 'repository_version': '0.9.0'},
        piece_input_kwargs={'url': 'https://images.pexels.com/photos/4055758/pexels-photo-4055758.jpeg', 'method': 'GET', 'bearer_token': 'ZZZZ', 'body_json_data': '{\n    "key_1": "value_1",\n    "key_2": "value_2"\n}\n'}
    )()

    ImageFilte_a2493188ba5348419adff676bb372305.set_upstream([globals()[t] for t in ['HttpReques_f27e3dfd8d014fa892ef6dc5707a0b22']])
