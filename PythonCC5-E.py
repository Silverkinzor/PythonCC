# toppings.py but extended

avaliable_toppings = ['mushrooms', 'pepperoni', 'extra cheese']
requested_toppings = ['green pepper']
pizza_toppings = []
toppingStr = ''
unavaliable_toppings = 0
make_anyways = ''
plain = ''


for topping in requested_toppings:
    if topping in avaliable_toppings:
        print("Adding " + topping + '.')

        if topping == 'mushrooms' or topping == 'anchovies':
            pizza_toppings.append(topping[:-1])

        else:
            pizza_toppings.append(topping)

    else:
        print('Sorry, the topping "' + topping + '" is not avaliable!')
        unavaliable_toppings = unavaliable_toppings + 1

for topping in pizza_toppings: # proper grammar handling

    if topping == pizza_toppings[-1] and len(pizza_toppings) > 1: # the last
        toppingStr = toppingStr + ' and ' + topping

    elif topping != pizza_toppings[0]:               # everything in between
        toppingStr = toppingStr + ', ' + topping

    else:                                            # the first
        toppingStr = toppingStr + topping

if not pizza_toppings: # if pizza_toppings is empty

    while True:
        plain = input('\nDo you want a plain pizza? (Y/N): ')
        plain = (plain.strip()).lower()
    
        if plain == 'y':
            print('Plain pizza it is then!')
            toppingStr = 'plain'
            break
    
        elif plain == 'n':
            print('Okay. I guess you get nothing then.')
            break

        else:
            print('Answer the question.')

elif unavaliable_toppings > 0:
    print('One or more of the requested toppings are not avaliable.')

    while True:

        make_anyways = input('Would you still like a ' + toppingStr + ' pizza? (Y/N): ')
        make_anyways = (make_anyways.strip()).lower()

        if make_anyways == 'y':
            break

        elif make_anyways == 'n':
            print('Okay, I guess you get nothing then.')
            break

        else:
            print('Answer the question.')


if make_anyways == 'n' or plain == 'n': # skip if pizza is not wanted
    pass

else:
    print("\nFinished making your " + toppingStr +" pizza!")