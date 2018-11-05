# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_
# attempts to 0.
#   Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

# I'll use 9-E instead of 9-3

class User():

    def __init__(self, first_name, last_name, middle_name='', **extra_info):
        """Initializing"""
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.login_attempts = 0
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

    def increment_login_attempts(self):
        """Increments the attribute login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the attribute login_attempts"""
        self.login_attempts = 0

    # You could have another function that checks the number of login attempts, and
    # if login attempts reaches a certain threshold, lock the user for a period of time.
    # You could then insert the function into the main loop of your program.

    def print_login_attempts(self):
        """Prints a statement showing the number of login attempts that have been made"""
        print(str(self.login_attempts) + ' logins have been attempted on user "' + self.first_name + '".')

taiga = User('taiga', 'aisaka', age=17, location='japan')

for x in range(3):                      # this thing is a for loop that runs a specified number of times, the range argument. range(3) == range(0, 3) == 0, 1, 2
    taiga.increment_login_attempts()

taiga.print_login_attempts()

taiga.reset_login_attempts()

taiga.print_login_attempts()

# alternativly without using the method, print(taiga.login_attempts)
