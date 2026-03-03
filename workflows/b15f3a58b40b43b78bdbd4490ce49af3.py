from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-03T15:28:00', 'schedule': None, 'catchup': False, 'dag_id': 'b15f3a58b40b43b78bdbd4490ce49af3'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    CreateIgni_e45acb961b1048509d00a88236051b2a = Task(
        dag,
        task_id='CreateIgni_e45acb961b1048509d00a88236051b2a',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.32-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.32'},
        piece_input_kwargs={'gps_text': '49.067464,18.480035'}
    )()
    ExecuteFar_723db61603264a51a57c2f94fc619cb1 = Task(
        dag,
        task_id='ExecuteFar_723db61603264a51a57c2f94fc619cb1',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.32-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.32'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_e45acb961b1048509d00a88236051b2a', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_d9711a2f56fa4e5b9b798db47e1522b5 = Task(
        dag,
        task_id='EvaluatePe_d9711a2f56fa4e5b9b798db47e1522b5',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.32-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.32'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_723db61603264a51a57c2f94fc619cb1', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_e45acb961b1048509d00a88236051b2a', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp', 'api_model_name': 'Model 2'}
    )()

    ExecuteFar_723db61603264a51a57c2f94fc619cb1.set_upstream([globals()[t] for t in ['CreateIgni_e45acb961b1048509d00a88236051b2a']])
    EvaluatePe_d9711a2f56fa4e5b9b798db47e1522b5.set_upstream([globals()[t] for t in ['CreateIgni_e45acb961b1048509d00a88236051b2a', 'ExecuteFar_723db61603264a51a57c2f94fc619cb1']])
