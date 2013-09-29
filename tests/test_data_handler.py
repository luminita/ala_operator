"""
Implements unit tests for the module data_handler
"""
import os
import sys
import unittest
import tempfile
import shutil
sys.path.append(os.path.dirname(__file__).replace("tests", "ala_operator"))
import data_handler

# TODO: path should be changed to something more elegant
# one of the tests can be broken in smaller parts 


class TestWriteLines(unittest.TestCase):
    """ Test the write_lines function """
    def setUp(self):
        unittest.TestCase.setUp(self)
        # make a temporary directory to store files 
        self.tmp_dir = tempfile.mkdtemp()
        self.tmp_file = os.path.join(self.tmp_dir, "tmp.txt")
        self.lines = ["1\n", "2\n"]
        data_handler.write_lines(self.lines, self.tmp_file)

    def test_file_exists(self):
        """ Test that the file was created """
        self.assertTrue(os.path.isfile(self.tmp_file))

    def test_file_content(self):    
        """ Test that the file contains the expected lines """
        loaded_lines = open(self.tmp_file).readlines()
        for exp_line, line in zip(self.lines, loaded_lines):
            self.assertEqual(exp_line, line)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        shutil.rmtree(self.tmp_dir)


class TestLoadLine(unittest.TestCase):
    """ Test the load_lines function """
    def setUp(self):
        """ Create a temporary files with a few lines """
        unittest.TestCase.setUp(self)
        self.lines = "123\n45675\n236456"
         # make a temporary file including these lines
        (tmp, self.tmp_file) = tempfile.mkstemp()
        in_handler = open(self.tmp_file, "w")
        in_handler.write(self.lines)
        in_handler.close()
        
    def test_file_content(self):
        """ Test that the lines loaded by the function are correct """
        loaded_lines = data_handler.load_lines(self.tmp_file)
        for (exp_l, line) in zip(self.lines.split("\n"), loaded_lines):
            self.assertEqual(exp_l, line)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        os.remove(self.tmp_file)

if __name__ == '__main__':
    unittest.main()


