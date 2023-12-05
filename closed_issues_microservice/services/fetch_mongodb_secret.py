from dotenv import load_dotenv
import os
import boto3
from botocore.exceptions import NoCredentialsError
import json

from utils.constants import db_secret

load_dotenv()

def configure_aws_credentials(access_key_id, secret_access_key, region):
    try:
        boto3.setup_default_session(
            aws_access_key_id=access_key_id,
            aws_secret_access_key=secret_access_key,
            region_name=region
        )
    except Exception as e:
        print(f"Error configuring AWS credentials: {e}")

def fetch_secret(access_key_id, secret_access_key, region_name, secret_name):
    try:
        session = boto3.session.Session()
        client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
        secret = get_secret_value_response['SecretString']
        return secret
    except NoCredentialsError as e:
        print(f"Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_secret():
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
    aws_region = os.getenv("AWS_REGION")
    configure_aws_credentials(aws_access_key_id, aws_secret_access_key, aws_region)
    secret_value = fetch_secret(aws_access_key_id, aws_secret_access_key, aws_region, db_secret)
    if secret_value:
        secret_json = json.loads(secret_value)
        return secret_json["database_url"]
    else:
        return str()