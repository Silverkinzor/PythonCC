# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

def make_album(name, title, number=0):
    album = {'artist': name, 'title': title}
    if number:
        album['number_of_tracks'] = number
    return album

artist_name = ''
album_title = ''
track_number = ''

print('Album maker')
print('Input "q" at any time to quit')

while True:

    artist_name = input('\nWhat is the name of the artist?: ')
    if artist_name == 'q':
        break

    album_title = input('What is the name of the album?: ')
    if album_title == 'q':
        break

    while True:
        track_number = input('How many tracks are in the album?: ')
        try:
            track_number = int(track_number)
            break
        except ValueError:
            if track_number == 'q':
                break
            else:
                print('a NUMBER.')
    if track_number == 'q':
        break

    album_information = make_album(artist_name, album_title, track_number)
    print(album_information)