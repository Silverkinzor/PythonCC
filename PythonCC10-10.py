# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files for these
# works, or copy the raw text from your browser into a text file on your
# computer.
# You can use the count() method to find out how many times a word or
# phrase appears in a string. For example, the following code counts the number
# of times 'row' appears in a string:
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted.
# Write a program that reads the files you found at Project Gutenberg and
# determines how many times the word 'the' appears in each text.

# Also note the method split()
# line = "Row, row, row your boat"
# line.split()
# ['Row,', 'row,', 'row', 'your', 'boat']

print('"the" counter\n---------------------' )

books = ["Alice in Wonderland.txt", 'Moby Dick.txt', 'The Adventures of Tom Sawyer.txt', 'Dracula.txt', 'Tarzan of the Apes.txt']

for book in books:

    try:
        with open(book) as f_obj:
            contents = f_obj.read()

    except FileNotFoundError:
        print('\nThe book "' + book[:-4] + '" was not found.')

    except UnicodeDecodeError:
        print('\nSomething went wrong when trying to read "' + book[:-4] + '".')

    else:
        the_count = contents.lower().count('the')
        print('\nIn "' + book[:-4] + '", "the" appears approximately ' +
              str(the_count) + ' times.')