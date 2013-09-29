"""                                                                                          
Implements unit tests for the module main                                            
"""
import os
import sys
import unittest
import tempfile
import shutil
import simple_solution
import optimized_solution
import main

class TestGetSolutionClass(unittest.TestCase):
    """ Test the get_solution_class function """
    def test_known_method(self):
        """ Test if it return the correct method when this is known """
        self.assertEqual(main.get_solution_class("simple"), \
            simple_solution.SimpleSolution)
        self.assertEqual(main.get_solution_class("fast"), \
            optimized_solution.OptimizedSolution)
      
    def test_unknown_method(self):
        """ Test that the program exits if an unknown method is given """
        with self.assertRaises(SystemExit) as cm:
            main.get_solution_class("some-method")
        the_exception = cm.exception
        self.assertEqual(str(the_exception), "Unknown method: some-method")


class TestGetPhoneNumbers(unittest.TestCase):
    """ Test that the function get_phone_numbers returns the correct data """
    def test_correct_number(self):
       """ Test the result is correct when one phone number is given """
       numbers = main.get_phone_numbers("1223")
       self.assertEqual(numbers, ["1223"])

    def test_incorrect_number(self):
       """ Test the result is an empty list when one phone number is incorrect """
       numbers = main.get_phone_numbers("1223h")
       self.assertEqual(numbers, [])

    def test_correct_file(self):
        """ Test the result is correct when a file is given with one correct phone
        number """
        lines = "q123\n456HJH75\n236456"
         # make a temporary file including these lines                                       
        (tmp, tmp_file) = tempfile.mkstemp()
        in_handler = open(tmp_file, "w")
        in_handler.write(lines)
        in_handler.close()
        numbers = main.get_phone_numbers(tmp_file)
        self.assertEqual(numbers, ["236456"])


class TestFormatSolution(unittest.TestCase):
    """ Test that the function to format the solution works as expected """
    def test_empty_list(self):
        """ Test the result when an empty list is given """
        self.assertEqual(main.format_solution([]), "No solution")

    def test_single_element_list(self):
        """ Test the result is as expected when the list has one element """
        solution_str = main.format_solution([("A", "123", 0.15)])
        self.assertEqual(solution_str, "A 123 0.15")

    def test_larger_element_list(self):
        """ Test the result is as expected when the list has more elements """
        solution_str = main.format_solution([("A", "123", 0.15), \
            ("B", "123", 0.15), ("C", "12", 0.15)])
        self.assertEqual(solution_str, "A 123 0.15\tB 123 0.15\tC 12 0.15")


if __name__ == '__main__':
    unittest.main()
        
        
