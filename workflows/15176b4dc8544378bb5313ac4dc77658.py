from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-02T14:59:00', 'schedule': None, 'catchup': False, 'dag_id': '15176b4dc8544378bb5313ac4dc77658'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    CreateIgni_4573f86e73004d71a42702f23aa2a39b = Task(
        dag,
        task_id='CreateIgni_4573f86e73004d71a42702f23aa2a39b',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.27-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.27'},
        piece_input_kwargs={'gps_text': '48.1486, 17.1077'}
    )()
    ExecuteFar_f9f2b90cd4b14e7688f9f59489752557 = Task(
        dag,
        task_id='ExecuteFar_f9f2b90cd4b14e7688f9f59489752557',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.27-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.27'},
        piece_input_kwargs={'lcp_path': '/work/test/final.lcp', 'inputs_path': '/work/test/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_4573f86e73004d71a42702f23aa2a39b', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()

    ExecuteFar_f9f2b90cd4b14e7688f9f59489752557.set_upstream([globals()[t] for t in ['CreateIgni_4573f86e73004d71a42702f23aa2a39b']])
