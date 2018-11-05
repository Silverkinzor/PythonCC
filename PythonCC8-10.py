# 8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
# Write a function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magician’s name. Call show_magicians() to
# see that the list has actually been modified.

def show_magicians(magicians):
    """prints each magician"""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Titlecases and adds 'the Great' to each magician's name"""
    counter = 0
    while counter < len(magicians):
        magicians[counter] = magicians[counter].title() + ' the Great'
        counter += 1

magicians = ['houdini', 'gazzo', 'james', 'matt']

make_great(magicians)
show_magicians(magicians)