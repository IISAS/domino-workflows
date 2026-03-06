from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-06T10:58:00', 'schedule': None, 'catchup': False, 'dag_id': '0e45e5eb5a674e37b80cbb2ae8eb0745'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_53095dbe9eba4eeca733f42937b41726 = Task(
        dag,
        task_id='ExecuteFar_53095dbe9eba4eeca733f42937b41726',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.44-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.44'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_64b32b44ff6b45e48065e2cd020c190a', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_8566704d0487451681cac72e7493f2b9 = Task(
        dag,
        task_id='EvaluatePe_8566704d0487451681cac72e7493f2b9',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.44-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.44'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_53095dbe9eba4eeca733f42937b41726', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_64b32b44ff6b45e48065e2cd020c190a', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    CreateIgni_64b32b44ff6b45e48065e2cd020c190a = Task(
        dag,
        task_id='CreateIgni_64b32b44ff6b45e48065e2cd020c190a',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.44-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.44'},
        piece_input_kwargs={'gps_text': '49.068034, 18.490261', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    ExecuteFar_53095dbe9eba4eeca733f42937b41726.set_upstream([globals()[t] for t in ['CreateIgni_64b32b44ff6b45e48065e2cd020c190a']])
    EvaluatePe_8566704d0487451681cac72e7493f2b9.set_upstream([globals()[t] for t in ['ExecuteFar_53095dbe9eba4eeca733f42937b41726', 'CreateIgni_64b32b44ff6b45e48065e2cd020c190a']])
