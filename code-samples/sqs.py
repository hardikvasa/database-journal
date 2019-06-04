import boto3
import time

# Creating an SQS client
client = boto3.client('sqs')

# Creating a queue
try:
    response = client.create_queue(
        QueueName='testQueue'
    )
    time.sleep(2)
    print("Queue Created")
except Exception as e:
    print(e)


#Sending a message to the queue
try:
    #getting the queue url from the queue name
    queue_url = client.get_queue_url(
        QueueName='testQueue'
    )
    url = queue_url['QueueUrl']
    response = client.send_message(
        QueueUrl=url, MessageBody='testMessage'
    )
    time.sleep(2)
    print("Message sent successful")
except Exception as e:
    print(e)


#Receiving a message to the queue
try:
    receive_response = client.receive_message(
        QueueUrl=url,
        AttributeNames=['All'],
        WaitTimeSeconds=20
        )
    print("Message received: " + receive_response['Messages'][0]['Body']
          + " - Message ID: " + receive_response['Messages'][0]['MessageId'])
except Exception as e:
    print(e)


#Deleting a message
try:
    response = client.delete_message(
        QueueUrl=url,
        ReceiptHandle=receive_response['Messages'][0]['ReceiptHandle']
    )
    print("Message Deleted")
except Exception as e:
    print(e)


#Deleting the queue
try:
    delete_response = client.delete_queue(
        QueueUrl=url
    )
    print("Queue delete successful")
except Exception as e:
    print(e)