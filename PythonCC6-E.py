favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'bob': 'python',
    }

poll_results = {}

# what I want to do: make a dictionary of each value and the number of times
# it recurs and print it. A program to tally uup the favourites

for language in favorite_languages.values():        # creates new dictionary

    if language in poll_results.keys():
        poll_results[language] = poll_results[language] + 1

    else:
        poll_results[language] = 1

for language, score in poll_results.items():        # prints it
    print(language.title() + ': ' + str(score))

print('')
print(poll_results)