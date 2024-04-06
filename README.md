# databaseGenerator
Project to explore using Faker and generating random test data in a MySQL database.

### The purpose of this project is to showcase and practice my learning of the following:
    + Creation of classes, methods and functions.
    + Connectivity to, and use of, relational database from within python.
    + Explore the use of Faker for creating test data for different languages.
    + Practice the analysis of data using SQL queries.

With dataGenerator.py you can create test tables and data for a database, which contains random name, address and email detail.  
The database platform is MySQL.
Data for a person includes: first name and last name and email address together with birthday date(year, month, day).

You can choose: how many records would you like to generate, county(Great Britain, United States of America, Ukraine, Spain and France) 
and name for your table in MySQL or by default name of the table is persons.
You can enter a name, password and database name or they will be named by default.
The database host to create a connection for MySQL can be entered, the default is the localhost.

You need to install modules from file importReqs.txt to successfully run this project.
dataGenerator.py contains the main code, that you need to run this project.
File uiChecks.py contains all functions and Classes, that you need to generate data for a person and to check the user input.

A number of SQL test queries are also provided to analyse the test data.
