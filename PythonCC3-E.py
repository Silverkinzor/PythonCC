# Fooling around with adding inputed things to a list
# Decided to do this after reading the "adding elements to a list" section on page 41-42

list = []
print('Enter "Stop" to stop')

while True:
    listElement = input()
    listElement = str(listElement)

    if listElement.isalpha():                   # ]
        listElementLower = listElement.lower()  # ]  Exit Condition
        if listElementLower == 'stop':          # ]
            break                               # ]

    list.append(listElement)
    print(list)
