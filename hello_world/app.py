import json
import boto3
from random import random
import os
from botocore.config import Config
# import requests


def lambda_handler(event, context):
    # S3 client 생성
    # s3 = boto3.client('s3')
    s3 = boto3.client('s3', config=Config(signature_version='s3v4'), region_name='ap-northeast-2')
    img_id = int(random() * 10000000)

    s3Params = {
        'Bucket': os.environ.get("UPLOAD_BUCKET"),
        'Key': '{}.jpg'.format(img_id),
        'ExpiresIn': os.environ.get("URL_EXPIRE_SECONDS"),
    }
    # presigned_post = s3.generate_presigned_post(ClientMethod='POST', Params=s3Params)
    presigned_post = s3.generate_presigned_post(
        Bucket=os.environ.get("UPLOAD_BUCKET"),
        Key='{}.jpg'.format(img_id),
        ExpiresIn=os.environ.get("URL_EXPIRE_SECONDS")
    )
    print(presigned_post)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }
