import sys
import mysql.connector
from mysql.connector import errorcode
from faker import Faker
from uiChecks import check_country_input, check_user_input, check_table_input, resolve_locale, Address, Person

"""
This program creates test data using faker and inserts into a database table.
Purpose is to demonstrate interaction with the database and with Faker.

Features:
    Classes for principle objects defined in uichecks.py
    Functions for validation user input also defined in uichecks.py

Start of pseudocode:
    Prompt the user for the following information with default options:
        Database connection credentials (username, password etc).
        Number of records to create.
        Menu of countries to create data for.
        Table name to use/create.
        
    Connect to database.
    Set country locale for Faker.
    Create table in MySQL is it does not exist.
    loop:
        Use class methods populate test data using faker.
        Insert data into MySQL table.
End of pseudocode.
"""

# Prompt the user for database connection credentials.
user_name = input("Please, enter your name for creating connection for SQL [Anna]: ").strip() or "Anna"
user_password = input("Please, enter your password for creating connection for SQL [Anna]: ").strip() or "Anna"
user_host = input("Please, enter your host for creating connection for SQL [localhost]: ").strip() or "localhost"
user_database = input("Please, enter a database, where you would like to store your data [sakila]: ").strip() or "sakila"


# Create an object for the connection.
try:
    cnx = mysql.connector.connect(user = user_name, password = user_password,
                                host = user_host,
                                database = user_database)

except mysql.connector.Error as error:
    if error.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist.")
    elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Incorrect username or password.")
    else:
        print(error)
    sys.exit(1)

# Create a variable called num_of_persons with a question to prompt user about number of test records they would like to generate.
num_of_persons = ("\nHow many test records would you like to generate?\n\
Please, enter the number: ")
# Check the user input.
num_of_persons = check_user_input(num_of_persons)

# Crerate a variable called country with a menu, where the user can choose country.
country = ("\nSelect the country:\n\
1.Great Britain\n\
2.United States of America\n\
3.Ukraine\n\
4.Spain\n\
5.France\n\
Please, enter a number of country for which you wish to generate data: ")

# Check the user input.
# Set the country locale for a Faker.
selected_country = check_country_input(country)
fake = Faker(resolve_locale(selected_country))

# Instantiate an object called my_cursor.
my_cursor = cnx.cursor()

# Execute my_cursor with create table calls persons, if not exists.
# Set up primary key with person_id.
table_name = ("\nWhat name  would you like your table to be called [persons]? ")
table_name = check_table_input(table_name, "persons")

create_table_statement = f"CREATE TABLE IF NOT EXISTS {table_name}\
(person_id int NOT NULL AUTO_INCREMENT,\
first_name varchar(255),\
last_name varchar(255),\
birthday date,\
email varchar(255),\
language varchar(255),\
building_num int,\
street_name varchar(255),\
city varchar(255),\
postcode varchar(100),\
country varchar(255),\
country_code int,\
PRIMARY KEY (person_id))"

my_cursor.execute(create_table_statement)

# Create a string called sql for the insert into table calls.
# Values %s - for each variable.
sql = "INSERT INTO persons (first_name, last_name, birthday, email, language, building_num, street_name, city, postcode, country, country_code)\
       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

random_address = Address("","","","","","")
random_person = Person("","","","","")

# Create loop for getting person details and inserting to database.
for person in range(num_of_persons):
    random_address.generate_random_address(fake,selected_country)
    random_person.generate_random_person(fake,selected_country)
    values = (random_person.first_name, random_person.last_name, random_person.birthday, random_person.email, random_person.language,\
            random_address.building_num, random_address.street_name, random_address.city, random_address.postcode,\
            random_address.selected_country, random_address.country_code)

    # Execute my_coursor with sql and values.
    my_cursor.execute(sql, values)

# Commit transactions.
cnx.commit()
# Close connection.
cnx.close()
