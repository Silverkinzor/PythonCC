# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
# printing each person’s name, print a message to them. The text of each message
# should be the same, but each message should be personalized with the
# person’s name.

# I'll also use a for loop because copy and pasting code is boring
# also using the title method

names = [ 'yui', 'mio', 'ritsu', 'mugi' ]
c = 0

for x in names:
    print(names[c].title() + " is a member of Hokago Tea Time!")
    c = c + 1

# Or maybe:

# for x in names:
#     print(x.title())

# The expected way to do it:

# names = [ 'yui', 'mio', 'ritsu', 'mugi' ]

# print(names[0].title() + " is a member of Hokago Tea Time!")
# print(names[1].title() + " is a member of Hokago Tea Time!")
# print(names[2].title() + " is a member of Hokago Tea Time!")
# print(names[3].title() + " is a member of Hokago Tea Time!")

# How boring.