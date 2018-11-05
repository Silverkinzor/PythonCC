# Extension of PythonCC-E2, list editor v1.0
# this thing is pretty much done
# (note made at a later time) Wait, isn't "while True:" and "if: break"
# bad programming practice? (seems similar to the old "goto" statements) I'll revise this in PythonCC3-E4
# I'll also have to go through ALL of my other programs and revise it -_-

print('List Editor')
print('Remember for position 0 = 1st, 1 = 2nd, etc and -1 = (current) last, -2 = 2nd last, etc also last for the element at the end of the list')
listT = []

def length_and_try_again():
    print('')
    print(listT) # output
    length = len(listT)

    if length == 1: # output for length
        print(str(length) + ' element in the list.')
    else:
        print(str(length) + ' elements in the list.')

    while True: # Try again?
        try_again = input('\nAgain? (Y/N): ')
        try_again = (try_again.strip()).lower()

        if try_again == 'y' or try_again == 'n': 
            break

    return try_again # try_again is then passed to an if try_again == 'n', and if it is then break out of the inner loop, which returns to the menu

while True:

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

    if menu == '0': # exit program
        break

    elif menu == '1': # append element
        while True:
            listElement = input("\nElement: ") # process
            listT.append(listElement)

            try_again = length_and_try_again() # again?
            if try_again == 'n':
                break
    
    elif menu == '2': # insert element
        while True:
            positionStr = '' # clean that positionStr

            listElement = input("\nElement: ")
            listElement = str(listElement)

            while True:
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
            if try_again == 'n':
                break

    elif menu == '3': # delete element
        while True:
            positionStr = '' # clean that positionStr

            while True:
                position = input("\nPosition: ")
                position = position.strip()
                try:
                    position = int(position) # ensures integer input
                    break
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
            if try_again == 'n':
                break

    elif menu == '4': # remove element by name
        while True:
            
            listElement = input('\nElement: ') # input the name

            try: # try to remove it
                listT.remove(listElement)

            except ValueError: # if it can't print this error
                print('Does not exist.')

            try_again = length_and_try_again() # again?
            if try_again == 'n':
                break

    elif menu == '5': # print an element
        while True:

            while True: # This loop ensures an integer input

                position = input("\nPosition: ")
                position = position.strip()

                try:
                    position = int(position)
                    break

                except ValueError:
                    pass

            if position < length and position >= length*-1: # If the input is valid, print the element
                print('\n' + listT[position])

            else: # If not, print an error
                print('Does not exist.')

            while True: # Try_again, the function but without the list counter part
                try_again = input('\nAgain? (Y/N): ')
                try_again = (try_again.strip()).lower() # strip white space and lower the input

                if try_again == 'y' or try_again == 'n':
                    break

            if try_again == 'n': 
                    break

    elif menu == '6': # position to position
        while True:

            while True: # input positions, ensure integer input

                position1 = input("\nPosition 1: ")
                position2 = input("\nPosition 2: ")
                position1 = position1.strip()
                position2 = position2.strip()

                try:
                    position1 = int(position1)
                    position2 = int(position2)
                    break

                except ValueError:
                    print('Enter a valid integer.')

            if (position1 < length and position1 >= length*-1) and (position2 < length and position2 >= length*-1): # if valid input, switch the positions

                position1Ele = listT.pop(position1)
                listT.insert(position2, position1Ele)

            else: # else return an error
                print('Position specified does not exist.')

            try_again = length_and_try_again() # again?
            if try_again == 'n':
                break

    elif menu == '7': # sort
        while True:
            Rev = input('Reverse? (Y/N): ') # sort  in reverse?
            Rev = (Rev.strip()).lower()

            if Rev == 'y' or Rev == 'n':
                break
        
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

        while True:

            while True: # input positions, ensure integer input

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
            if try_again == 'n':
                break

    else: # the user inputs something in the menu that isn't one of the options
        print('Enter one of the options.')

# Would an alternative clear fuction be:
# for x in listT:
#     del listT[0]
#
# ?

# Alternative reverse function:
# for x in listT:
#     RevElement = listT.pop()
#     listR.append(RevElement)]
# listT = listR
# listR.clear()
# 
# ?


# Extended functionality:

# An option to create another list by slicing the first list
# Then the ability to choose which list you want to perform the operation selected operation on, or all of them.
# The ability to create as many lists as the user wants dynamically, and the options also change dynamically in regards to the number of lists
# The ability to create and delete these lists at will

# A simple replace function, which replaces the element in a specific position with the input