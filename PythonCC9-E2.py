# the thing, but with inputs

# can replace the following with the whole of user.py
# apparently from ___ import * is not good practice

from user import User, Admin

print('PythonCC9-something, user thing with inputs' + 
      '\nUse the middle_name keyword for proper middle name handling' +
      '\nUser Creation' +
      '\n---------------------------------------------------')

input_active = True
extra_info = {}
add_more = ''
user_selection = ''

first_name = input('First name?: ')
first_name = first_name.strip().lower()
last_name = input('Last name?: ')
last_name = last_name.strip().lower()

while input_active == True:

    add_more = input('Would you like to add more info? (Y/N): ')
    add_more = add_more.strip().lower()

    if add_more == 'n':
        input_active = False
        print('')
    
    else:
        keyword = input('Keyword?: ')
        keyword = keyword.strip().lower()
        if keyword == 'middle name' or keyword == 'middlename':
            keyword = 'middle_name'

        value = input('Value?: ')
        value = value.strip()
        extra_info[keyword] = value

print('What kind of user do you want to create?' + 
      '\n1. User' + 
      '\n2. Admin')

while user_selection != '1' and user_selection != '2':
    user_selection = input()
    if user_selection != '1' and user_selection != '2':
        print('Type in one of the options!')

if user_selection == '1':
    user = User(first_name, last_name, **extra_info) # the ** unpacks the dictionary of extra_info into keywords

elif user_selection == '2':
    user = Admin(first_name, last_name, **extra_info)

user.describe_user()
user.greet_user()

# Further expansion into selecting methods through the program...?
# Create new user
# logging in
# new selectable methods (same as the first one)
# like view login attempts
# actual privilege control
# Maybe a message board