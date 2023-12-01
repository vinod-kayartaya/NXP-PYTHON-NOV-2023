import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'


s3_service = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          region_name=region)

bucket_name = 'vkk-s3-bucket-01'
try:
    response = s3_service.list_objects_v2(Bucket=bucket_name)

    for index, each_object in enumerate(response['Contents']):
        print(f'{index + 1}. {each_object["Key"]}')
except Exception as err:
    print(err)
