# def hasNumbers(inputString):
 
#   a = False
 
#   for char in inputString:
#        if char.isdigit():
#            a = True
         
#    return a  

# print(hasNumbers(''))

# Ignore the above, it is just a function test


# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# - If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
# - Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
# in again.

users = ['GreyRat', 'Cornyx', 'Rolebo', 'admin', 'Silverkin']

for user in users:

    if user == 'admin':
        print('Hello ' + user + ', would you like to see a status report?')

    else:
        print('Hello ' + user + ', thank you for logging in!')
