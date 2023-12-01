import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'

s3_service = boto3.client('s3',
                          aws_access_key_id=access_key,
                          aws_secret_access_key=secret_key,
                          region_name=region)

bucket_name = 'vkk-s3-bucket-01'
source_file_path = '/Users/vinod/Desktop/Backup/Amar Chitra Katha/503 -The Sons of Rama (gnv64).pdf'
destination_file_path = 'comics/ack/the_sons_of_rama.pdf'

try:
    s3_service.upload_file(source_file_path, bucket_name, destination_file_path)
    print('File uploaded successfully!')
except Exception as err:
    print(err)
