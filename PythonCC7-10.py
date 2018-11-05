# 7-10. Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

# modulus(%) is a remainder function. (5 % 3 = 2)

# This is basically a copy of the example.

responses = {}
polling_active = True

while polling_active:

    repeat = ''
    print('Thank you for taking this poll!')
    name = input('\nWhat is your name?: ')
    vacation = input('Where is somewhere in the world that you want to see before you die?: ')

    responses[name] = vacation

    while repeat != 'no' and repeat != 'yes':
        repeat = input('\nWould you like to let another person take the poll? (yes/no): ')
        repeat.strip().lower()

    if repeat == 'no':
        polling_active = False

print('')
print('----Poll Results----')

for name, vacation in responses.items():
    print(name.title() + ' would like to visit ' + vacation + ' someday.')

# I could attach PythonCC6-E3 to the end of this to tally up the responses and show the number of unique and duplicate responses