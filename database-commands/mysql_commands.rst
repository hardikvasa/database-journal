=====================
MySQL Sample Commands
=====================

Sample database can be found in the `sql` directory of this repository. You can install xampp software to run Apache and MySQL server on your machine.


Show all the existing databases

.. code-block:: sql
   
   SHOW DATABASES;


Create Database testDB if it does not exist

.. code-block:: sql
   
   CREATE DATABASE testDB IF NOT EXISTS;


Delete Database testDB if it exists

.. code-block:: sql
   
   DROP DATABASE IF EXISTS testDB;


Begin using the database name testDB

.. code-block:: sql
   
   USE testDB;


Show system status

.. code-block:: sql
   
   SHOW STATUS;


Show MySQL environment variables

.. code-block:: sql
   
   SHOW VARIABLES;


Select all the records (rows) from Country table

.. code-block:: sql

   SELECT * 
   FROM Country


Select specific columns from the Country table

.. code-block:: sql

   SELECT Name, Code, Population
   FROM Country


Create Alias (alternate names) a column

.. code-block:: sql
   
   SELECT Name AS 'country-name', Population as 'country-population'
   FROM Country;


Order the rows by Name column in ascending order

.. code-block:: sql
   
   SELECT * 
   FROM Country 
   ORDER BY Name ASC;


Order the rows by Name column in descending order

.. code-block:: sql
   
   SELECT * 
   FROM Country 
   ORDER BY Name DESC;


First order by Continent and then Name within each Continent

.. code-block:: sql
   
   SELECT Name, Continent 
   FROM Country 
   ORDER BY Continent, Name DESC;


Order by content name in descending order and then name in ascending order

.. code-block:: sql
   
   SELECT Name, Continent 
   FROM Country 
   ORDER BY Continent DESC, Name;


Limit clause to limit the number of rows returned

.. code-block:: sql
   
   SELECT * 
   FROM Country 
   LIMIT 5;

Offset

.. code-block:: sql
   
   SELECT * 
   FROM Country 
   ORDER BY Name 
   LIMIT 5 OFFSET 5;

Where clause

.. code-block:: sql
   
   SELECT Name, Code, Population 
   FROM Country 
   WHERE Population > 100000000 
   ORDER BY Population;

Null clause

.. code-block:: sql
   
   SELECT Name, Code, Population 
   FROM Country  
   WHERE Population > 100000000 OR Population IS NULL
   ORDER BY Population;


OR clause

.. code-block:: sql
   
   SELECT Name, Code, Population 
   FROM Country 
   WHERE Population > 100000000 OR Population IS NULL
   ORDER BY Population;


NOT Null clause

.. code-block:: sql
   
   SELECT Name, Code, Population 
   FROM Country 
   WHERE Population > 100000000 OR Population IS NOT NULL
   ORDER BY Population;


AND clause

.. code-block:: sql
   
   SELECT Name, Code, Population 
   FROM Country 
   WHERE Population > 100000000 AND Continent = 'Asia'
   ORDER BY Population;

Where clause with string match

.. code-block:: sql
   
   SELECT Name, Code 
   FROM Country 
   WHERE Code = 'USA’;


Like clause

.. code-block:: sql
   
   SELECT Name, Continent, Population 
   FROM Country 
   WHERE Name LIKE 'ind%’;


Like clause with single character

.. code-block:: sql
   
   SELECT Name, Continent, Population 
   FROM Country 
   WHERE Name LIKE ‘_a%’;


IN clause

.. code-block:: sql
   
   SELECT Name, Continent, Population 
   FROM Country
   WHERE Continent IN ('Asia', 'Europe')
   ORDER BY Continent;


Regex

.. code-block:: sql
   
   SELECT Name, Continent, Population 
   FROM Country 
   WHERE Name REGEXP '^.[a-d].*’;


Create table

.. code-block:: sql
   
   CREATE TABLE test (a INT, b TEXT, C TEXT);

Insert row 

.. code-block:: sql
   
   INSERT INTO test 
   VALUES (1, 'First Value’, ’Second Value');


Insert row specifying the columns

.. code-block:: sql
   
   INSERT INTO test 
   (a,b) VALUES (1, 'First Value')


Insert row by Selecting rows from other table

.. code-block:: sql
   
   INSERT INTO test 
   (a, b, c)
   SELECT id, name, description FROM item;

Updating a row

