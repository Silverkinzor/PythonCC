# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
# each person can have more than one favorite number. Then print each person’s
# name along with their favorite numbers.

favourite_numbers = {'bob': [27, 31, 85], 
                     'gregory': [64, 128], 
                     'matt': [2, 4, 6, 7],
                     'hal': [42], 
                     'joseph': [894, 219, 300]
                     }

for name, numbers in favourite_numbers.items():

#    if len(numbers) == 1:
#        print(name.title() + "'s favourite number is " + str(number) + '.')

#    else:
        numberStr = ''

        for number in numbers:
            
            if number == numbers[0]:
                numberStr = numberStr + str(number)

#            elif number == numbers[-1]:
#                numberStr = numberStr + ' and ' + str(number)

            else:
                numberStr = numberStr + ', ' + str(number)
            
        print(name.title() + ": " + numberStr)
#        print(name.title() + "'s favourite numbers are " + numberStr + '.')
        
        print('')
#    print('')

# not exactly what was asked in the exercise, but it does the same thing.
# just extra code for grammar.
# exercise in what was asked in actual code