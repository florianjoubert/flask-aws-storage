import boto3
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv("ACCESS")
SECRET_KEY = os.getenv("SECRET")
s3_client = boto3.client(
    's3',
    endpoint_url ='https://wojo.s3.naitways.net',
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY
)

def upload_file(file_name, bucket):
    object_name = os.path.basename(file_name)
    response = s3_client.upload_file(file_name, bucket, object_name)
    return response

def list_files_v2(bucket):
    contents = []
    ## Tri par date décroissante
    for item in sorted(s3_client.list_objects_v2(Bucket=bucket)['Contents'],key=lambda x: x['LastModified'], reverse=True):
        contents.append(item)
    return contents