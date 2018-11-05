# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
# silently if either file is missing.

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print('The file "' + filename + '" contains:\n' + 
                  contents + '\n')
    
    except FileNotFoundError:
        pass