# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
# names of cats in the first file and three names of dogs in the second file. Write
# a program that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error,
# and print a friendly message if a file is missing. Move one of the files to a different
# location on your system, and make sure the code in the except block
# executes properly.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print('The file "' + filename + '" contains:\n' + 
                  contents + '\n')
    
    except FileNotFoundError:
        print('The file "' + filename + '" does not exist\n')