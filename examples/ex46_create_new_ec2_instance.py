import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'

ec2_service = boto3.client('ec2',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region)

try:
    response = ec2_service.run_instances(
        ImageId='ami-0fc5d935ebf8bc3bc',
        InstanceType='t2.micro',
        KeyName='vkk_kp_01',
        SecurityGroupIds=['vkk_security_group_01'],
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'my first ubuntu ec2'},
                    {'Key': 'Env', 'Value': 'dev'}
                ]
            }
        ]
    )
    new_instance_id = response['Instances'][0]['InstanceId']
    print(f'New EC2 instance created successfully. Instance id - {new_instance_id}')
except Exception as err:
    print(err)
