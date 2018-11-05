# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *


# v1

import sandwich

sandwich.order_sandwich('salami', 'lettuce')


# v2

from sandwich import order_sandwich

order_sandwich('knäckebröd', 'cheese', 'ham')


# v3

from sandwich import order_sandwich as od

od('cucumber')


# v4

import sandwich as sw

sw.order_sandwich('rye', 'banana', 'beef')


# v5

from sandwich import *

order_sandwich('avocado', 'pepper', 'egg')