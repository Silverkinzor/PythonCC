# 10-4. Guest Book: Write a while loop that prompts users for their name. When
# they enter their name, print a greeting to the screen and add a line recording
# their visit in a file called guest_book.txt. Make sure each entry appears on a
# new line in the file.

filename = 'guest_book.txt'
guest_name = ''

print('Welcome! Input "quit" to at any time to quit')

while guest_name.strip().lower() != 'quit':

    guest_name = input('Name?: ')

    if guest_name.strip().lower() != 'quit':
        print('Hello, ' + guest_name + '!\n')

        with open(filename, 'a') as file_object:
            file_object.write(guest_name + '\n')

print('\nCome again soon!')

# maybe an alternative structure would be to get all the names first,
# store them in a list, then loop through that list