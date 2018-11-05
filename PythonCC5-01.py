
# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# - Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# - Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.

# 10 tests!?! ugh. I know how if statements work


# Tests if food is pizza

food = 'pizza'
print('Is food == pizza? predict True')
print(food == 'pizza')
print('Is food == fish? predict False')
print(food == 'fish')
print('Is food == Pizza? predict False')
print(food == 'Pizza')
print('Is food.title() == Pizza? predict True')
print(food.title() == 'Pizza')
print('Is food.upper() == PIZZA? predict True')
print(food.upper() == 'PIZZA')
print('Is food != pizza? predict False')
print(food != 'pizza')
print('Is food != knackebrod? predict True')
print(food != 'knackebrod')

number = 24
number2 = 350
print('\nIs number == 24 and number != 350? predict False')
print(number == 24 and number2 != 350)
print('Is number > 24 or number < 24? predict False')
print(number > 24 or number < 24)
print('Is number != 7? predict True')
print(number != 7)
print('Is number < (28/4)*3? predict False')
print(number < (28/4)*3)
print('Is number not == 24? predict False')
print(not number == 24)

banned = ['bob', 'dylan', 'james']
print('\nIs duke banned? predict False')
print('duke' in banned)
print('\nIs duke not banned? predict True')
print('duke' not in banned)
print('Is james banned? predict True')
print('james' in banned)

# if statement structure:
# if (condition):
#     code

# if not (condition):
# will reverse the value of the condition, false will be true, true will be false