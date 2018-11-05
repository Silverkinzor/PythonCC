# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

glossary = {'defenestration': 'the act of throwing something out of a window', 
            'list': 'a collection of items in a particular order', 
            'float': 'any number with a decimal point', 
            'integer': 'any number without a decimal point',
            'whitespace': 'any nonprinting character, such as spaces, tabs and end-of-line-symbols',
            'slice': 'working with a specific group of elements from a list',
            'list comprehension': 'a method of generating a list with just one line of code',
            'string': 'a sequence of characters',
            'comments': 'regular english in the code that explains the code',
            'method': 'an action that Python can perform on a piece of data',
            }

for term, definition in glossary.items():
    print('The term "' + term + '" refers to ' + definition + '.\n')