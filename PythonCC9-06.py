# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

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

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['vanilla', 'chocolate', 'mint', 'green tea']

    def display_flavours(self):
        print('The follow ice cream flavours are avaliable:')
        for flavour in self.flavours:
            print(flavour)
        print('')

    def add_flavour(self, new_flavour):
        self.flavours.append(new_flavour)

la_paloma = IceCreamStand('la paloma')

la_paloma.describe_restaurant()
la_paloma.display_flavours()

la_paloma.add_flavour('strawberry')
la_paloma.display_flavours()