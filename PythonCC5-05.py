# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else
# chain.
# - If the alien is green, print a message that the player earned 5 points.
# - If the alien is yellow, print a message that the player earned 10 points.
# - If the alien is red, print a message that the player earned 15 points.
# - Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

# I'll go a step further and make it an if-elif-elif-else

print('V. 1')

alien_colour = 'green'

if alien_colour == 'green':
    points = 5

elif alien_colour == 'yellow':
    points = 10

elif alien_colour == 'red':
    points = 15

else:
    points = 0

print(str(points) + ' points earned!')


print('\nV. 2')

alien_colour = 'yellow'

if alien_colour == 'green':
    points = 5

elif alien_colour == 'yellow':
    points = 10

elif alien_colour == 'red':
    points = 15

else:
    points = 0

print(str(points) + ' points earned!')


print('\nV. 3')

alien_colour = 'red'

if alien_colour == 'green':
    points = 5

elif alien_colour == 'yellow':
    points = 10

elif alien_colour == 'red':
    points = 15

else:
    points = 0

print(str(points) + ' points earned!')


print('\nV. 4')

alien_colour = 'blue'

if alien_colour == 'green':
    points = 5

elif alien_colour == 'yellow':
    points = 10

elif alien_colour == 'red':
    points = 15

else:
    points = 0

print(str(points) + ' points earned!')