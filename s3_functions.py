import boto3
import json
import os
from dotenv import load_dotenv
from pathlib import Path
import convertapi
from werkzeug.utils import secure_filename
import requests
import base64


load_dotenv()
env_path = Path('.')/'.env'
load_dotenv(dotenv_path=env_path)

ACCESS_KEY = os.getenv("ACCESS")
SECRET_KEY = os.getenv("SECRET")
CONVERT_SECRET = os.getenv("CONVERT")
ENDPOINT = "https://wojo.s3.naitways.net/preprod/"
convertapi.api_secret=CONVERT_SECRET
s3_client = boto3.client(
    's3',
    endpoint_url ='https://wojo.s3.naitways.net',
    aws_access_key_id = ACCESS_KEY,
    aws_secret_access_key = SECRET_KEY
)

def delete_file(file_name, bucket):
    response = s3_client.delete_object(Bucket = bucket, Key = file_name)
    return response

def upload_file(file,filename, bucket, acl="public-read"):
    """
    Function to upload a file to an S3 bucket
    """
    response = s3_client.put_object(
            Body = file,
            Bucket = bucket,
            Key = filename,
            ACL = acl,
            ContentType = "image/webp"
        )
    return response

def upload_file_to_s3(file,bucket, acl="public-read"):
    filename = secure_filename(file.filename).replace(" ","_")
    try:
        s3_client.upload_fileobj(
            file,
            bucket,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        # This is a catch all exception, edit this part to fit your needs.
        print("Something Happened: ", e)
        return e
    
    # after upload file to s3 bucket, return filename of the uploaded file
    return filename

def list_files_v2(bucket):
    contents = []
    ## Tri par date décroissante
    for item in sorted(s3_client.list_objects_v2(Bucket=bucket)['Contents'],key=lambda x: x['LastModified'], reverse=True):
        contents.append(item)
    return contents

def convert_upload_files(file, format, bucket):
    # on upload image to s3
    # on convertit l'image uploadé
    # on supprime l'image de s3
    # on reupload nouvelle image
    # c'est degueu mais convertapi il aime pas les filestorage l'enf
    filename = secure_filename(file.filename).replace(" ", "_")

    ## ETAPE 1 on upload l'image 
    upload_file_to_s3(file, bucket)
    urlImage = ENDPOINT + filename

    ## ETAPE 2 on convertit l'image
    print("url =  "+urlImage)
    try:
        result=convertapi.convert('webp', {
            'File' : urlImage,
            'ScaleImage': True,
            'ScaleProportions' : True,
            'ImageWidth' : 600,
            'FileName' : os.path.basename(os.path.splitext(filename)[0]),
            'StoreFile' : True
        }, from_format = format)
        try:
            response = result.__dict__
            url = response.get('response').get('Files')[0].get('Url')
            req_for_image = base64.b64encode(requests.get(url).content)
            upload_file(base64.decodebytes(req_for_image), os.path.basename(url), bucket)
        except Exception as e:
            print(str(e))
    except Exception as e:
        print("PB: "+str(e))


    ## ETAPE 3 on upload nouvelle image
    delete_file(filename, bucket)
    return "ok"
   
#delete_file('sdsdsdsd.png', 'preprod')