# 8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
# a profile of yourself by calling build_profile(), using your first and last names
# and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

# I just don't feel comfortable using my real information here...
# kinda fake version then, i guess

my_profile = build_profile('matt', 'le',
                           location='toronto',
                           favourite_food='fish and chips',
                           occupation='student')

print(user_profile)
print(my_profile)

# Extension idea, multiple user handling
# but wasn't that already covered in the dictionary chapter?
# I already kind of know how to do that (I think)
# nested for loops right