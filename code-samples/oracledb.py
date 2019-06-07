import cx_Oracle 

# Create a table in Oracle database 
try: 
	#Creating a connection
	connection = cx_Oracle.connect("<userName>", "<password>", "<host>/<service>") 
	
	#Creating a cursor object
	cursor = connection.cursor() 
	
	#Querying a table and getting two columns - firstName and lastName 
	cursor.execute("SELECT firstName, lastName FROM myTable") 
					
	for firstName, lastName in cursor:
    	print("Values: ", firstName, lastName)
	
except cx_Oracle.DatabaseError as e: 
	print("There is a problem with Oracle", e) 

finally: 
	cursor.close() 
	connection.close() 
