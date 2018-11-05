favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

poll_results = {}

# what I want to do: make a dictionary of each value and the number of times
# it recurs and print it. A program to tally up the favourites
# PythonCC6-E3 edition, lists instead of just 1 string, multiple choice support
# solution: nest a for loop

for languages in favorite_languages.values():        # creates new dictionary

    for language in languages:

        if language in poll_results.keys():
            poll_results[language] += 1

        else:
            poll_results[language] = 1

for language, score in poll_results.items():        # prints it
    print(language.title() + ': ' + str(score))

print('')
print(poll_results)
