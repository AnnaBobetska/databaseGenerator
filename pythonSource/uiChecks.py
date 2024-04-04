import random
import calendar

def check_country_input(question_string):
    """ With try block prompt the user and set up input to integer.
        If the user enters a number - the program will check if the number is in range between 1 and 5(because, the user has 5 countries to choose).
        If the user entered a correct number - the program returns user_input as an integer.
        If the user entered negative number or or a letter - the program will shows an error.
        And continues to ask until the usser enters a correct number."""
    try:
        user_input = input(question_string)
        user_input = int(user_input)

        if  1 <= user_input <= 5:
            return user_input
        else:
            raise ValueError(f"\nUnfortunatly, you entered {user_input}.\nPlease, enter number from 1 until 5.\n")
    except ValueError as error:
        print(error)
        return check_country_input(question_string)

def check_user_input(question_string):
    """ With try block prompt the user and set up input to integer.
        If the user enters a number - the program will check if the number greater or equal to 1.
        If the user entered a positive number - the program returns user_input as an integer.
        If the user entered negative number or or a letter - the program will shows an error.
        And continues to ask until the usser enters a correct number."""
    try:
        user_input = input(question_string)
        user_input = int(user_input)

        if user_input >= 1:
            return int(user_input)
        else:
            raise ValueError(f"\nUnfortunatly, you entered {user_input}.\nPlease, enter a positive number.\n")
    except ValueError as error:
        print(error)
        return check_user_input(question_string)

def check_table_input(question_string, default_table):
    """ With try block prompt the user and strip the input, set up with default name of table.
        If the user enters a number or name of table longer than 64 characters - the program shows an error. 
        And continues to ask until the usser enters a correct name of table.
        If the user entered a correct name of table - the program returns a name of table."""
    try:
        table_name = input(question_string).strip() or default_table

        if 0 < len(table_name) <= 64 and not table_name.isdigit():
            return table_name
        else:
            raise ValueError(f"\nUnfortunatly, you entered {table_name}.\n\
Length of table name must be less that 65 characters and must not be an integer.\n")
    except ValueError as error:
        print(error)
        return check_table_input(question_string, default_table)

def resolve_locale(selected_country):
    """ The fuction returns a locale depends on user choice.
        If country equal to 1 - the function returns a locale for Great Britain.
        If country equal to 2 - the function returns a locale for the United States of America.
        If country equal to 3 - the function returns a locale for Ukraine.
        If country equal to 4 - the function returns a locale for Spain.
        If country equal to 5 - the function returns a locale for France."""
    locale_list = ['en_GB', 'en_US', 'uk_UA',  'es_ES', 'fr_FR']
    selected_locale = locale_list[selected_country-1]
    return selected_locale

def generate_country(selected_country):
    """ The fuction returns a country name depends on user choice.
        If country equal to 1 - the function returns Great Britain.
        If country equal to 2 - the function returns United States of America.
        If country equal to 3 - the function returns Ukraine.
        If country equal to 4 - the function returns Spain.
        If country equal to 5 - the function returns France."""
    country_list = ["Great Britain", "United States of America", "Ukraine", "Spain","France"]
    country = country_list[selected_country-1]
    return country

def generate_country_code(selected_country):
    """ The fuction returns a country code depends on user choice.
        If country equal to 1 - the function returns code for Great Britain.
        If country equal to 2 - the function returns code for United States of America.
        If country equal to 3 - the function returns code for Ukraine.
        If country equal to 4 - the function returns code for Spain.
        If country equal to 5 - the function returns code for France."""
    country_code_list = [44, 1, 380, 34, 33]
    country_code = country_code_list[selected_country-1]
    return country_code

def generate_language(selected_country): 
    """ The fuction returns a language depending on the country, which the user chooses.
        If country equal to 1 - the function returns English language.
        If country equal to 2 - the function returns English language.
        If country equal to 3 - the function returns Ukrainian language.
        If country equal to 4 - the function returns Spanish language.
        If country equal to 5 - the function returns French language."""
    language_list = ["English", "English", "Ukrainian", "Spanish", "French"]
    language = language_list[selected_country-1]
    return language


def generate_custom_email(fake, first_name, last_name):
    """ Create a variable called email_domain, which generates a random domain for an email.
        Create a variable called email and format with f-string, 
        to contain first_name in lower case, dot, last_name in lower case, at(@) and email_domain.
        Return an email."""
    email_domain = fake.domain_name()
    email = f"{first_name.lower()}.{last_name.lower()}@{email_domain}"
    return email

def generate_random_birthday():
    """ Create a list called months_30_days for number of months that have 30 days.
        Create a variable called month, to contain a random month.
        Create a variable called year, to contain a random year between 1960 until 2025.
        
        If month equal to 2 (February) set it up with 29 days, if year is a leap year.
        else set up with 28 days.
        If month in list month_30_days set up with 30 days.
        else set with 31 days.

        Return f-string with year, month and day."""
    months_30_days = [9,4,6,11]
    month = random.randint(1, 12)
    year = random.randint(1960, 2023)
    if month == 2:
        if calendar.isleap(year):
            max_day = 29
        else:
            max_day = 28
    elif month in months_30_days:
        max_day = 30
    else:
        max_day = 31

    day = random.randint(1, max_day)
    return f"{year}-{month:02d}-{day:02d}"


class Person:
    """Base class for all person objects.
    
    Attributes:
    first_name: string - random first name for a person.
    last_name: string - random last name for a person.
    birthday: f-string - random birthday day, mounth and year for a person.
    email: f-string - custom email for a person.
    language: string - language for a person depends on country."""
    def __init__(self, first_name, last_name, birthday, email, language):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.email = email
        self.language = language

    def generate_random_person(self, fake, selected_country):
        """Generate a random person with: first name, last name, birthday, email and language."""
        self.first_name = fake.first_name()
        self.last_name = fake.last_name()
        self.birthday = generate_random_birthday()
        self.email = generate_custom_email(fake,self.first_name, self.last_name)
        self.language = generate_language(selected_country)

class Address:
    """Base class for a random address.
    
    Attributes:
    building_num: integer - random buildaing number for an address.
    street_name: string - random street name for an address.
    city: string - random city name for an address.
    postcode: string - random postcode for an address.
    country: string - country, depends on user choice, for an address.
    country_code: integer - country code, depends on user choice, for an address."""
    def __init__(self, building_num, street_name, city, postcode, selected_country, country_code):
        self.building_num = building_num
        self.street_name = street_name
        self.city = city
        self.postcode = postcode
        self.selected_country = selected_country
        self.country_code = country_code

    def generate_random_address(self, fake, selected_country):
        """Generate a random address with: building number, street name, city name, postcode, country and country code."""
        self.building_num = fake.random_int(min = 1, max = 1000)
        self.street_name = fake.street_name().title()
        self.city = fake.city()
        self.postcode = fake.postcode()
        self.selected_country = generate_country(selected_country)
        self.country_code = generate_country_code(selected_country)
