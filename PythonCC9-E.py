# Hmm. extension... dictionary? arbirary arguments?
# handle any extra information?
# PythonCC9-03 extension, I guess
# Remember, the functions within classes are not functions, they are methods.

class User():

    def __init__(self, first_name, last_name, middle_name='', **extra_info):
        """Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        info_dictionary = {}
        for key, value in extra_info.items():
           info_dictionary[key]= value
        self.extra_info = info_dictionary

    def describe_user(self):
        """Prints a summary of the user's information"""
        if self.middle_name:
            full_name = self.first_name + ' ' + self.middle_name + ' '+ self.last_name
        else:
            full_name = self.first_name + ' ' + self.last_name

        print('\nFirst Name: ' + self.first_name)
        if self.middle_name:
              print('Middle Name: ' +  self.middle_name)
        print('Last Name: ' + self.last_name +
              '\nFull Name: ' + full_name.title())
        for info_type, info in self.extra_info.items():
            print(info_type.title() + ': ' + str(info).title())

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print('\nGreetings, ' + self.first_name.title() + '!')

guy = User('guy', 'fieri', age=50, location='ohio', occupation='restauranteur')

guy.describe_user()
guy.greet_user()

# Further extension, being able to input all of this information