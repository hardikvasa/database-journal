#brew install postgresql, pip install psycopg2
import psycopg2
try:
    connection = psycopg2.connect(user = "<username>",
                                  password = "<password>",
                                  host = "<host for example, 127.0.0.1>",
                                  port = "5432",
                                  database = "<dbName>")
    cursor = connection.cursor()
except (Exception, psycopg2.Error) as error :
    print ("Error connecting to PostgreSQL database", error)


# Insert an item into the table
try:
    cursor.execute("INSERT INTO dbName VALUES "
                   "(NULL, 'USA', 327000000),"
                   "(NULL, 'Germany', 82000000);"
                   )
    connection.commit()
    print("Item Inserted successfully.")
except connection.Error as err:
    print(err)

# Print Items
try:
    print("\nPrinting items...")
    cursor.execute("SELECT * FROM dbName;")
    connection.commit()
    for item in cursor.fetchall():
        print(item)
except connection.Error as err:
    print(err)

cursor.close()
connection.close()
print("PostgreSQL connection is closed")