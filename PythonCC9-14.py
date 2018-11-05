# 9-14. Dice: The module random contains functions that generate random numbers
# in a variety of ways. The function randint() returns an integer in the
# range you provide. The following code returns a number between 1 and 6:
# from random import randint
# x = randint(1, 6)
# Make a class Die with one attribute called sides, which has a default
# value of 6. Write a method called roll_die() that prints a random number
# between 1 and the number of sides the die has. Make a 6-sided die and roll
# it 10 times.
# Make a 10-sided die and a 20-sided die. Roll each die 10 times.

# Extension idea, allow input for number of sides, and amount of times to roll

from random import randint

class Die():
    """Modeling a dice"""

    def __init__(self, sides=6):
        """Initialize the dice"""
        self.sides = sides

    def roll_die(self):
        rolled_number = randint(1, self.sides)
        print('Rolled number: ' + str(rolled_number))

print('10 6-sided dice rolls:')
d6 = Die()
for x in range(10):
    d6.roll_die()

print('\n10 10-sided dice rolls: ')
d10 = Die(10)
for x in range(10):
    d10.roll_die()

print('\n10 20-sided dice rolls: ')
d20 = Die(20)
for x in range(10):
    d20.roll_die()