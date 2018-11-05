# The only code that should go in a try statement
# is code that might cause an exception to be raised., p. 203

# 10-6. Addition: One common problem when prompting for numerical input
# occurs when people provide text instead of numbers. When you try to convert
# the input to an int, you'll get a TypeError. Write a program that prompts for
# two numbers. Add them together and print the result. Catch the TypeError if
# either input value is not a number, and print a friendly error message. Test your
# program by entering two numbers and then by entering some text instead of a
# number.

# Heh, I've dealt with that problem a lot.

first_number = ''
second_number = ''

print('Simple Addition Calculator' +
      '\nInput q to quit.')

while first_number != 'q' and second_number != 'q':

    try:
        first_number = input('\nFirst Number: ')
        first_number = int(first_number)
        second_number = input('Second Number: ')
        second_number = int(second_number)

    except ValueError:
        if first_number != 'q' and second_number != 'q':
            print('Enter valid numbers.')

    else:
        answer = first_number + second_number
        print(answer)