# Same as PythonCC11-03

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