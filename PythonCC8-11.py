# 8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians’ names. Because the
# original list will be unchanged, return the new list and store it in a separate list.
# Call show_magicians() with each list to show that you have one list of the original
# names and one list with the Great added to each magician’s name.

# Great. I didn't do it in the way the book expects,
# So in order to do what book wants, I'll have to rewrite the code.
# -_-
# I'll make v2 doing it the way the book wants
# this way is my way.
# Working with only one list, instead of two.
# Editing the list.

def show_magicians(magicians):
    """Prints each magician"""
    for magician in magicians:
        print(magician)
    print('')

def make_great(magicians):
    """Titlecases and adds 'the Great' to each magician's name"""
    counter = 0
    while counter < len(magicians):
        magicians[counter] = magicians[counter].title() + ' the Great'
        counter += 1

magicians = ['houdini', 'gazzo', 'james', 'matt']

great_magicians = magicians[:]
make_great(great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)

# My version is an editing function
# Book's version is a building function