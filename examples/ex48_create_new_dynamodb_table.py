import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'

dynamodb_service = boto3.client('dynamodb',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region)

try:
    table_name = 'customers_table'
    dynamodb_service.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'cust_id', 'KeyType': 'HASH'}
        ],
        AttributeDefinitions=[
            {'AttributeName': 'cust_id', 'AttributeType': 'S'}
        ],
        ProvisionedThroughput={'ReadCapacityUnits': 5, 'WriteCapacityUnits': 5},
    )
    print(f'Table {table_name} created successfully!')
except Exception as err:
    print(err)
