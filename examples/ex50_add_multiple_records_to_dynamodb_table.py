import boto3

access_key = 'AKIARA6XTUWXVPECNB5U'
secret_key = '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'
region = 'us-east-1'
# access_key = 'AKIARFSHV4PN3XOHQASQ'
# secret_key = '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'
# region = 'us-east-1'

dynamodb_service = boto3.client('dynamodb',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name=region)

customers = [
    dict(cust_id='1001', children=None, married=True, name='John Doe', email='johndoe@xmpl.com', phone='9876512345', region='Texas'),
    dict(cust_id='1002', name='Ramesh Kumar', email='rameshkumar@xmpl.com', phone='9876512000', country='India'),
    dict(cust_id='1003', name='Jane Doe', phone='9876512222', city='Dallas')
]

try:
    table_name = 'customers_table'
    for each_customer in customers:
        dynamodb_service.put_item(
            TableName=table_name,
            Item={
                key: {'S': value}
                for key, value in each_customer.items()
            }
        )
        print(f'customer "{each_customer["name"]}" added to the {table_name}')

except Exception as err:
    print(err)
