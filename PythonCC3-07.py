# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

# Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.

# Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

guests = ['lawrence', 'holo', 'col']

for x in guests:
    print('Hey ' + x.title() + ", you're invited to dinner! ")

cant_come = guests.pop()
print("\n" + cant_come.title() + " can't make it. :(")

for x in guests:
    print(x.title() + ", you're still invited!")

print("\nHey all, I've found a bigger dinner table so I will be inviting more guests!")

guests.insert(0, 'mio')
guests.insert(1, 'ritsu')
guests.append('yui')
guests.append('mugi')
print('')

for x in guests:
    print(x.title() + ", you're invited!")

print("\n Hey, so apparently my bigger table won't arrive in time for dinner, so I can only host two people.")

print("\n" + guests[2].title() + " and " + guests[3].title() + ", you're still invited!")

removed_guest = guests.pop()
print("Sorry " + removed_guest.title() + '.')

removed_guest = guests.pop()
print("Sorry " + removed_guest.title() + '.')

removed_guest = guests.pop(0)
print("Sorry " + removed_guest.title() + '.')

removed_guest = guests.pop(0)
print("Sorry " + removed_guest.title() + '.')

del guests[1] # Alternative, use guests.clear()
del guests[0]

print('')
print(guests)