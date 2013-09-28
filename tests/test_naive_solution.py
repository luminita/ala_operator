"""
Implements unit tests for the module naive_solution
"""
import os
import sys
import unittest
sys.path.append(os.path.dirname(__file__).replace("tests", "ala_operator"))
import naive_solution
import my_exception

def dir_data():
    return os.path.join(os.path.dirname(__file__), "data")

class TestLoadData(unittest.TestCase):
    """ Test that the function load_data in NaiveSolution loads correctly 
    an input file"""
    def setUp(self):
        unittest.TestCase.setUp(self)
        op_file = os.path.join(dir_data(), "ok_format_operator.txt")
        self.ns = naive_solution.NaiveSolution(op_file)
        self.ns.load_data()
        self.known_values_op1 = {"1":0.9, "4631":0.15, "46732":1.1}
        self.known_values_op2 = {"1":0.92, "467":1.0, "48":1.2}

    def test_number_operators(self):
        """ Test that the number of operators and number of prefixed are loaded correctly"""
        self.assertEqual(len(self.ns.operator_data), 2)
        self.assertEqual(len(self.ns.operator_ids), 2)
        self.assertEqual(len(self.ns.operator_data[0]), 8)
        self.assertEqual(len(self.ns.operator_data[1]), 5)
       
    def test_operator_ids(self):
        """ Test that the operator ids are correct """
        self.assertEqual(self.ns.operator_ids[0], 'A')
        self.assertEqual(self.ns.operator_ids[1], 'B')
        
    def test_operator_known_values(self):
        """ Test that the prices were loaded correctly """
        for dictionary, hash_table in zip([self.known_values_op1, \
            self.known_values_op2], self.ns.operator_data):
            for prefix, value in dictionary.iteritems():
                self.assertAlmostEqual(value, hash_table[prefix])
        
        

if __name__ == '__main__':
    unittest.main()
