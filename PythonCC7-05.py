# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.

print('Welcome to the movie theater.'+
      '\nTickets are different prices for different ages.')

active = True
while active:
      
    # oh great, gotta make sure its an integer
    # it always gets so complicated
    age = ''
        
    while True:
        try:
            age = input('\nHow old are you?: ')

            if age == 'quit':
                break

            age = int(age)
            break

        except:
            print('Invalid age, reenter.')
    
    if str(age) == 'quit':
        active = False
        continue

    elif age < 3:
        price = 'free'

    elif age <= 12:
        price = 10

    else:
        price = 15
    
    if str(price) != 'free':
        print('The price of your ticket will be $' + str(price) + '.')
    else:
        print('Your ticket will be ' + price + '.')