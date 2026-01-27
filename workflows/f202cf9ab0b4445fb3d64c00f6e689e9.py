from datetime import datetime
from dateutil.parser import parse
from airflow.sdk import DAG
from domino.task import Task

dag_config_0 = {'start_date': '2026-01-27T15:32:00', 'schedule': None, 'catchup': False, 'dag_id': 'f202cf9ab0b4445fb3d64c00f6e689e9'}

# Parse datetime values
dt_keys = ['start_date', 'end_date']
dag_config = { k: (v if k not in dt_keys else parse(v)) for k, v in dag_config_0.items()}
dag_config = {**dag_config, 'is_paused_upon_creation': False}

with DAG(**dag_config) as dag:
    YoutubeLis_3864b50a62f341a8a89e2af15421920d = Task(
        dag,
        task_id='YoutubeLis_3864b50a62f341a8a89e2af15421920d',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'YoutubeListVideosPiece', 'source_image': 'ghcr.io/tauffer-consulting/social_media_domino_pieces:0.5.4-group1', 'repository_url': 'https://github.com/Tauffer-Consulting/social_media_domino_pieces', 'repository_version': '0.5.4'},
        piece_input_kwargs={'channel_username': 'bbcnews', 'max_videos': 10, 'published_at_or_after': '2023-11-01', 'order_by': 'date', 'video_duration': 'short', 'return_only_urls': True}
    )()
    GetItemFro_6335e5bd838e4ab78784652a2ca1d061 = Task(
        dag,
        task_id='GetItemFro_6335e5bd838e4ab78784652a2ca1d061',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'GetItemFromArrayPiece', 'source_image': 'ghcr.io/tauffer-consulting/default_domino_pieces:0.8.1-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/default_domino_pieces', 'repository_version': '0.8.1'},
        piece_input_kwargs={'input_array': {'type': 'fromUpstream', 'upstream_task_id': 'YoutubeLis_3864b50a62f341a8a89e2af15421920d', 'output_arg': 'videos_list'}, 'index': 'first', 'another_index': 1}
    )()
    YoutubeDow_25e42c9d0a3c48148f3bb8ffc4fa60ed = Task(
        dag,
        task_id='YoutubeDow_25e42c9d0a3c48148f3bb8ffc4fa60ed',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'YoutubeDownloadPiece', 'source_image': 'ghcr.io/tauffer-consulting/social_media_domino_pieces:0.5.4-group1', 'repository_url': 'https://github.com/Tauffer-Consulting/social_media_domino_pieces', 'repository_version': '0.5.4'},
        piece_input_kwargs={'url': {'type': 'fromUpstream', 'upstream_task_id': 'GetItemFro_6335e5bd838e4ab78784652a2ca1d061', 'output_arg': 'output_value'}, 'output_type': 'audio'}
    )()
    AudioTrans_ccaf7bd318eb47d9bfff44ec70b316eb = Task(
        dag,
        task_id='AudioTrans_ccaf7bd318eb47d9bfff44ec70b316eb',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '512.0Mi'}, 'use_gpu': False},
        piece={'name': 'AudioTranscriptionPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.7.2-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/openai_domino_pieces', 'repository_version': '0.7.2'},
        piece_input_kwargs={'audio_file_path': {'type': 'fromUpstream', 'upstream_task_id': 'YoutubeDow_25e42c9d0a3c48148f3bb8ffc4fa60ed', 'output_arg': 'file_path'}, 'output_type': 'file', 'temperature': 0.1}
    )()
    TextSummar_834a26033d2944f89b92a891db4dc113 = Task(
        dag,
        task_id='TextSummar_834a26033d2944f89b92a891db4dc113',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'limits': {'cpu': '100.0m', 'memory': '128.0Mi'}, 'use_gpu': False},
        piece={'name': 'TextSummarizerPiece', 'source_image': 'ghcr.io/tauffer-consulting/openai_domino_pieces:0.7.2-group0', 'repository_url': 'https://github.com/Tauffer-Consulting/openai_domino_pieces', 'repository_version': '0.7.2'},
        piece_input_kwargs={'text_file_path': {'type': 'fromUpstream', 'upstream_task_id': 'AudioTrans_ccaf7bd318eb47d9bfff44ec70b316eb', 'output_arg': 'file_path_transcription_result'}, 'output_type': 'string', 'openai_model': 'gpt-3.5-turbo', 'chunk_size': 1000, 'chunk_overlap_rate': 0.2, 'completion_max_tokens': 500, 'temperature': 0.2}
    )()
    EmailSende_dc44dcf44dd543f7a5f684ea4ae5dcf9 = Task(
        dag,
        task_id='EmailSende_dc44dcf44dd543f7a5f684ea4ae5dcf9',
        workspace_id=1,
        workflow_shared_storage={'source': 'Local', 'mode': 'Read/Write', 'provider_options': {}},
        container_resources={'requests': {'cpu': '500.0m', 'memory': '200.0Mi'}, 'limits': {'cpu': '500.0m', 'memory': '200.0Mi'}, 'use_gpu': False},
        piece={'name': 'EmailSenderPiece', 'source_image': 'ghcr.io/tauffer-consulting/social_media_domino_pieces:0.5.4-group2', 'repository_url': 'https://github.com/Tauffer-Consulting/social_media_domino_pieces', 'repository_version': '0.5.4'},
        piece_input_kwargs={'email_provider': 'gmail', 'email_receivers': 'ja@ja.sk', 'email_subject': 'summary', 'email_body': {'type': 'fromUpstream', 'upstream_task_id': 'TextSummar_834a26033d2944f89b92a891db4dc113', 'output_arg': 'string_summarized_text'}}
    )()

    GetItemFro_6335e5bd838e4ab78784652a2ca1d061.set_upstream([globals()[t] for t in ['YoutubeLis_3864b50a62f341a8a89e2af15421920d']])
    YoutubeDow_25e42c9d0a3c48148f3bb8ffc4fa60ed.set_upstream([globals()[t] for t in ['GetItemFro_6335e5bd838e4ab78784652a2ca1d061']])
    AudioTrans_ccaf7bd318eb47d9bfff44ec70b316eb.set_upstream([globals()[t] for t in ['YoutubeDow_25e42c9d0a3c48148f3bb8ffc4fa60ed']])
    TextSummar_834a26033d2944f89b92a891db4dc113.set_upstream([globals()[t] for t in ['AudioTrans_ccaf7bd318eb47d9bfff44ec70b316eb']])
    EmailSende_dc44dcf44dd543f7a5f684ea4ae5dcf9.set_upstream([globals()[t] for t in ['TextSummar_834a26033d2944f89b92a891db4dc113']])
