# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
#   Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

# note:

# number = 0
# when number is used as a boolean, it returns false
# but number != 0 used as a boolean returns true

albums = []

def make_album(name, title, number=0):
    album = {'artist': name, 'title': title}
    if number:
        album['number_of_tracks'] = int(number)
    return album

blue_turtles = make_album('sting', 'dream of the blue turtles', 10)
albums.append(blue_turtles)

jazz = make_album(title='jazz', name='queen')
albums.append(jazz)

moody_blue = make_album('elvis presley', 'moody blue')
albums.append(moody_blue)

for single_album in albums:
    print(single_album)

    for info_type, info in single_album.items():
        print(info_type.title() + ': ' + str(info).title())

    print('')