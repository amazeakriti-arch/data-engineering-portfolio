import boto3
import json

lambda_client = boto3.client(
    'lambda',
    region_name='ap-south-1'
)

response = lambda_client.invoke(
    FunctionName='week5_s3_etl_lambda',
    InvocationType='RequestResponse',
    Payload=json.dumps({"source": "local_test"})
)

print(response['Payload'].read().decode())
