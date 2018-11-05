# PythonCC5-E but you can input requested toppings
# Also fixed the unhealthy while True loops and break statements
# Maybe I could put all the 'try agains' in one function

avaliable_toppings = ['mushrooms', 'pepperoni', 'extra cheese']
requested_toppings = []
pizza_toppings = []
toppingStr = ''
unavaliable_toppings = False
make_anyways = ''
plain = ''
again = ''

print('Hello and welcome to the pizzeria!')
print('What toppings would you like on your pizza?\n')

while again != 'n': # Topping input
    again = ''
    req_topping = input('Topping: ')
    req_topping = req_topping.strip().lower()

    # checking if the string contains a number

    contains_number = False

    for char in req_topping:
        if char.isdigit():
            contains_number = True

    if contains_number:
        print("I don't think that is a valid topping...")

    else:
        requested_toppings.append(req_topping)
    
    while again != 'y' and again != 'n':

        again = input('Would you like to add another topping? (Y/N): ')
        again = again.strip().lower()

        if again != 'y' and again != 'n':
            print('Answer the question.')

print('')

for topping in requested_toppings: # topping handling, creation of a list of toppings able to go on the pizza
    if topping in avaliable_toppings:
        print("Adding " + topping + '.')

        if topping == 'mushrooms' or topping == 'anchovies':
            pizza_toppings.append(topping[:-1])

        else:
            pizza_toppings.append(topping)

    else:
        print('Sorry, the topping "' + topping + '" is not avaliable!')
        unavaliable_toppings = True

for topping in pizza_toppings: # proper grammar handling

    if topping == pizza_toppings[-1] and len(pizza_toppings) > 1: # the last
        toppingStr = toppingStr + ' and ' + topping

    elif topping != pizza_toppings[0]:               # everything in between
        toppingStr = toppingStr + ', ' + topping

    else:                                            # the first
        toppingStr = toppingStr + topping

if not pizza_toppings: # if pizza_toppings is empty

    while plain != 'y' and plain != 'n':
        plain = input('\nDo you want a plain pizza? (Y/N): ')
        plain = (plain.strip()).lower()
    
        if plain == 'y':
            print('Plain pizza it is then!')
            toppingStr = 'plain'
    
        elif plain == 'n':
            print('Okay. I guess you get nothing then.')

        else:
            print('Answer the question.')

elif unavaliable_toppings:
    print('\nOne or more of the requested toppings are not avaliable.')

    while make_anyways != 'y' and make_anyways != 'n':

        make_anyways = input('Would you still like a ' + toppingStr + ' pizza? (Y/N): ')
        make_anyways = (make_anyways.strip()).lower()

        if make_anyways == 'y':
            pass

        elif make_anyways == 'n':
            print('Okay, I guess you get nothing then.')

        else:
            print('Answer the question.')


if make_anyways == 'n' or plain == 'n': # skip if pizza is not wanted
    pass

else:
    print("\nFinished making your " + toppingStr + " pizza!")


# but would

# if make_anyways != 'n' or plain != 'n':
#   print("\nFinished making your " + toppingStr + " pizza!")

# be better?

# a function to check if any number is in a string?

# def hasNumbers(inputString):
# 
#   a = True
# 
#   for char in inputString:
#       if char.isdigit():
#           a = False
#         
#   return a  