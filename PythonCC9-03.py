# 9-3. Users: Make a class called User. Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
#    Create several instances representing different users, and call both methods
# for each user.

# Hmm. extension... dictionary? arbirary arguments?
# handle any extra information?

class User():

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        """Prints a summary of the user's information"""
        full_name = self.first_name + ' ' + self.last_name
        print('First Name: ' + self.first_name +
              '\nLast Name: ' + self.last_name +
              '\nFull Name: ' + full_name.title() +
              '\nAge: ' + str(self.age) +
              '\nCountry: ' + self.country.title())

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print('Greetings, ' + self.first_name.title() + '!\n')

bro = User('dan', 'le', 12, 'canada')
cousin = User('dave', 'nguyen', 16, 'united states')
toradora = User('taiga', 'aisaka', 17, 'japan')

bro.describe_user()
bro.greet_user()

cousin.describe_user()
cousin.greet_user()

toradora.describe_user()
toradora.greet_user()