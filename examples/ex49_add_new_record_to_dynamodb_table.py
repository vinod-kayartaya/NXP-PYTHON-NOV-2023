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
    cust_id = input('Enter customer id: ')
    name = input('Enter name: ')
    email = input('Enter email address: ')
    phone = input('Enter phone: ')
    dynamodb_service.put_item(
        TableName=table_name,
        Item={
            'cust_id': {'S': cust_id},
            'name': {'S': name},
            'email': {'S': email},
            'phone': {'S': phone},
        }
    )
    print('New customer data added successfully!')
except Exception as err:
    print(err)
