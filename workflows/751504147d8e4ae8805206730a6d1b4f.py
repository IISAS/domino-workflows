from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-03-05T12:50:00', 'schedule': None, 'catchup': False, 'dag_id': '751504147d8e4ae8805206730a6d1b4f'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    ExecuteFar_1c75780c15ad470081b0575b7cb630e6 = Task(
        dag,
        task_id='ExecuteFar_1c75780c15ad470081b0575b7cb630e6',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ExecuteFarsitePiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group0', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'lcp_path': '/home/shared_storage/fire/final.lcp', 'inputs_path': '/home/shared_storage/fire/Zavada.input', 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd', 'output_arg': 'ignition_shp_path'}, 'barrier_shp_path': '0', 'output_basename': 'farsite_run', 'outputs_type': 1}
    )()
    EvaluatePe_5aa9b3fc41d2482594dc6c03407ec866 = Task(
        dag,
        task_id='EvaluatePe_5aa9b3fc41d2482594dc6c03407ec866',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '1024.0Mi'}, 'use_gpu': False},
        piece={'name': 'EvaluatePerimeterPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group1', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'outputs_zip_path': {'type': 'fromUpstream', 'upstream_task_id': 'ExecuteFar_1c75780c15ad470081b0575b7cb630e6', 'output_arg': 'outputs_zip_path'}, 'ignition_shp_path': {'type': 'fromUpstream', 'upstream_task_id': 'CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd', 'output_arg': 'ignition_shp_path'}, 'buffer_shp_path': '/home/shared_storage/fire/buffer.shp'}
    )()
    CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd = Task(
        dag,
        task_id='CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'CreateIgnitionPiece', 'source_image': 'ghcr.io/valaseklukas-svg/domino-farsite-pieces:0.1.43-group2', 'repository_url': 'https://github.com/valaseklukas-svg/domino-farsite-pieces', 'repository_version': '0.1.43'},
        piece_input_kwargs={'gps_text': '49.066, 18.490', 'lcp_path': '/home/shared_storage/fire/final.lcp'}
    )()

    ExecuteFar_1c75780c15ad470081b0575b7cb630e6.set_upstream([globals()[t] for t in ['CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd']])
    EvaluatePe_5aa9b3fc41d2482594dc6c03407ec866.set_upstream([globals()[t] for t in ['CreateIgni_de0c4e8dd0994d2aa18f850dfd97bebd', 'ExecuteFar_1c75780c15ad470081b0575b7cb630e6']])
