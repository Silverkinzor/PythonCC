# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwich_orders = ['pastrami', 'ham and cheese', 'pastrami', 'jam', 'bologna', 'tuna', 'pastrami']
finished_sandwiches = []

print('The deli has run out of pastrami, so it will not be avaliable.' +
      '\nWe apologize for the inconvenience.\n')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print('I made your ' + sandwich + ' sandwich.')
    finished_sandwiches.append(sandwich)

print('\nAll sandwiches have been made.')
print('\nA recap of each sandwich made: ')

sandwich = ''

for sandwich in finished_sandwiches:
    print('\t' + sandwich)
