======================
MongoDB shell commands
======================

Installing MongoDB on linux/mac

.. code-block:: bash
   
   brew install mongodb


Running the mongodb server

.. code-block:: bash
   
   brew services start mongodb


Stop the mongodb server

.. code-block:: bash
   
   brew services stop mongodb


Starting the mongodb shell in the terminal

.. code-block:: bash
   
   mongo --host localhost:27017


Check server status and connection

.. code-block:: bash
   
   db.serverStatus()


Create a database and use it

.. code-block:: bash

	use testDatabase


Create a collection (table)

.. code-block:: bash

	db.createCollection("testCollection")


Insert one document in the collection

.. code-block:: bash

	db.testCollection.insert({"city": "San Fransisco", "population": "884363", "state": "California"})


Insert multiple documents in the database

.. code-block:: bash

	db.testCollection.insert([{"city": "San Fransisco", "population": "884363", "state": "California"},{"city": "Seattle", "population": "724745", "state": "Washington"},{"city": "Portland", "population": "647805", "state": "Oregon"}])


List all the records in the collection

.. code-block:: bash

	db.testCollection.find()


Search for a specific record

.. code-block:: bash

	db.user.find({"city": "Seattle"})


Show all the databases on the server

.. code-block:: bash

	show dbs


Show all the collections on the server

.. code-block:: bash

	show collections


Delete a collection

.. code-block:: bash

	db.testCollection.drop()


Show the total size of the collection

.. code-block:: bash

	db.testColection.dataSize()


Exporting a collection

.. code-block:: bash

	mongoexport --db testDatabase --collection testCollection --out db.json


Delete current database

.. code-block:: bash

	db.dropDatabase();


Show all the users

.. code-block:: bash

	show users


Create a new user

.. code-block:: bash

	db.createUser({"user": "testUser", "pwd": "testPassword", "roles": ["readWrite"]})


Log into the database using user credentials

.. code-block:: bash

	mongo -u testUser -p testPassword --authenticationDatabase testDatabase


Delete a user

.. code-block:: bash

	db.dropUser("testUser")


Importing a collection

.. code-block:: bash

	mongoimport --db testDatabase --collection testCollection < path/to/db.json