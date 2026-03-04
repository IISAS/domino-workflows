from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-04T08:45:00', 'schedule': None, 'catchup': False, 'dag_id': '7ee6c855844a4ef08977267517e79f22'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    CreateIgni_f9d7877172064d1eb028708f821236b1 = Task(
        dag,
        task_id='CreateIgni_f9d7877172064d1eb028708f821236b1',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.34-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.34'},
        piece_input_kwargs={'gps_text': '49.06669261617986, 18.482122337861703', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()
    EvaluatePe_c7d726fb155a4c2bbef21951dc139fb5 = Task(
        dag,
        task_id='EvaluatePe_c7d726fb155a4c2bbef21951dc139fb5',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.34-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.34'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_24d69f359387419fb59f2d4c62b4d7cd', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_f9d7877172064d1eb028708f821236b1', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp', 'api_model_name': 'Model 2'}
    )()
    ExecuteFar_24d69f359387419fb59f2d4c62b4d7cd = Task(
        dag,
        task_id='ExecuteFar_24d69f359387419fb59f2d4c62b4d7cd',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.34-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.34'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_f9d7877172064d1eb028708f821236b1', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()

    EvaluatePe_c7d726fb155a4c2bbef21951dc139fb5.set_upstream([globals()[t] for t in ['CreateIgni_f9d7877172064d1eb028708f821236b1', 'ExecuteFar_24d69f359387419fb59f2d4c62b4d7cd']])
    ExecuteFar_24d69f359387419fb59f2d4c62b4d7cd.set_upstream([globals()[t] for t in ['CreateIgni_f9d7877172064d1eb028708f821236b1']])
