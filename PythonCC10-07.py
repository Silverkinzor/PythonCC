# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
# so the user can continue entering numbers even if they make a mistake and
# enter text instead of a number.

# But I already made it that way from the beginning...

# Guess it expected this the first time
# I guess pythonCC10-06 and 07 got switched.

print('Simple Addition Calculator')

try:
    first_number = input('\nFirst Number: ')
    first_number = int(first_number)
    second_number = input('Second Number: ')
    second_number = int(second_number)

except ValueError:
    print('Enter valid numbers.')

else:
    answer = first_number + second_number
    print(answer)