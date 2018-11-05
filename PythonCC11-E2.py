import unittest
from employee import Employee

my_guy = Employee('sal', 'haruji', 0)

my_guy.show_attributes()

my_guy.give_raise(26000)

print('')
my_guy.show_attributes()