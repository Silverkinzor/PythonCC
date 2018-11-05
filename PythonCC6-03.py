# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# - Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# - Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

glossary = {'defenestration': 'the act of throwing something out of a window', 
            'list': 'a collection of items in a particular order', 
            'float': 'any number with a decimal point', 
            'integer': 'any number without a decimal point',
            'whitespace': 'any nonprinting character, such as spaces, tabs and end-of-line-symbols', 
            }

print('Defenestration is ' + glossary['defenestration'] + '.\n')
print('A list is ' + glossary['list'] + '.\n')
print('A float is ' + glossary['float'] + '.\n')
print('An integer is ' + glossary['integer'] + '.\n')
print('Whitespaces refers to ' + glossary['whitespace'] + '.\n')