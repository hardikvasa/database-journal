import sys
import logging
import pymysql

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Aurora configurations
rds_host  = "<rds endpoint without the port no.>"
name = "<master username>"
password = "<master password>"

try:
    connection = pymysql.connect(rds_host, user=name, passwd=password, connect_timeout=5)
    cursor = connection.cursor()
except Exception as e:
    logger.error(e)
    logger.error("ERROR: Unexpected error: Could not connect to Aurora instance.")
    sys.exit()

#Create database and select the dataabase for performing operations
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS countriesDB;")
    logger.info("Database Created.")
    cursor.execute("USE countriesDB;")
except connection.Error as err:
    logger.error(err)

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
    logger.info("Table Created")
except connection.Error as err:
    logger.error(err)


# Insert an item into the table
try:
    cursor.execute("INSERT INTO countries VALUES "
                   "(NULL, 'USA', 327000000),"
                   "(NULL, 'Germany', 82000000);"
                   )
    logger.info("Item Inserted successfully.")
except connection.Error as err:
    logger.error(err)


# Print Items
try:
    logger.info("\nPrinting items...")
    cursor.execute("SELECT * FROM countries;")
    for item in cursor.fetchall():
        print(item)
except connection.Error as err:
    logger.error(err)


# Deleting a table
try:
    cursor.execute("DROP TABLE countries;")
    logger.info("\nTable delete successful.")
except connection.Error as err:
    logger.error(err)

# Deleting the database
try:
    cursor.execute("DROP DATABASE IF EXISTS countriesDB;")
    logger.info("Database delete successful.")
except connection.Error as err:
    logger.error(err)

#Closing cursor and the connection
cursor.close()
connection.close()