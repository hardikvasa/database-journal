#pip install redis
#brew install redis
#brew services start redis

import redis

#configurations
redis_host = "localhost"
redis_port = 6379
redis_password = ""

try:

    #creating a redis client
    client = redis.Redis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)

    #writing data to redis cluster
    client.set("msg:name", "{'name','John'}")
    print('Data written to cache...')

    #retrieve data from cluster
    message = client.get("msg:name")
    print("Result: " + message)

except Exception as e:
    print(e)
