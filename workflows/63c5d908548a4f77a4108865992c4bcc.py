from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-20T08:59:00', 'schedule': None, 'catchup': False, 'dag_id': '63c5d908548a4f77a4108865992c4bcc'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_677237fc35554a639c3fb1929a585627 = Task(
        dag,
        task_id='ExecuteFar_677237fc35554a639c3fb1929a585627',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_509cc6a212ec4fe7bb40811baa2f70e8 = Task(
        dag,
        task_id='EvaluatePe_509cc6a212ec4fe7bb40811baa2f70e8',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_677237fc35554a639c3fb1929a585627', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48 = Task(
        dag,
        task_id='CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'gps_text': '49.066, 18.481', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    ExecuteFar_677237fc35554a639c3fb1929a585627.set_upstream([globals()[t] for t in ['CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48']])
    EvaluatePe_509cc6a212ec4fe7bb40811baa2f70e8.set_upstream([globals()[t] for t in ['ExecuteFar_677237fc35554a639c3fb1929a585627', 'CreateIgni_7eaf6bb6dc924eeeb19e92600f56db48']])
