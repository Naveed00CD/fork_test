import json
import boto3

def lambda_handler(event, context):
  client = boto3.client('ec2')
  response = client.run_instances(
    ImageId='ami-0614680123427b75e',
    InstanceType='t2.micro',
    KeyName='from ec_2 8:54 test 2',
    MaxCount=2,
    MinCount=2
)

