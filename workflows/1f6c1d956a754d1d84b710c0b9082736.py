from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-12T09:11:00', 'schedule': None, 'catchup': False, 'dag_id': '1f6c1d956a754d1d84b710c0b9082736'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_4bb53c3d3d0a4db88e3c64d0a03d75f8 = Task(
        dag,
        task_id='ExecuteFar_4bb53c3d3d0a4db88e3c64d0a03d75f8',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.45-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.45'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_695e9fdbc6d447ef9d2af29efda16145', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_cb793075948b4283b387ce4cb38aae7b = Task(
        dag,
        task_id='EvaluatePe_cb793075948b4283b387ce4cb38aae7b',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.45-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.45'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_4bb53c3d3d0a4db88e3c64d0a03d75f8', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_695e9fdbc6d447ef9d2af29efda16145', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    CreateIgni_695e9fdbc6d447ef9d2af29efda16145 = Task(
        dag,
        task_id='CreateIgni_695e9fdbc6d447ef9d2af29efda16145',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.45-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.45'},
        piece_input_kwargs={'gps_text': '49.0654412799986, 18.48880967387001', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    ExecuteFar_4bb53c3d3d0a4db88e3c64d0a03d75f8.set_upstream([globals()[t] for t in ['CreateIgni_695e9fdbc6d447ef9d2af29efda16145']])
    EvaluatePe_cb793075948b4283b387ce4cb38aae7b.set_upstream([globals()[t] for t in ['CreateIgni_695e9fdbc6d447ef9d2af29efda16145', 'ExecuteFar_4bb53c3d3d0a4db88e3c64d0a03d75f8']])
