from elasticsearch import Elasticsearch
import time
import json

es = Elasticsearch(['<host:port>'])
print(es)

#Create index
if es.indices.exists(index='customer'):
    es.indices.delete(index='customer')

create_index = es.indices.create(
    index='customer',
    body={
        "settings" : {
            "index" : {
                "number_of_shards" : 5,
                "number_of_replicas" : 0
            }
        },
        "mappings": {
            "customer" : {
                "properties" : {
                    "username": { "type" : "text"},
                    "first_name" : { "type" : "text"},
                    "last_name" : { "type" : "text"},
                    "time_epoch" : { "type" : "long" }
                }
            }
        }
    },
    ignore=400)
print(create_index)

#Adding a document to the index
record1={
    "username":"john123",
    "first_name":"Henry",
    "last_name":"Gates",
    "time_epoch": int(time.time())
}

record2={
    "username":"billg",
    "first_name":"Bill",
    "last_name":"Gates",
    "time_epoch": int(time.time())
}

put_record_1 = es.index(index='customer',doc_type='customer',id=1,body=record1)
put_record_2 = es.index(index='customer',doc_type='customer',id=2,body=record2)
print(put_record_1,put_record_2)

#Get document by id
print("\n\n")
abc = es.get(index='customer',doc_type='customer',id=1)
print(abc['_source'])

#Search document with first_name
print("\n\n")
time.sleep(1)
res = es.search(index='customer', body={'query':{'match':{'first_name':'Bill'}}})
print("%d documents found" % res['hits']['total'])
for doc in res['hits']['hits']:
    print(json.dumps(doc['_source'], indent=4, sort_keys=True))
