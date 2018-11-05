# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
# would you invite? Make a list that includes at least three people you’d like to
# invite to dinner. Then use your list to print a message to each person, inviting
# them to dinner.

guests = ['lawrence', 'holo', 'col']

print('Hey ' + guests[0].title() + ", you're invited to dinner! ")
print('Hey ' + guests[1].title() + ", you're invited to dinner! ")
print('Hey ' + guests[2].title() + ", you're invited to dinner! ")

# Or how about

# for x in guests:
#     print('Hey ' + x.title() + ", you're invited to dinner! ")

# hardcoding the guest list feels wrong