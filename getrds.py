import boto3

client = boto3.client('rds')

response = client.describe_db_instances()

for y in response["DBInstances"]:
    print y["DBInstanceStatus"]


