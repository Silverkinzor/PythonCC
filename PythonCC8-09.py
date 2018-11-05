# slicing operators are useful!
# list[:] blank for a copy of a list

# 8-9. Magicians: Make a list of magician’s names. Pass the list to a function
# called show_magicians(), which prints the name of each magician in the list.

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['houdini', 'gazzo', 'james', 'matt']

show_magicians(magicians)