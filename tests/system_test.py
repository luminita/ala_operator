""" This files provides a few system tests to make sure that the program 
returns the correct answer for a few examples """
import os
import shutil
import subprocess
import tempfile
import sys

class TestCorrectInput:
    """ This class provides a few functions when correct input data is given """
    def __init__(self, path_to_main):
        """ Constructor that takes as input the path to main.py """
        self.path_to_main = os.path.join(path_to_main, "main.py")
        # make a temporary directory
        self.tmp_dir = tempfile.mkdtemp()
        lines = "Operator tele2\n1 0.9\n268 5.1\n46 0.17\n4620 0.0\n468 0.15\n"
        lines += "4631 0.15\n4673 0.9\n46732 1.1\nOperator RomaniaOperator\n"
        lines += "1 0.92\n44 0.5\n46 0.2\n467 1.0\n48 1.2\n"
         # make a temporary file with correct format
        self.tmp_file = os.path.join(self.tmp_dir, "op_data.txt")
        in_handler = open(self.tmp_file, "w")
        in_handler.write(lines)
        in_handler.close()
 
    def test_single_number_out_file(self):
        """ Test that the correct solution is written to the output file when 
        one phone number is given """
        out_file = os.path.join(self.tmp_dir, "out.txt")
        subprocess.call(["python", self.path_to_main, "-i", self.tmp_file, "-n", "467327483", \
            "-o", out_file])
        lines = open(out_file).readlines()
        if len(lines) != 2 or not lines[1].startswith("467327483\tRomaniaOperator 467 1.0"):
            res = "FAIL"
        else:
            res = "OK"
        print "TestCorrectInput:test_single_number_out_file: {}".format(res)
        

    def test_many_numbers_out_file(self):
        """ Test that the correct solution is written to the output file when 
        a file including a few phone numbers is given """
        numbers = "6736745ghjgj\n467327483\n1234" 
        nfile = os.path.join(self.tmp_dir, "tmp_numbers.txt")
        file_handler = open(nfile, "w")
        file_handler.write(numbers)
        file_handler.close()
        out_file = os.path.join(self.tmp_dir, "out.txt")
        subprocess.call(["python", self.path_to_main, "-i", self.tmp_file, "-n", nfile, \
            "-o", out_file])
        lines = open(out_file).readlines()
        if len(lines) != 3 or not lines[1].startswith("467327483\tRomaniaOperator 467 1.0") or\
            not lines[2].startswith("1234\ttele2 1 0.9"):
            res = "FAIL"
        else:
            res = "OK"
        print "TestCorrectInput:test_many_numbers_out_file: {}".format(res)

    def test_single_number_out_screen(self):
        """ Test that the correct solution is written on the screen  """
        out_file = os.path.join(self.tmp_dir, "out.txt")
        out_handler = open(out_file, "w")
        subprocess.call(["python", self.path_to_main, "-i", self.tmp_file, "-n", "469999999"], \
            stdout=out_handler)
        out_handler.close()
        lines = open(out_file).readlines()
        if len(lines) != 2 or not lines[1].startswith("469999999\ttele2 46 0.17"):
            res = "FAIL"
        else:
            res = "OK"
        print "TestCorrectInput:test_single_number_out_screen: {}".format(res)
        
    def test_several_numbers_out_screen(self):
        """ Test that the correct solution is written on the screen  """
        numbers = "468563\n1234637" 
        nfile = os.path.join(self.tmp_dir, "tmp_numbers.txt")
        file_handler = open(nfile, "w")
        file_handler.write(numbers)
        file_handler.close()
        out_file = os.path.join(self.tmp_dir, "out.txt")
        out_handler = open(out_file, "w")
        subprocess.call(["python", self.path_to_main, "-i", self.tmp_file, "-n", nfile], \
            stdout=out_handler)
        out_handler.close()
        lines = open(out_file).readlines()
        if len(lines) != 3 or not lines[1].startswith("468563\ttele2 468 0.15") or \
                not lines[2].startswith("1234637\ttele2 1 0.9"):
            res = "FAIL"
        else:
            res = "OK"
        print "TestCorrectInput:test_several_numbers_out_screen: {}".format(res)

    def __del__(self):
        shutil.rmtree(self.tmp_dir)


def main():
    if len(sys.argv) < 2:
        sys.exit("Path to main.py need to be provided")
    path_to_main = sys.argv[1]

    tfi = TestCorrectInput(path_to_main)
    tfi.test_single_number_out_file()
    tfi.test_many_numbers_out_file()
    tfi.test_single_number_out_screen()
    tfi.test_several_numbers_out_screen()

if __name__ == '__main__':
    main()
