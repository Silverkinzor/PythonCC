# 2-7. Stripping Names: Store a person’s name, and include some whitespace
# characters at the beginning and end of the name. Make sure you use each
# character combination, "\t" and "\n", at least once.
# Print the name once, so the whitespace around the name is displayed.
# Then print the name using each of the three stripping functions, lstrip(),
# rstrip(), and strip().

name = "   Kraft \n\tLawrence       "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# I guess I can't really see the effects well in this environment ¯\_(ツ)_/¯