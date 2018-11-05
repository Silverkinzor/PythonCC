# PythonCC5-E3 but with dictionaries and stuff
# maybe all the 'agains' can be put into one function?

avaliable_toppings = ['mushrooms', 'pepperoni', 'extra cheese'
                      'bacon', 'beef', 'vegetables', 'asparagus']
requested_toppings = []
pizza = {
    'crust': '',
    'toppings': [],
    }
toppingStr = ''
unavaliable_toppings = False
make_anyways = ''
plain = ''
again = ''

print('Hello and welcome to the pizzeria!')
print('What kind of crust do you want on your pizza?')
print('(Leave blank for regular)')

while again != 'n': # Topping input
    again = ''
    pizza['crust'] = input('Crust: ')
    pizza['crust'] = pizza['crust'].strip().lower()

    # checking if the string contains a number

    contains_number = False

    for char in pizza['crust']:
        if char.isdigit():
            contains_number = True

    if contains_number:
        print("I don't think that is a valid crust...")

    else:
        again = 'n'
    
again = ''
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

        if topping.endswith('s') and topping != 'asparagus':
            pizza['toppings'].append(topping[:-1])

        else:
            pizza['toppings'].append(topping)

    else:
        print('Sorry, the topping "' + topping + '" is not avaliable!')
        unavaliable_toppings = True

for topping in pizza['toppings']: # proper grammar handling

    if topping == pizza['toppings'][-1] and len(pizza['toppings']) > 1: # the last
        toppingStr = toppingStr + ' and ' + topping

    elif topping != pizza['toppings'][0]:               # everything in between
        toppingStr = toppingStr + ', ' + topping

    else:                                               # the first
        toppingStr = toppingStr + topping

if not pizza['toppings']: # if pizza is empty

    while plain != 'y' and plain != 'n':

        if pizza['crust']:
            plain = input('\nDo you want a ' + pizza['crust'] + '-crust plain pizza? (Y/N): ')
        else:
            plain = input('\nDo you want a plain pizza? (Y/N): ')

        plain = (plain.strip()).lower()
    
        if plain == 'y':
            
            if pizza['crust']:
                print('A ' + pizza['crust'] + '-crust plain pizza it is then!')

            else:
                print('Plain pizza it is then!')

            toppingStr = 'plain'
    
        elif plain == 'n':
            print('Okay. I guess you get nothing then.')

        else:
            print('Answer the question.')

elif unavaliable_toppings:
    print('\nOne or more of the requested toppings are not avaliable.')

    while make_anyways != 'y' and make_anyways != 'n':

        if pizza['crust']:
            make_anyways = input('Would you still like a ' + pizza['crust'] + 
                                 '-crust, ' + toppingStr + ' pizza? (Y/N): ')
        else:
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
    if pizza['crust']:
        print("\nFinished making your " + pizza['crust'] + '-crust, ' + toppingStr + " pizza!")
    else:
        print("\nFinished making your " + toppingStr + " pizza!")
