import boto3
import time

stream_name = 'mystream'

#Creating a kinesis client
client = boto3.client('kinesis')

#Getting shard id by describing the stream
response = client.describe_stream(StreamName=stream_name)
shard_id = response['StreamDescription']['Shards'][1]['ShardId']

#getting the shard iterator (pointer) value
shard_iterator = client.get_shard_iterator(StreamName=stream_name,
                                                      ShardId=shard_id,
                                                      ShardIteratorType='TRIM_HORIZON')

stream_shard_iterator = shard_iterator['ShardIterator']

#Getting records from the stream
response = client.get_records(ShardIterator=stream_shard_iterator, Limit=1)

#looping infinitely to get records instantly
#limit can be set from 1-10,000
while True:
    response = client.get_records(
        ShardIterator=response['NextShardIterator'],
        Limit=1
    )
    print response
    #making sure we are not getting throttled by kinesis
    time.sleep(0.5)