.. code-block:: sql
   
   UPDATE test 
   SET c = ’Something else’
   WHERE a = 1;


Delete a row with only its first occurrance

.. code-block:: sql
   
   DELETE
   FROM test
   WHERE a = 1
   LIMIT 1;
   SELECT * FROM test;


Delete a table

.. code-block:: sql
   
   DROP TABLE test;


Describe table <— MySQL specific

.. code-block:: sql
   
   DESCRIBE test;


Verbose table structure

.. code-block:: sql
   
   SHOW TABLE STATUS;


Index while creating table

.. code-block:: sql
   
   INDEX(a);


Show index

.. code-block:: sql
   
   SHOW INDEXES FROM test;


Modify the table at a later stage

.. code-block:: sql
   
   ALTER TABLE test 
   ADD d VARCHAR(10);

Remove a column

.. code-block:: sql
   
   ALTER TABLE test 
   DROP d;

Add a column with more options

.. code-block:: sql
   
   ALTER TABLE test 
   ADD d VARCHAR(10) 
   AFTER a 
   DEFAULT ’something’;


Timezone

.. code-block:: sql
   
   SHOW VARIABLES LIKE ‘%time_zone%’;
	SELECT NOW()
	SET TIMEZONE = ‘US/Eastern’


String functions - Length of a value <— counts the bytes

.. code-block:: sql
   
   SELECT Name, LocalName, Length(LocalName) AS len 
   FROM Country 
   WHERE Continent = 'Europe' 
   ORDER BY len;

CHAR_LENGTH counts characters


Left 3 characters (similarly for Right and Mid):

.. code-block:: sql
   
   Left(Name, 3)


Concatenation

.. code-block:: sql
   
   CONCAT(Name, LocalName)


Char position

.. code-block:: sql
   
   LOCATE(’string’, ‘bigString’)

Case

.. code-block:: sql
   
   UPPER(Name) or LOWER(Name)


Reverse a string

.. code-block:: sql
   
   REVERSE(Name)


Algebra

.. code-block:: sql
   
   SELECT 5+5;


Others

.. code-block:: sql
   
   POWER(2,3), ABS(-5), SIGN, CONV (to convert base), ROUND, TRUNCATE, RAND


Date and Time

.. code-block:: sql
   
   NOW(), UNIX_TIMESTAMP(), DAYOFMONTH, MONTHNAME


GROUP BY

.. code-block:: sql
   
   SELECT Continent, COUNT(*) as Count 
   FROM Country 
   GROUP BY Continent 
   ORDER BY Count DESC;


Scan the table and get the count of distinct values

.. code-block:: sql
   
   COUNT(DISTINCT NAME)


Maintaining the integrity of database

.. code-block:: sql
   
   COMIT and ROLLBACK


TRIGGER

.. code-block:: sql
   
   CREATE TRIGGER …


SELECT statement to be used as data for another SELECT statement

.. code-block:: sql
   
   SUBSELECT


View if you would want to use a query multiple times

.. code-block:: sql
   
   CREATE VIEW viewName


Check the current user

.. code-block:: sql
   
   SELECT USER();


Show all the users, hosts and passwords

.. code-block::sql
   
   SELECT User,Host,Password FROM mysql.user;


Create user

.. code-block::sql

   CREATE USER '<userName>'@'localhost' IDENTIFIED BY '<userPassword>';


Delete user

.. code-block::sql
   
   DROP USER <userName>;


Grant all permissions to a user

.. code-block::sql
   
   GRANT ALL PRIVILEGES 
   ON *.* TO '<username>'@'localhost';


Grant some select permissions to a user

.. code-block::sql
   
   GRANT SELECT,UPDATE,INSERT,DELETE 
   ON <database_name>.* TO '<username>'@'localhost';


Export everything to a .csv file

.. code-block::sql
   
   SELECT *
   FROM <table_name>
   INTO OUTFILE 'database.csv'
   FIELDS TERMINATED BY ','
   ENCLOSED BY '"'
   LINES TERMINATED BY '\n';


Inspired by `MySQL Essential Training <https://www.lynda.com/MySQL-tutorials/MySQL-Essential-Training/139986-2.html?srchtrk=index%3a3%0alinktypeid%3a2%0aq%3amysql+%0apage%3a1%0as%3arelevance%0asa%3atrue%0aproducttypeid%3a2>`__
