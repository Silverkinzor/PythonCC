# Exercise 8-11/8-10, done the way the book wants.

def show_magicians(magicians):
    """Prints each magician"""
    for magician in magicians:
        print(magician)
    print('')

def make_great(magicians):
    """Titlecases and adds 'the Great' to each magician's name"""
    while magicians:
        current_magician = magicians.pop()
        current_magician = current_magician.title() + ' the Great'
        great_magicians.append(current_magician)

# Lists are global!
# no return statement needed

magicians = ['houdini', 'gazzo', 'james', 'matt']
great_magicians = []

make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)

# arbitrary arguments:
# def function(*argument) for tuple
# def function(**argument) for dictionary