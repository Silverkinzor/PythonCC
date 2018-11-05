class Employee():

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize employee attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Adds an amount to the annual salary, default 5000"""
        self.annual_salary += raise_amount

    def show_attributes(self):
        """Prints employee attributes"""
        formatted_name = self.first_name.title() + ' ' + self.last_name.title()
        print('Name: ' + formatted_name)
        print('Annual Salary: ' + str(self.annual_salary))