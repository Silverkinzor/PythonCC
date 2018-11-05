# 6-12. Extensions: We’re now working with examples that are complex enough
# that they can be extended in any number of ways. Use one of the example programs
# from this chapter, and extend it by adding new keys and values, changing
# the context of the program or improving the formatting of the output.

# But I've already been doing this since the beginning of the book...
# I'll just do the suggested extension I saw on pg. 113

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():

    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is " + languages[0].title() + '.')

    else:
        print("\n" + name.title() + "'s favorite languages are:")

        for language in languages:
            print("\t" + language.title())