from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-20T08:18:00', 'schedule': None, 'catchup': False, 'dag_id': '677cadb2b3a340e999ff11ecae2639f7'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    EvaluatePe_77e85bd6882a4db9ba9d07da21854c1b = Task(
        dag,
        task_id='EvaluatePe_77e85bd6882a4db9ba9d07da21854c1b',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_5de5c10b3df54ddaa86ddfec9b2c4c76', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    ExecuteFar_5de5c10b3df54ddaa86ddfec9b2c4c76 = Task(
        dag,
        task_id='ExecuteFar_5de5c10b3df54ddaa86ddfec9b2c4c76',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc = Task(
        dag,
        task_id='CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.46-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.46'},
        piece_input_kwargs={'gps_text': '49.066, 18.490', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    EvaluatePe_77e85bd6882a4db9ba9d07da21854c1b.set_upstream([globals()[t] for t in ['CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc', 'ExecuteFar_5de5c10b3df54ddaa86ddfec9b2c4c76']])
    ExecuteFar_5de5c10b3df54ddaa86ddfec9b2c4c76.set_upstream([globals()[t] for t in ['CreateIgni_d648f45511d14b0dbd6bd19c0230a2bc']])
