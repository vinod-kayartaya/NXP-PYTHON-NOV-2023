import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'

ec2_service = boto3.client('ec2',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region)

try:
    response = ec2_service.stop_instances(
        InstanceIds=['i-049c9fb34ebe6d610'],
        Force=True)
    print('EC2 instance stopped!')
except Exception as err:
    print(err)
