# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + ' serves ' + 
              self.cuisine_type + '.')

    def open_restaurant(self):
        print(self.restaurant_name.title() + ' is now open!')


restaurant_1 = Restaurant("harveys", 'burgers')
restaurant_2 = Restaurant('olde yorke', 'british food')
restaurant_3 = Restaurant('dragon pearl', 'buffet style food')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()