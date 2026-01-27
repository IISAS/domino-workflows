from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-27T14:54:00', 'schedule': None, 'catchup': False, 'dag_id': '899e3a33fe7546078039ebb280cc61d3'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    KafkaConsu_f8032f4ba7bf453ebd1eaf57a8c0ee2d = Task(
        dag,
        task_id='KafkaConsu_f8032f4ba7bf453ebd1eaf57a8c0ee2d',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'KafkaConsumerPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'topics': ['default-topic'], 'bootstrap_servers': 'localhost:9093', 'security_protocol': 'SSL', 'group_id': 'default-group', 'auto_offset_reset': 'earliest', 'message_polling_timeout': 5, 'no_message_timeout': 10, 'output_format': 'message'}
    )()

