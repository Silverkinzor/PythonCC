# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.

# Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.

# Use insert() to add one new guest to the beginning of your list.
# Use insert() to add one new guest to the middle of your list.
# Use append() to add one new guest to the end of your list.
# Print a new set of invitation messages, one for each person in your list.

# Remember for indexs: 0 = 1st, 1 = 2nd, 2 = 3rd and so on. Also -1 = last, -2 = second last etc.

guests = ['lawrence', 'holo', 'col']

for x in guests:
    print('Hey ' + x.title() + ", you're invited to dinner! ")

guests.remove('col')
print("\nCol can't make it. :(")

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

# Alternate can't make it
# guests.remove('col')
# print("\nCol can't make it :(")