# version using a return statement, not restricted to that specific list

def show_magicians(magicians):
    """Prints each magician"""
    for magician in magicians:
        print(magician)
    print('')


def make_great(magicians):
    """Titlecases and adds 'the Great' to each magician's name"""
    great_magicians = [] 
    while magicians:
        current_magician = magicians.pop()
        current_magician = current_magician.title() + ' the Great'
        great_magicians.append(current_magician)
    return great_magicians

magicians = ['houdini', 'gazzo', 'james', 'matt']

great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
