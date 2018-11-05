
# for PythonCC9-10

"""An (bad) attempt to model a restaurant"""
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + 
              self.cuisine_type + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')

    def set_number_served(self, number_served):
        """Sets the value of number_served"""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        if number_served >= 0:
            self.number_served += number_served
        else:
            print('Cannot increment by a negative number.')