import boto3
import json
from datetime import datetime
import calendar

stream_name = 'mystream'

#Creating a kinesis client
client = boto3.client('kinesis')

#Sending range of dummy data to kinesis
for i in range(100):
    id = i
    timestamp = calendar.timegm(datetime.utcnow().timetuple())

    payload = {'id': str(id), 'timestamp': str(timestamp*1000)}

    print payload

    response = client.put_record(
        StreamName=stream_name,
        Data=json.dumps(payload),
        PartitionKey='1'
    )