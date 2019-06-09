import boto3
import time

epoch_time = epoch_time = int(time.time())

client = boto3.client('dynamodb')

#Create a DynamoDB table
response = client.create_table(
    TableName='customers',
    AttributeDefinitions=[
        #setting username as primary key (unique key)
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Creating table... " + str(response))
print("\nWaiting 15 seconds for the the table to be created...")
time.sleep(15)

#put item in the table
put_item = client.put_item(
    TableName='customers',
    Item={
        'username':
            {
                'S':'john123'
            },
        'time_stamp':
            {
                'S': str(epoch_time)
            },
        'first_name':
            {
                'S':'John'
            },
        'last_name':
            {
                'S':'Gates'
            },
    },
)
print(put_item)

#get item from the table
get_item = client.get_item(
    TableName='customers',
    Key={
        'username':
            {
                'S':'john123'
            },
    }
)
print("\nGetting the item..." + str(get_item))

#delete table
delete_item = client.delete_item(
    TableName='customers',
    Key={
        'username':
            {
                'S':'john123'
            }
    }
)
print("\nDeleting the item..." + str(delete_item))

#delete table
delete_table = client.delete_table(
    TableName='customers'
)
print("\nDeleting the table..." + str(delete_table))