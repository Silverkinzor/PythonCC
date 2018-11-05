# An alternative version of PythonCC4-10 where the items are printed in a single line

cubes = [value**3 for value in range(1, 11)]
print(cubes)

cubes1 = ''
cubes2 = ''
cubes3 = ''


print('\nThe first three items in the list are: ')

for cube in cubes[:3]:
    cubes1 = cubes1 + str(cube) + ' '

cubes1.rstrip()
print(cubes1)

print('\nThree items from the middle of the list are: ')

for cube in cubes[4:7]:
    cubes2 = cubes2 + str(cube) + ' '

cubes2.rstrip()
print(cubes2)

print('\nThe last three items in the list are: ')

for cube in cubes[-3:]:
    cubes3 = cubes3 + str(cube) + ' '

cubes3.rstrip()
print(cubes3)