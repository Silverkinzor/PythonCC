# 10-11. Favorite Number: Write a program that prompts for the users favorite
# number. Use json.dump() to store this number in a file. Write a separate program
# that reads in this value and prints the message, I know your favorite
# number! It

import json

filename = 'favourite_number.json'

try:
    with open(filename) as f_obj:
        number = json.load(f_obj)

except FileNotFoundError:
    while True:
        number = input('What is your favourite number?: ')
        try:
            number = int(number)
        except ValueError:
            print("That's not a number!")
        else:
            break

    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
        print("\nOkay, I'll remember it next time!")

else:
    print("I know your favourite number! It's " + str(number) + '.')