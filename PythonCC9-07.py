# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator’s set of
# privileges. Create an instance of Admin, and call your method.

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

    def print_login_attempts(self):
        """Prints a statement showing the number of login attempts that have been made"""
        print(str(self.login_attempts) + ' logins have been attempted on user "' + self.first_name + '".')


class Admin(User):

    def __init__(self, first_name, last_name, middle_name = '', **extra_info):
        """Initialize admin attributes"""
        super().__init__(first_name, last_name, middle_name, **extra_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('The user "' + self.first_name +
              '" has the following admin privileges:')
        for privilege in self.privileges:
            print(privilege)

ryuuji = Admin('ryuuji', 'takasu', age=17, location='japan')
ryuuji.show_privileges()