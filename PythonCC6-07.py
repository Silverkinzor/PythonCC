# so the range() function is inclusive, but
# the slicing operator [:] and [::] are not

# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

# WHOOPS I MADE IT INTO A DICTIONARY
# DAMMIT AM I GOING TO HAVE TO REDO THIS
# REDO IT IS HERE WE GO

klawrence = {
    'first_name': 'kraft', 
    'last_name': 'lawrence', 
    'occupation': 'bathhouse owner',
    'age': 40,
    'location': 'nyohhira'
    }

ebolan = {
    'first_name': 'eve',
    'last_name': 'bolan',
    'occupation': 'merchant',
    'age': 40, 
    'location': 'winfiel'
    }

holo = {
    'first_name': 'holo',
    'last_name': '',
    'occupation': "wife",
    'age': '???',
    'location': 'nyohhira'
    }

famati = {
    'first_name': 'fermi',
    'last_name': 'amati',
    'occupation': 'merchant',
    'age': 33, 
    'location': 'kumersun'
    }

people = [klawrence, ebolan, holo, famati]

for person in people:

    full_name = person['first_name'].title() + ' ' + person['last_name'].title()

    print('Full name: ' + full_name)
    print('Occupation: ' + person['occupation'].title())
    print('Age: ' + str(person['age']))
    print('Location: ' + person['location'].title() + '\n')

# that was a bit of an ordeal to figure out