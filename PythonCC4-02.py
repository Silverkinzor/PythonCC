# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.
# - Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# - Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!

aquarium_fish = ['dwarf gourami', 'neon tetra', 'platy']

for fish in aquarium_fish:
    print(fish)

print('\nA ' + aquarium_fish[0].title() + ' is a nice colourful centerpiece fish. But if you keep more than one in the same tank then you may have problems!\n')
print(aquarium_fish[1].title() + 's are popular choice. Always keep them in groups of at least ~6 as they are a schooling species, and be aware that they can be quite fragile!\n')
print('The ' + aquarium_fish[2].title() + ' is an active, social fish. Always keep more than one. Be careful though, they breed alot!\n')

print('All of these fish are suitable for a peaceful, tropical aquarium.')
