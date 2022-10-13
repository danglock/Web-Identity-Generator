import argparse
import gender_guesser.detector as gender
import names
import string
import os
from random import randrange
from datetime import datetime
from config import *

parser = argparse.ArgumentParser( description = "This script can generate a fake identity" )
parser.add_argument("-b", "--banking", action = "store_true", help = "Generate banking informations")
parser.add_argument("-m", "--mailcow", action = "store_true", help = "Create an email address")
parser.add_argument("-fb", "--facebook", action = "store_true", help = "Create a facebook account")
parser.add_argument("-i", "--instagram", action = "store_true", help = "Create an instagram account")
args = parser.parse_args()





def random_date(start, end):
    """
    This function will return a random datetime between two datetime objects.
    """
    from datetime import timedelta
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)







class Identity:

    def __init__(self, firstname, lastname, age):

        self.firstname = firstname
        self.lastname = lastname
        self.age = age

        self.gender = gender.Detector().get_gender(firstname)

        if self.gender == "male":
            self.gender = "Male"
        elif self.gender == "female":
            self.gender = "Female"
        elif self.gender == "andy":
            self.gender = "Male"
        elif self.gender== "mostly_female":
            self.gender = "Female"
        elif self.gender == "mostly_male":
            self.gender = "Male"
        elif self.gender == "unknown":
            self.gender = "Male"



    def gen_banking(self):
        import ccard
        from random import randrange

        #ccv = 

        aleatory = randrange(4)


        if aleatory == 0:

            self.creditCardType = "Visa"
            self.creditCardNumber = ccard.visa()
            
        if aleatory == 1:
            self.creditCardType = "Mastercard"
            self.creditCardNumber = ccard.mastercard()
        if aleatory == 2:
            self.creditCardType = "AmericanExpress"
            self.creditCardNumber = ccard.americanexpress()
        if aleatory == 3:
            self.creditCardType = "Discover"
            self.creditCardNumber = ccard.discover()

    def register_identity(self):
        import sqlite3

        try:
            sqliteConnection = sqlite3.connect(r'data\database.db')
            cursor = sqliteConnection.cursor()

            query = "INSERT INTO t_identities (firstname, lastname, gender, birth_date, username, email, password) VALUES (?, ?, ?, ?, ?, ?, ?);"

            cursor.execute(query, (p1.firstname, p1.lastname, p1.gender, p1.age, p1.username, p1.email, p1.password))

            print("User registered !")

            cursor.close()
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Connection closed with the database.")


    def setMaicowDb(self):
        import sqlite3

        try:
            sqliteConnection = sqlite3.connect(r'data\database.db')
            cursor = sqliteConnection.cursor()

            query = "UPDATE t_identities SET mailcow = ? WHERE username = ?;"

            cursor.execute(query,(1, p1.username))

            print("User updated !")

            cursor.close()
            sqliteConnection.commit()

        except sqlite3.Error as error:
            print("Error while connecting to sqlite", error)

        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Connection closed with the database.")



    def gen_username(self):
        """
        This method generate a username (can be better !)
        """
        import random

        firstname = self.firstname
        lastname = self.lastname

        names = str(firstname) + " " + str(lastname)

        splitted_name = names.split(" ")

        first_letter = splitted_name[0][0]
        three_letters_surname = splitted_name[-1][:3]
        number = '{:03d}'.format(random.randrange(1, 999))


        username = first_letter + three_letters_surname + number

        self.username = username

        # creation of an email

        email = username.lower() + "@" + domain

        self.email = email


        # Generation of a password
        
        characters = list(string.ascii_letters + string.digits + "!@#$%&-")
        length = 13
        random.shuffle(characters)

        password = []
        for i in range(length):
            password.append(random.choice(characters))

        random.shuffle(password)

        password = "".join(password)

        self.password = password
    











# 2 dates pour générer une date de naissance
d1 = datetime.strptime('1/1/1992 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2005 4:50 AM', '%m/%d/%Y %I:%M %p')







def output(banking = False):



    print("\n-- Personnals informations --")
    print(f"Firstname       : {p1.firstname}")
    print(f"Lastname        : {p1.lastname}")
    print(f"Date of Birth   : {p1.age}")
    print(f"Gender          : {p1.gender}")

    if banking is True:

        p1.gen_banking()

        print("\n-- Bankings --")
        print(f"Card Type       : {p1.creditCardType}")
        print(f"Card Number     : {p1.creditCardNumber}")

    print("\n-- Internet --")
    print(f"Username        : {p1.username}")
    print(f"Email           : {p1.email}")
    print(f"Password        : {p1.password}")

    print("")








if __name__ == '__main__':

    autoRegister = False
    mailcow = False

    while True :
        
        # Instantiation de la personne
        p1 = Identity(firstname = names.get_first_name() , lastname = names.get_last_name() , age = random_date(d1, d2))
        # Generation d'un username
        p1.gen_username()

        output()
        print("Continue ?")
        is_ok = input("[Y/n] : ")

        if is_ok == "y" or is_ok == "Y":
            break
        elif is_ok == "exit" or is_ok == "quit":
            exit()
        else :
            os.system('cls' if os.name == 'nt' else 'clear')







    if args.mailcow:
        autoRegister = True
        mailcow = True
        from modules.genMailCowBox import genMailCowBox
        print("Creation of an email address")
        print(f"Loading MailCow config...\nURL = {mailcow_url}\nUsername = {mailcow_username}\nPassword = {mailcow_password}")
        genMailCowBox( mailcowUrl = mailcow_url,
                       mailcowUsername = mailcow_username,
                       mailcowPassword = mailcow_password,
                       newUsername = p1.username,
                       newFullName = p1.email,
                       newPassword = p1.password
                       )

        

    if args.facebook:
        if args.mailcow:
            autoRegister = True
            from modules.genFBaccount import genFBaccount
            print("creation of a facebook account")
            genFBaccount( firstname = p1.firstname,
                        lastname = p1.lastname,
                        email = p1.email,
                        password = p1.password,
                        mounth = "Dec",
                        day = "12",
                        year = "2000",
                        gender = p1.gender
                        )
        


    if args.banking:
        output(banking = True)


    if args.instagram:
        print("Creation of an instagram account")



    # END
    if autoRegister is True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Registering identity...")
        p1.register_identity()

        if mailcow is True :
            p1.setMaicowDb() # This define that the user have a mailcow address in the db
    else :
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("Would you want to register identity ?")
        register = input("[Y/n] : ")
    
        if register == "y" or register == "Y":
            print("\nRegistering identity...")
            p1.register_identity()
