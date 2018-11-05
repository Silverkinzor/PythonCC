# 10-5. Programming Poll: Write a while loop that asks people why they like
# programming. Each time someone enters a reason, add their reason to a file
# that stores all the responses.

# Each time someone enters a reason... not a data collection phase and then a work phase, but at once. ok.

filename = 'programming_poll.txt'
polling_active = True

print('Thank you for taking this poll!')

while polling_active:           # a while True, break statement would work just as well.

    name = input('\nName?: ')
    reason = input('Why do you like programming?: ')

    with open(filename, 'a') as file_object:
        file_object.write(name.title() + ': ' + reason + '\n')

    while True:
        try_again = input('\nWill another person take the poll? (Y/N): ')
        try_again = try_again.strip().lower()
        if try_again == 'y' or try_again == 'n':
            break

    if try_again == 'n':
        polling_active = False

print('\nPolling finished, output stored in programming_poll.txt')

# side note:
# reminder to create an extension of PythonCC6-E3 to allow inputs within the program
# or maybe even from a text file, and then outputs the result to a text file, not just the program