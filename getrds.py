import boto3

client = boto3.client('rds',"ap-northeast-1")

response = client.describe_db_instances()

for y in response["DBInstances"]:
    print y["DBInstanceStatus"]


