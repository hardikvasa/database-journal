# https://pypi.org/project/PyMySQL/

import pymysql
import pymysql.cursors

# Establishing connection with the database
try:
    connection = pymysql.connect(host='<host>',
                                        user='<userName>',
                                        password='<password>')
    cursor = connection.cursor()
except:
    print("Connection error")


#Create database and select the dataabase for performing operations
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS countriesDB;")
    print("Database Created.")
    cursor.execute("USE countriesDB;")
except connection.Error as err:
    print(err)

# Creating a table 'countries'
try:
    TABLES = {}
    TABLES['countries'] = ("CREATE TABLE IF NOT EXISTS `countries` ("
                           "  `id` int(11) AUTO_INCREMENT,"
                           "  `Name` varchar(14) NOT NULL,"
                           "  `Population` int NOT NULL,"
                           "   PRIMARY KEY(id)"
                           ") ENGINE=InnoDB")

    table_description = TABLES['countries']
    cursor.execute(table_description)
    print("Table Created")
except connection.Error as err:
    print(err)


# Insert an item into the table
try:
    cursor.execute("INSERT INTO countries VALUES "
                   "(NULL, 'USA', 327000000),"
                   "(NULL, 'Germany', 82000000);"
                   )
    print("Item Inserted successfully.")
except connection.Error as err:
    print(err)


# Print Items
try:
    print("\nPrinting items...")
    cursor.execute("SELECT * FROM countries;")
    for item in cursor.fetchall():
        print(item)
except connection.Error as err:
    print(err)


# Deleting a table
try:
    cursor.execute("DROP TABLE countries;")
    print("\nTable delete successful.")
except connection.Error as err:
    print(err)

# Deleting the database
try:
    cursor.execute("DROP DATABASE IF EXISTS countriesDB;")
    print("Database delete successful.")
except connection.Error as err:
    print(err)

#Closing cursor and the connection
cursor.close()
connection.close()