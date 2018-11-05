# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

# Using PythonCC3-06

guests = ['lawrence', 'holo', 'col']

for guest in guests:
    print('Hey ' + guest.title() + ", you're invited to dinner! ")

# What was intended, probably:
# print('Hey ' + guests[0].title() + ", you're invited to dinner! ")
# print('Hey ' + guests[1].title() + ", you're invited to dinner! ")
# print('Hey ' + guests[2].title() + ", you're invited to dinner! ")

print("\n" + str(len(guests)) + " people are invited to dinner!")

guests.remove('col')
print("\nCol can't make it. :(")

for guest in guests:
    print(guest.title() + ", you're still invited!")

# print(guests[0].title() + ", you're still invited!")
# print(guests[-1].title() + ", you're still invited!")

print("\n" + str(len(guests)) + " people are invited to dinner!")

print("\nHey all, I've found a bigger dinner table so I will be inviting more guests!")

guests.insert(0, 'mio')
guests.insert(1, 'ritsu')
guests.append('yui')
guests.append('mugi')
print('')

for guest in guests:
    print(guest.title() + ", you're invited!")

# print(guests[0].title() + ", you're invited!")
# print(guests[1].title() + ", you're invited!")
# print(guests[2].title() + ", you're invited!")
# print(guests[3].title() + ", you're invited!")
# print(guests[4].title() + ", you're invited!")
# print(guests[5].title() + ", you're invited!")

print("\n" + str(len(guests)) + " people are invited to dinner!")
