# List editor v. 1.1
# fixed bad programming habit (the while Trues and breaks)
# Now to do it in all of my other programs -_-

# You know, declaring all the variables helps reduce errors

print('List Editor')
print('Remember for position 0 = 1st, 1 = 2nd, etc and -1 = (current) last, -2 = 2nd last, etc also last for the element at the end of the list')
listT = []
menu = ''

def length_and_try_again():     # don't judge me on this function, I haven't read the function chapter yet
    print('')
    print(listT) # output
    length = len(listT)
    try_again = ''

    if length == 1: # output for length
        print(str(length) + ' element in the list.')
    else:
        print(str(length) + ' elements in the list.')

    while try_again != 'y' and try_again != 'n': # Try again? while loops are a bit tricky with and/or.
        try_again = input('\nAgain? (Y/N): ')    # think about what it actually does and it makes sense,
        try_again = (try_again.strip()).lower()  # though

    return try_again # try_again is then passed to an if try_again == 'n', and if it is then break out of the inner loop, which returns to the menu

def isInt(s): # I stole this from stackoverflow, it checks if something is a int T/F
    try: 
        int(s)
        return True
    except ValueError:
        return False

while menu != '0': # exit program

    print('\n\nList: ' + str(listT)) # the menu
    print('\nOptions:')
    print('1. Add an element to the list')
    print('2. Insert an element to a specific position')
    print('3. Delete an element in a specific position')
    print('4. Remove an element by value')
    print('5. Print specific element from list')
    print('6. Move element in a position to a different position')
    print('7. Sort list (Alphabetically)')
    print('8. Reverse list')
    print('9. Clear list')
    print('s. Slice list')
    print('0. Exit')

    menu = input('\nWhat do you want to do?: ') # menu selection
    menu = (menu.strip()).lower()
    length = len(listT) # setup
    try_again = ''

    if menu == '0': # this is still necessary otherwise it will go to the 
        pass        # "everything else" thing

    elif menu == '1': # append element
        while try_again != 'n':
            listElement = input("\nElement: ") # process
            listT.append(listElement)

            try_again = length_and_try_again() # again?
    
    elif menu == '2': # insert element
        while try_again != 'n':
            positionStr = '' # clean that positionStr

            listElement = input("\nElement: ")
            listElement = str(listElement)

            while True: # alternative, a variable
                position = input("Position: ")
                position = position.strip()
                try:
                    position = int(position) # ensures integer input
                    break
                except ValueError:
                    positionStr = position.lower()
                    if positionStr == 'last' or positionStr == 'first': # first or last position handling
                        break
                    print("Enter an integer.") # Otherwise make them try again to ensure integer input

            if positionStr == 'last' or length == 0: # insert with nothing, append to prevent error
                listT.append(listElement)

            elif positionStr == 'first':
                listT.insert(0, listElement)

            else: # all is good, insert
                listT.insert(position, listElement)

            try_again = length_and_try_again() # again?

    elif menu == '3': # delete element

        if listT:

            while try_again != 'n':
                position = ''
                positionStr = '' # clean that positionStr

                while not isInt(position): # while position is not an integer...
                    position = input("\nPosition: ")
                    position = position.strip()
                    try:
                        position = int(position) # ensures integer input

                    except ValueError:
                        positionStr = position.lower()

                        if positionStr == 'last' or positionStr == 'first': # first and last position handling
                            position = 0
                            break

                        print("Enter an integer.") # Otherwise make them try again to ensure integer input
            
                if position >= length or position < length*-1: # ensures a valid input
                    print('Position does not exist.')

                elif positionStr == 'last':
                    del listT[-1]

                elif positionStr == 'first':
                    del listT[0]

                else: # all is good, delete
                    del listT[position]

                try_again = length_and_try_again() # again?

        else:
            print('No can do señor. There are no elements!')

    elif menu == '4': # remove element by name
        if listT:

            while try_again != 'n':
            
                listElement = input('\nElement: ') # input the name

                try: # try to remove it
                    listT.remove(listElement)

                except ValueError: # if it can't print this error
                    print('Does not exist.')

                try_again = length_and_try_again() # again?

        else:
            print('No can do señor. There are no elements!')

    elif menu == '5': # print an element
        while try_again != 'n':
            position = ''

            while not isInt(position): # This loop ensures an integer input

                position = input("\nPosition: ")
                position = position.strip()

                try:
                    position = int(position)

                except ValueError:
                    pass

            if position < length and position >= length*-1: # If the input is valid, print the element
                print('\n' + listT[position])

            else: # If not, print an error
                print('Does not exist.')

            try_again = input('\nAgain? (Y/N): ') # Again? but without all the list counter stuff
            try_again = (try_again.strip()).lower() # strip white space and lower the input

    elif menu == '6': # position to position
        while try_again != 'n':
            position1 = ''
            position2 = ''

            while not isInt(position1) or not isInt(position2): # input positions, ensure integer input

                position1 = input("\nPosition 1: ")
                position2 = input("\nPosition 2: ")
                position1 = position1.strip()
                position2 = position2.strip()

                try:
                    position1 = int(position1)
                    position2 = int(position2)

                except ValueError:
                    print('Enter a valid integer.')

            if (position1 < length and position1 >= length*-1) and (position2 < length and position2 >= length*-1): # if valid input, switch the positions

                position1Ele = listT.pop(position1)
                listT.insert(position2, position1Ele)

            else: # else return an error
                print('Position specified does not exist.')

            try_again = length_and_try_again() # again?

    elif menu == '7': # sort

        Rev = ''

        while Rev != 'y' and Rev != 'n':
            Rev = input('Reverse? (Y/N): ') # sort  in reverse?
            Rev = (Rev.strip()).lower()
        
        if Rev == 'n': # no, sort normally
            listT.sort()

        elif Rev == 'y': # yes, sort in reverse
            listT.sort(reverse=True)

        else: # this should never happen
            print('Something went wrong.')

        print('Done!')

    elif menu == '8': # reverses the string
        listT.reverse()
        print('Done!')

    elif menu == '9': # clears the string
        listT.clear()
        print('Done!')

    elif menu == 's':
        print('Enter "none" in the position to leave it blank') # remember for slicing [start:stop] or [start:stop:step]

        # Maybe I should add step functionality? a question for 

        while try_again != 'n':
            position1 = ''
            position2 = ''

            while not isInt(position1) and not isInt(position2): # input positions, ensure integer input

                position1 = input("\nStart Position: ") # Inputs, accepts integers or "none"
                position2 = input("End Position: ")
                position1 = (position1.strip()).lower()
                position2 = (position2.strip()).lower()

                try:
                    if position1 != 'none':
                        position1 = int(position1)
                    else:
                        pass

                    if position2 != 'none':
                        position2 = int(position2)
                    else:
                        pass

                    # lets avoid a super long, complicated boolean in the while statement
                    # at this point position1 and position2 must = an integer or 'none'
                    # so I think it's ok to use break here
                    # it's pretty obvious what it points to anyways

                    break

                except ValueError:
                    print('Enter a valid integer or "none".')

            if position1 == 'none' and position2 != 'none':
                listT = listT[:position2]

            elif position2 == 'none' and position1 != 'none':
                listT = listT[position1:]

            elif position1 == 'none' and position2 == 'none':
                listT = listT[:]

            else:
                listT = listT[position1:position2]

            try_again = length_and_try_again() # again?

    else: # the user inputs something in the menu that isn't one of the options
        print('Enter one of the options.')
