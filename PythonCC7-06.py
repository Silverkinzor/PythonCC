# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# Use a conditional test in the while statement to stop the loop.
# Use an active variable to control how long the loop runs.
# Use a break statement to exit the loop when the user enters a 'quit' value.

# ver. 1

topping = ''
while topping != 'quit':
    topping = input('Enter a topping: ')

    if topping != 'quit':
        print("I'll add " + topping + ' to your pizza.')

# ver. 2

active = True
topping = ''
while active:
    topping = input('Enter a topping: ')

    if topping != 'quit':
        print("I'll add " + topping + ' to your pizza.')
    else:
        active = False

# ver. 3

topping = ''
while True:
    topping = input('Enter a topping: ')

    if topping != 'quit':
        print("I'll add " + topping + ' to your pizza.')
    else:
        break