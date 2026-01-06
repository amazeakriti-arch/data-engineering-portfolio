import boto3
import urllib.parse

s3 = boto3.client("s3")

def lambda_handler(event, context):
    print("S3 EVENT RECEIVED:", event)

    record = event["Records"][0]

    bucket_name = record["s3"]["bucket"]["name"]
    object_key = urllib.parse.unquote_plus(
        record["s3"]["object"]["key"]
    )

    print(f"Bucket: {bucket_name}")
    print(f"Key: {object_key}")

    # Read file
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    content = response["Body"].read().decode("utf-8")

    print("File content:")
    print(content)
    print("Lambda got Triggered!!!")
    # Example output
    s3.put_object(
        Bucket=bucket_name,
        Key="output/output.txt",
        Body=content.upper()
    )

    return {
        "statusCode": 200,
        "message": "ETL completed successfully"
    }
