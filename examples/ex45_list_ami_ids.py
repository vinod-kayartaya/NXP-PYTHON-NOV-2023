import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'

ec2_service = boto3.client('ec2',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region)

try:
    response = ec2_service.describe_images(
        Owners=['amazon'],  # 'self', 'amazon', 'aws-marketplace'
        Filters=[
            {'Name': 'state', 'Values': ['available']},
            {'Name': 'architecture', 'Values': ['x86_64']},
        ]
    )
    print('List of available images: ')
    for each_image in response['Images']:
        print(f'{each_image["ImageId"]} --> {each_image["Name"]}')

except Exception as err:
    print(err)