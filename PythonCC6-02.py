# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.

favourite_numbers = {'bob': 27, 'gregory': 64, 'matt': 2, 'hal': 42, 'joseph': 894}

print("Bob's favourite number is " +     # testing out splitting it across multiple lines
      str(favourite_numbers['bob']) +
      ".")

print("Gregory's favourite number is " + str(favourite_numbers['gregory']) + '.')
print("Matt's favourite number is " + str(favourite_numbers['matt']) + '.')
print("Hal's favourite number is " + str(favourite_numbers['hal']) + '.')
print("Joseph's favourite number is " + str(favourite_numbers['joseph']) + '.')