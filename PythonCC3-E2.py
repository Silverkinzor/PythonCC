# Extension of PythonCC3-E where the user can specify insert position and handles it if the user enters some out of bounds thing

print('Inputing stuff to a list in specific positions')
list = []
print('Enter "Stop" to exit')
print('Remember for position 0 = 1st, 1 = 2nd, etc and -1 = (current) last, -2 = 2nd last, etc also')

while True:
    length = 0
    positionLower = ''
    length = len(list)

    if length == 1:
        print(str(length) + ' element in the list.')
    else:
        print(str(length) + ' elements in the list.')

    listElement = input("\nElement: ")
    listElement = str(listElement)

    if (listElement.lower()).islower(): # Exit Condition, first checks if alphabet character is in that
        listElementLower = (listElement.strip()).lower()
        if listElementLower == 'stop': # if some form of stop is entered, stop.
            break

    while True:
        position = input("Insert position: ")
        position = position.strip()
        try:
            position = int(position) # ensures integer input
            break
        except ValueError:
            positionLower = position.lower()
            if positionLower == 'stop' or positionLower == 'last': # Exit condition 2 exception or last position
                break
            print("Enter an integer.") # Otherwise make them try again to ensure integer input

    if positionLower == 'stop': # Exit Condition 2
        break

    if positionLower == 'last':
        list.append(listElement)

    elif length == 0 or position > length:
        list.append(listElement)

    elif position <= length and position >= length*-1:
        list.insert(position, listElement)

    elif position < length*-1:
        list.insert(0, listElement)

    else:
        list = "This isn't supposed to happen, something must've went wrong"

    print('')
    print(list) # output