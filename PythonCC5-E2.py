# PythonCC5-05 but repeated code is a function

def colour_to_points(colour):
    if colour == 'green':
        pts = 5

    elif colour == 'yellow':
        pts = 10

    elif colour == 'red':
        pts = 15

    else:
        pts = 0

    return pts

print('V. 1')
alien_colour = 'green'
points = colour_to_points(alien_colour)
print(str(points) + ' points earned!')


print('\nV. 2')
alien_colour = 'yellow'
points = colour_to_points(alien_colour)
print(str(points) + ' points earned!')


print('\nV. 3')
alien_colour = 'red'
points = colour_to_points(alien_colour)
print(str(points) + ' points earned!')


print('\nV. 4')
alien_colour = 'blue'
points = colour_to_points(alien_colour)
print(str(points) + ' points earned!')