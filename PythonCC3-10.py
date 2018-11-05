# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything
# else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.

# Bleh. I don't want to do this but fine. A bit of a pain in the arse.

keions = ['mugi', 'mio', 'ritsu']

print('There are ' + str(len(keions)) + ' members of the Light Music Club!')

print("\n" + keions[0].title() + " is on keyboard!")
print(keions[1].title() + " is on bass!")
print(keions[2].title() + " is on drums!")

keions.append('yui')
print("\n" + keions[-1].title() + " joined the Light Music Club!")
print(keions[-1].title() + " is on lead guitar!")
print('There are now ' + str(len(keions)) + ' members of the Light Music Club!')

keions.insert(1, 'azusa')
print("\n" + keions[1].title() + " joined the Light Music Club!")
print(keions[1].title() + " is on rhythm guitar!")
print('There are now ' + str(len(keions)) + ' members of the Light Music Club!')

on_vacation = keions.pop(0)
print("\n" + on_vacation.title() + " went on vacation!")
print('There are now ' + str(len(keions)) + ' members of the Light Music Club!')

keions.insert(0, on_vacation)
print('\n' + keions[0].title() + " is back from her vacation!")
print('There are now ' + str(len(keions)) + ' members of the Light Music Club!')
print('')

print(sorted(keions))
print(sorted(keions, reverse=True))
print(keions)
keions.reverse()
print(keions)
keions.sort()
print(keions)
keions.sort(reverse=True)
print(keions)

del keions [3]
print("\nMio graduated!")
del keions[0]
print("Yui graduated!")
keions.remove('ritsu')
print('Ritsu graduated!')
keions.remove('mugi')
print('Mugi graduated!')

print('\nThere is now ' + str(len(keions)) + ' member of the Light Music Club!')
print(keions)