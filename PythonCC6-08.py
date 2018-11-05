# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.

glaze = {
    'name': 'glaze',
    'species': 'cat',
    'type': 'shorthair',
    'temperament': 'lazy',
    }

weston = {
    'name': 'weston',
    'species': 'dog',
    'type': 'terrier',
    'temperament': 'active',
    }

pandora = {
    'name': 'pandora',
    'species': 'fish',
    'type': 'dwarf gourami',
    'temperament': 'calm',
    }

rebel = {
    'name': 'rebel',
    'species': 'dog',
    'type': 'beagle',
    'temperament': 'feisty',
    }

pipsqueak = {
    'name': 'pipsqueak',
    'species': 'fish',
    'type': 'neon tetra',
    'temperament': 'peaceful'
    }


pets = [glaze, weston, pandora, rebel, pipsqueak]

for pet in pets:

    for info_type, info in pet.items(): # remember the .items()!
        print(info_type.title() + ': ' + info.title())

    print('')