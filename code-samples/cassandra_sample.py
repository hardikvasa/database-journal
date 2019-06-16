"""
$ brew install cassandra
$ pip install cassandra-driver
$ pip install cqlsh
$ cassandra -f #Run cassandra node
"""

import logging
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement
import time

cluster = Cluster(['localhost'])
session = cluster.connect()
print(session)
time.sleep(0.1)

keyspace = "test"
keyspaces = []

for item in cluster.metadata.keyspaces: keyspaces.append(item)
print(keyspaces)
if keyspace in keyspaces:
    session.execute("DROP KEYSPACE " + keyspace)
    print('keyspace dropped...')
time.sleep(0.5)

create =  session.execute("""
                CREATE KEYSPACE %s
                WITH replication = { 'class': 'SimpleStrategy', 'replication_factor': '1' }
                """ % keyspace)
print("Keyspace created...")

#using the keyspace
session.set_keyspace(keyspace)

#Creating a table
c_sql = """ CREATE TABLE IF NOT EXISTS users (emp_id int PRIMARY KEY,
                                              name varchar,
                                              age double,
                                              city varchar); """
session.execute(c_sql)
print("Table created...")

#Inserting item into the table
insert_sql = session.prepare("INSERT INTO  users (emp_id, name, age, city) VALUES (?,?,?,?)")
batch = BatchStatement()
batch.add(insert_sql, (1, 'Mike', 29, 'Seattle'))
batch.add(insert_sql, (2, 'Jenny', 25, 'Seattle'))
batch.add(insert_sql, (3, 'Henry', 31, 'Portland'))
batch.add(insert_sql, (4, 'Yandall', 42, 'Portland'))
session.execute(batch)
print("Items inserted into table...")

#getting top three records from the user table
rows = session.execute('select * from users limit 3;')
for row in rows:
    print(row.name, row.age)

#Drop (delete) the table
delete_table = session.execute('DROP TABLE users;')
print('Table deleted...')

#Drop (delete) the keyspace (database)
delete_keyspace = session.execute('DROP KEYSPACE %s;' % keyspace)
print('Keyspace deleted...')
