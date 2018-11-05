from user_only import User

class Admin(User):

    def __init__(self, first_name, last_name, middle_name = '', **extra_info):
        """Initialize admin attributes"""
        super().__init__(first_name, last_name, middle_name, **extra_info)
        self.privileges = Privileges()


class Privileges():

    def __init__(self):
        """Initialize the Priviliges attributes"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print('The following admin privileges are avaliable to this user:')
        for privilege in self.privileges:
            print(privilege)
