
# the 'continue' statement returns to the beginning of the loop without running the rest of the code

# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

topping = ''
while topping != 'quit':
    topping = input('Enter a topping: ')

    if topping != 'quit':
        print("I'll add " + topping + ' to your pizza.')