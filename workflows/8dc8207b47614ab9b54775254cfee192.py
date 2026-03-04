from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-04T12:37:00', 'schedule': None, 'catchup': False, 'dag_id': '8dc8207b47614ab9b54775254cfee192'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    EvaluatePe_cbafe46bc1e341fd8dfd34f38d3b9c82 = Task(
        dag,
        task_id='EvaluatePe_cbafe46bc1e341fd8dfd34f38d3b9c82',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.37-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.37'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_cc65553ab3994c2aab337b08c3055013', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_6355faa353f64d7dbbbb766cab4676fa', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp', 'api_model_name': 'Model 2'}
    )()
    CreateIgni_6355faa353f64d7dbbbb766cab4676fa = Task(
        dag,
        task_id='CreateIgni_6355faa353f64d7dbbbb766cab4676fa',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.37-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.37'},
        piece_input_kwargs={'gps_text': '49.066, 18.490', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()
    ExecuteFar_cc65553ab3994c2aab337b08c3055013 = Task(
        dag,
        task_id='ExecuteFar_cc65553ab3994c2aab337b08c3055013',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.37-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.37'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_6355faa353f64d7dbbbb766cab4676fa', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()

    EvaluatePe_cbafe46bc1e341fd8dfd34f38d3b9c82.set_upstream([globals()[t] for t in ['CreateIgni_6355faa353f64d7dbbbb766cab4676fa', 'ExecuteFar_cc65553ab3994c2aab337b08c3055013']])
    ExecuteFar_cc65553ab3994c2aab337b08c3055013.set_upstream([globals()[t] for t in ['CreateIgni_6355faa353f64d7dbbbb766cab4676fa']])
