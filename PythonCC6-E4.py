# PythonCC6-E3 extension which includes output to a text file

filename = 'favourite_languages_poll.txt'
poll_results = {}
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

open(filename, "w").close() # cleans the text file

for languages in favorite_languages.values():

    for language in languages:

        if language in poll_results.keys():
            poll_results[language] += 1

        else:
            poll_results[language] = 1

for language, score in poll_results.items():
    print(language.title() + ': ' + str(score))
    
    with open(filename, 'a') as file_object:
        file_object.write(language.title() + ': ' + str(score) + '\n')

# Next up, inputs, ongoing polling (storage)