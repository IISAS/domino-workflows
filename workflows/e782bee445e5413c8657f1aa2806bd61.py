from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-02-12T13:38:00', 'schedule': None, 'catchup': False, 'dag_id': 'e782bee445e5413c8657f1aa2806bd61'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    fve-9484ce6eb2154394b01f18fc40b3e044 = Task(
        dag,
        task_id='fve-9484ce6eb2154394b01f18fc40b3e044',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'FVEPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'fve_input_file'}, 'location': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'location'}}
    )()
    ciselniky-18d23783c24347bfa6b5de8bbb284c9e = Task(
        dag,
        task_id='ciselniky-18d23783c24347bfa6b5de8bbb284c9e',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'CiselnikyPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'ciselniky_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'ciselniky_input_file'}, 'location': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'location'}}
    )()
    meteo-0bbb21aa81fa40dba4f44ed007dadb5c = Task(
        dag,
        task_id='meteo-0bbb21aa81fa40dba4f44ed007dadb5c',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'MeteoPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'meteo_input_file'}, 'ciselniky_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'CiselnikyP_18d23783c24347bfa6b5de8bbb284c9e', 'output_arg': 'file_path'}}
    )()
    meteo_fve-c0394a59d04b4077950586b4cde0ef83 = Task(
        dag,
        task_id='meteo_fve-c0394a59d04b4077950586b4cde0ef83',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'Meteo_FVEPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'FVEPiece_9484ce6eb2154394b01f18fc40b3e044', 'output_arg': 'file_path'}, 'meteo_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'MeteoPiece_0bbb21aa81fa40dba4f44ed007dadb5c', 'output_arg': 'file_path'}}
    )()
    converttime-7395ecd902294a81bd5c01599143c5dc = Task(
        dag,
        task_id='converttime-7395ecd902294a81bd5c01599143c5dc',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'ConvertTimePiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'Meteo_FVEP_c0394a59d04b4077950586b4cde0ef83', 'output_arg': 'file_path'}}
    )()
    dayoftheyear-ee22a97f4ea4407bba97f0cc86aa17f7 = Task(
        dag,
        task_id='dayoftheyear-ee22a97f4ea4407bba97f0cc86aa17f7',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'DayOfTheYearPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'SelectDate_406b669fdaf942548b8de29c8dc0ac25', 'output_arg': 'file_path'}}
    )()
    minoftheday-f863af33291543808b275ab3d230aba2 = Task(
        dag,
        task_id='minoftheday-f863af33291543808b275ab3d230aba2',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'MinOfTheDayPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'DayOfTheYe_ee22a97f4ea4407bba97f0cc86aa17f7', 'output_arg': 'file_path'}}
    )()
    addsun-80771494b68644049262b415b3bd7d10 = Task(
        dag,
        task_id='addsun-80771494b68644049262b415b3bd7d10',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'AddSunPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'MinOfTheDa_f863af33291543808b275ab3d230aba2', 'output_arg': 'file_path'}, 'slnko_input_file': '/home/shared_storage/slnkoCasy2.csv'}
    )()
    isday-84b22525a81a4d0780fc735d64ca0fc0 = Task(
        dag,
        task_id='isday-84b22525a81a4d0780fc735d64ca0fc0',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'IsDayPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'AddSunPiec_80771494b68644049262b415b3bd7d10', 'output_arg': 'file_path'}}
    )()
    addadvancedmeteo-bd22d724a675439b8c4ecf1173eb0522 = Task(
        dag,
        task_id='addadvancedmeteo-bd22d724a675439b8c4ecf1173eb0522',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'AddAdvancedMeteoPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'IsDayPiece_84b22525a81a4d0780fc735d64ca0fc0', 'output_arg': 'file_path'}}
    )()
    renamecolumn-a61205e09c6a4686bdb6c956f1fcb9ac = Task(
        dag,
        task_id='renamecolumn-a61205e09c6a4686bdb6c956f1fcb9ac',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'RenameColumnPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'AddAdvance_bd22d724a675439b8c4ecf1173eb0522', 'output_arg': 'file_path'}, 'original_column_name': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'location'}, 'new_column_name': 'FVE'}
    )()
    removeunusedmeteo-8ae57055eb4e48a7ab45a0a4b0f84303 = Task(
        dag,
        task_id='removeunusedmeteo-8ae57055eb4e48a7ab45a0a4b0f84303',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'RemoveUnusedMeteoPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'meteo_fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'RenameColu_a61205e09c6a4686bdb6c956f1fcb9ac', 'output_arg': 'file_path'}}
    )()
    traintestsplit-fdb7e68571cf452dbbca9db0060fb594 = Task(
        dag,
        task_id='traintestsplit-fdb7e68571cf452dbbca9db0060fb594',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TrainTestSplitPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'data_path': {'type': 'fromUpstream', 'upstream_task_id': 'RemoveUnus_8ae57055eb4e48a7ab45a0a4b0f84303', 'output_arg': 'file_path'}, 'test_data_size': 0.2, 'random_state': 42, 'target_column': 'FVE'}
    )()
    trainrandomforestregressor-061d50d271844b3eaddc289a8c924295 = Task(
        dag,
        task_id='trainrandomforestregressor-061d50d271844b3eaddc289a8c924295',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TrainRandomForestRegressorPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'train_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'train_data_path'}, 'n_estimators': 100, 'criterion': 'squared_error', 'max_depth': None, 'bootstrap': True, 'oob_score': True, 'n_jobs': 1, 'random_state': 42, 'max_samples': None, 'target_column': 'FVE'}
    )()
    inferencemodel-8fd11a7c16064e009c06ba747943f8a5 = Task(
        dag,
        task_id='inferencemodel-8fd11a7c16064e009c06ba747943f8a5',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'InferenceModelPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'test_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'test_data_path'}, 'trained_model_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainRando_061d50d271844b3eaddc289a8c924295', 'output_arg': 'random_forest_model_path'}, 'target_column': 'FVE'}
    )()
    selectdates-406b669fdaf942548b8de29c8dc0ac25 = Task(
        dag,
        task_id='selectdates-406b669fdaf942548b8de29c8dc0ac25',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'SelectDatesPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'fve_input_file': {'type': 'fromUpstream', 'upstream_task_id': 'ConvertTim_7395ecd902294a81bd5c01599143c5dc', 'output_arg': 'file_path'}, 'date_start': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'date_start'}, 'date_end': {'type': 'fromUpstream', 'upstream_task_id': 'InputDataS_1fcd756720d940ee868717b17ef075ad', 'output_arg': 'date_end'}}
    )()
    trainrandomforestregressor-a173399b11ce41309ec7613a461224e5 = Task(
        dag,
        task_id='trainrandomforestregressor-a173399b11ce41309ec7613a461224e5',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TrainRandomForestRegressorPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'train_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'train_data_path'}, 'n_estimators': 50, 'criterion': 'squared_error', 'max_depth': None, 'bootstrap': True, 'oob_score': True, 'n_jobs': 1, 'random_state': 42, 'max_samples': None, 'target_column': 'FVE'}
    )()
    trainrandomforestregressor-193b7341fca046fdb6ac0aa6c1a8c62f = Task(
        dag,
        task_id='trainrandomforestregressor-193b7341fca046fdb6ac0aa6c1a8c62f',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TrainRandomForestRegressorPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'train_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'train_data_path'}, 'n_estimators': 80, 'criterion': 'squared_error', 'max_depth': None, 'bootstrap': True, 'oob_score': True, 'n_jobs': 1, 'random_state': 42, 'max_samples': None, 'target_column': 'FVE'}
    )()
    trainrandomforestregressor-12ee45f168d84a32b3f580e2f0a87704 = Task(
        dag,
        task_id='trainrandomforestregressor-12ee45f168d84a32b3f580e2f0a87704',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TrainRandomForestRegressorPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'train_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'train_data_path'}, 'n_estimators': 100, 'criterion': 'poisson', 'max_depth': None, 'bootstrap': True, 'oob_score': True, 'n_jobs': 1, 'random_state': 42, 'max_samples': None, 'target_column': 'FVE'}
    )()
    inferencemodel-b346a5037de24de3a5f451023ad524fd = Task(
        dag,
        task_id='inferencemodel-b346a5037de24de3a5f451023ad524fd',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'InferenceModelPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'test_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'test_data_path'}, 'trained_model_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainRando_193b7341fca046fdb6ac0aa6c1a8c62f', 'output_arg': 'random_forest_model_path'}, 'target_column': 'FVE'}
    )()
    inferencemodel-76297b55a58d462f81bc7f092eb357f2 = Task(
        dag,
        task_id='inferencemodel-76297b55a58d462f81bc7f092eb357f2',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'InferenceModelPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'test_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'test_data_path'}, 'trained_model_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainRando_a173399b11ce41309ec7613a461224e5', 'output_arg': 'random_forest_model_path'}, 'target_column': 'FVE'}
    )()
    inferencemodel-29db434976b0411ab9f2b9a8f0410779 = Task(
        dag,
        task_id='inferencemodel-29db434976b0411ab9f2b9a8f0410779',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'InferenceModelPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'test_data_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainTestS_fdb7e68571cf452dbbca9db0060fb594', 'output_arg': 'test_data_path'}, 'trained_model_path': {'type': 'fromUpstream', 'upstream_task_id': 'TrainRando_12ee45f168d84a32b3f580e2f0a87704', 'output_arg': 'random_forest_model_path'}, 'target_column': 'FVE'}
    )()
    inputdataseps-1fcd756720d940ee868717b17ef075ad = Task(
        dag,
        task_id='inputdataseps-1fcd756720d940ee868717b17ef075ad',
        workspace_id=4,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'InputDataSEPSPiece', 'source_image': 'ghcr.io/iisas/spice_domino_pieces:0.2.0-group0', 'repository_url': 'https://github.com/IISAS/spice_domino_pieces', 'repository_version': '0.2.0'},
        piece_input_kwargs={'fve_input_file': '/home/shared_storage/FVE_2021+2022upr.csv', 'location': 'Loc01', 'meteo_input_file': '/home/shared_storage/meteo_2021+2022upr.csv', 'ciselniky_input_file': '/home/shared_storage/lokality_FVE_ciselnik.csv', 'date_start': '2021-01-01', 'date_end': '2021-02-01'}
    )()

    fve-9484ce6eb2154394b01f18fc40b3e044.set_upstream([globals()[t] for t in ['inputdataseps-1fcd756720d940ee868717b17ef075ad']])
    ciselniky-18d23783c24347bfa6b5de8bbb284c9e.set_upstream([globals()[t] for t in ['inputdataseps-1fcd756720d940ee868717b17ef075ad']])
    meteo-0bbb21aa81fa40dba4f44ed007dadb5c.set_upstream([globals()[t] for t in ['ciselniky-18d23783c24347bfa6b5de8bbb284c9e', 'inputdataseps-1fcd756720d940ee868717b17ef075ad']])
    meteo_fve-c0394a59d04b4077950586b4cde0ef83.set_upstream([globals()[t] for t in ['meteo-0bbb21aa81fa40dba4f44ed007dadb5c', 'fve-9484ce6eb2154394b01f18fc40b3e044']])
    converttime-7395ecd902294a81bd5c01599143c5dc.set_upstream([globals()[t] for t in ['meteo_fve-c0394a59d04b4077950586b4cde0ef83']])
    dayoftheyear-ee22a97f4ea4407bba97f0cc86aa17f7.set_upstream([globals()[t] for t in ['selectdates-406b669fdaf942548b8de29c8dc0ac25']])
    minoftheday-f863af33291543808b275ab3d230aba2.set_upstream([globals()[t] for t in ['dayoftheyear-ee22a97f4ea4407bba97f0cc86aa17f7']])
    addsun-80771494b68644049262b415b3bd7d10.set_upstream([globals()[t] for t in ['minoftheday-f863af33291543808b275ab3d230aba2']])
    isday-84b22525a81a4d0780fc735d64ca0fc0.set_upstream([globals()[t] for t in ['addsun-80771494b68644049262b415b3bd7d10']])
    addadvancedmeteo-bd22d724a675439b8c4ecf1173eb0522.set_upstream([globals()[t] for t in ['isday-84b22525a81a4d0780fc735d64ca0fc0']])
    renamecolumn-a61205e09c6a4686bdb6c956f1fcb9ac.set_upstream([globals()[t] for t in ['addadvancedmeteo-bd22d724a675439b8c4ecf1173eb0522', 'inputdataseps-1fcd756720d940ee868717b17ef075ad']])
    removeunusedmeteo-8ae57055eb4e48a7ab45a0a4b0f84303.set_upstream([globals()[t] for t in ['renamecolumn-a61205e09c6a4686bdb6c956f1fcb9ac']])
    traintestsplit-fdb7e68571cf452dbbca9db0060fb594.set_upstream([globals()[t] for t in ['removeunusedmeteo-8ae57055eb4e48a7ab45a0a4b0f84303']])
    trainrandomforestregressor-061d50d271844b3eaddc289a8c924295.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    inferencemodel-8fd11a7c16064e009c06ba747943f8a5.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594', 'trainrandomforestregressor-061d50d271844b3eaddc289a8c924295']])
    selectdates-406b669fdaf942548b8de29c8dc0ac25.set_upstream([globals()[t] for t in ['converttime-7395ecd902294a81bd5c01599143c5dc', 'inputdataseps-1fcd756720d940ee868717b17ef075ad']])
    trainrandomforestregressor-a173399b11ce41309ec7613a461224e5.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    trainrandomforestregressor-193b7341fca046fdb6ac0aa6c1a8c62f.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    trainrandomforestregressor-12ee45f168d84a32b3f580e2f0a87704.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    inferencemodel-b346a5037de24de3a5f451023ad524fd.set_upstream([globals()[t] for t in ['trainrandomforestregressor-193b7341fca046fdb6ac0aa6c1a8c62f', 'traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    inferencemodel-76297b55a58d462f81bc7f092eb357f2.set_upstream([globals()[t] for t in ['trainrandomforestregressor-a173399b11ce41309ec7613a461224e5', 'traintestsplit-fdb7e68571cf452dbbca9db0060fb594']])
    inferencemodel-29db434976b0411ab9f2b9a8f0410779.set_upstream([globals()[t] for t in ['traintestsplit-fdb7e68571cf452dbbca9db0060fb594', 'trainrandomforestregressor-12ee45f168d84a32b3f580e2f0a87704']])
