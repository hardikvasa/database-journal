import pymongo
import sys

#Create a MongoDB client
client = pymongo.MongoClient('<host,for e.g. 127.0.0.1:27017>') 

#Specifying the database to be used
mydb = client.test

#Creating collection (table equivalent)
mycollection = mydb.myTestCollection

#Inserting a record into the collection
mycollection.insert_one({'name':'Andrew'})

#Finding a record and printing it
x = mycollection.find_one({'name':'Andrew'})
print(x)

#Closing the connection
client.close()