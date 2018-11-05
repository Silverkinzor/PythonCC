# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.

from collections import OrderedDict

glossary = OrderedDict()

glossary['list'] = 'a collection of items in a particular order'
glossary['whitespace'] = 'any nonprinting character, such as spaces, tabs and end-of-line-symbols'
glossary['list comprehension'] = 'a method of generating a list with just one line of code'
glossary['string'] = 'a sequence of characters'
glossary['defenestration'] = 'the act of throwing something out of a window'

for term, definition in glossary.items():
    print('The term "' + term + '" refers to ' + definition + '.\n')