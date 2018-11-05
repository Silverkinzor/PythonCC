# 11-3. Employee: Write a class called Employee. The __init__() method should
# take in a first name, a last name, and an annual salary, and store each of these
# as attributes. Write a method called give_raise() that adds $5000 to the
# annual salary by default but also accepts a different raise amount.
#   Write a test case for Employee. Write two test methods, test_give_
# default_raise() and test_give_custom_raise(). Use the setUp() method so
# you don’t have to create a new employee instance in each test method. Run
# your test case, and make sure both tests pass.

# note, each test uses fresh setUp variables that are local to that test
# they are not saved throughout the test
# The only thing global to the whole test is anything in setUp

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Create an employee for use in all test methods"""
        self.testEmployee = Employee('Rob', 'Stark', 63000)

    def test_give_default_raise(self):
        """Tests that the default raise amount (5000) is working properly"""
        self.testEmployee.give_raise()
        self.assertEqual(self.testEmployee.annual_salary, 68000)

    def test_give_custom_raise(self):
        """Tests that a custom raise amount works properly"""
        self.testEmployee.give_raise(7000)
        self.assertEqual(self.testEmployee.annual_salary, 70000)
        
unittest.main()

# Now that I'm done with the first part of this book, onto projects