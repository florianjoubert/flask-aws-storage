import boto3
import os
from dotenv import load_dotenv
from pathlib import Path
import convertapi

load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv("ACCESS")
SECRET_KEY = os.getenv("SECRET")
CONVERT_SECRET = os.getenv("CONVERT")
convertapi.api_secret=CONVERT_SECRET
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

def convert_upload_files(file, format, bucket, folder):
    try:
        result=convertapi.convert('webp', {
            'File' : file,
            'ScaleImage': True,
            'ScaleProportions' : True,
            'ImageWidth' : 600,
            'FileName' : os.path.basename(os.path.splitext(file)[0])
        }, from_format = format).save_files(folder)
        try:
            upload_file(folder+'/'+os.path.basename(os.path.splitext(file)[0])+'.webp', bucket)
            os.remove(folder+'/'+os.path.basename(os.path.splitext(file)[0])+'.webp')
        except Exception as e:
            print(str(e))
    except Exception as e:
        print(str(e))
