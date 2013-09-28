"""
Implements unit tests for the module naive_solution
"""
import os
import sys
import unittest
sys.path.append(os.path.dirname(__file__).replace("tests", "ala_operator"))
import simple_solution
import my_exception

def dir_data():
    return os.path.join(os.path.dirname(__file__), "data")

class TestLoadData(unittest.TestCase):
    """ Test that the function load_data in NaiveSolution loads correctly 
    an input file"""
    def setUp(self):
        unittest.TestCase.setUp(self)
        op_file = os.path.join(dir_data(), "ok_format_operator.txt")
        self.ns = simple_solution.SimpleSolution(op_file)
        self.ns.load_data()
        self.known_values_op1 = {"1":0.92, "4631":0.15, "46732":1.1}
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
        
        
class TestGetSolution(unittest.TestCase):
    """ Test that the solution returned is correct """
    def setUp(self):
        unittest.TestCase.setUp(self)
        op_file = os.path.join(dir_data(), "ok_format_operator.txt")
        self.ns = simple_solution.SimpleSolution(op_file)
        self.ns.load_data()
        self.known_solutions = {"112345":[("A","1",0.92),("B","1",0.92)], \
            "99999":[], "467":[("A","46",0.17)], "486536":[("B","48",1.2)], \
            "463127":[("A","4631", 0.15)], "46732125":[("B","467",1.0)]}

    def test_known_values(self):
        """ The functions returns the correct solution for a few examples """
        for phone_number, correct_sol in self.known_solutions.iteritems():
            sol = self.ns.get_solution(phone_number)
            print phone_number, sol, correct_sol
            self.assertEqual(len(correct_sol), len(sol))
            i = 0
            while i<len(correct_sol):
                self.assertEqual(correct_sol[i][0], sol[i][0])
                self.assertEqual(correct_sol[i][1], sol[i][1])                    
                self.assertAlmostEqual(correct_sol[i][2], sol[i][2])
                i += 1


if __name__ == '__main__':
    unittest.main()
