"""
Implements unit tests for the module naive_solution
"""
import os
import sys
import unittest
import naive_solution

class TestLoadDataOkInput(unittest.TestCase):
    """ Test that the function load_data in NaiveSolution loads correctly 
    the data when the input file is correct """
    def setUp(self):
        self.ns = naive_solution.NaiveSolution("data/ok_format_operator.txt")
        self.ns.load_data()


    def test_size_operators(self):
        self.assertEqual(len(self.ns.operator_data), 2)

    def test_operator_ids(self):
        pass

    def test_operator_known_values(self):
        pass


if __name__ == '__main__':
    print __file__
    unittest.main()
