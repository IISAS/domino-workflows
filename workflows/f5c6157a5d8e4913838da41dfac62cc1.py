from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-05T16:54:00', 'schedule': None, 'catchup': False, 'dag_id': 'f5c6157a5d8e4913838da41dfac62cc1'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_4a4b87d1a317433b89198f4418c6934e = Task(
        dag,
        task_id='ExecuteFar_4a4b87d1a317433b89198f4418c6934e',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_0c6a1b808c2143eda8de48c32123f450 = Task(
        dag,
        task_id='EvaluatePe_0c6a1b808c2143eda8de48c32123f450',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_4a4b87d1a317433b89198f4418c6934e', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223 = Task(
        dag,
        task_id='CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'gps_text': '49.067280, 18.481847', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    ExecuteFar_4a4b87d1a317433b89198f4418c6934e.set_upstream([globals()[t] for t in ['CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223']])
    EvaluatePe_0c6a1b808c2143eda8de48c32123f450.set_upstream([globals()[t] for t in ['ExecuteFar_4a4b87d1a317433b89198f4418c6934e', 'CreateIgni_30dd2f153cb54c61a4f492e1d1bf4223']])
