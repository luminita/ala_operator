"""
This file provides a class that implements the simplest solution to 
the problem: the prices of each operators are kept in a hash-table, 
and all the data is loaded in a list of hash tables. When searching 
a number, each hashtable is consulted.  
"""
import my_exception


class NaiveSolution:
    def __init__(self, operator_file):
        self.operator_file = operator_file
        self.operator_data = []
        self.operator_ids = []


    def load_data(self):
        """ Load the data from the operator file; 
        The variable self.operator_data is a list of hash tables; 
        The variable self.operator_ids is a list of operator ids in the same order as 
        the hash tables """
        try:
            in_handler = open(self.operator_file)
            line = in_handler.readline()
            while line:
                # load the offers of each operator
                if line.startswith("Operator"):
                    operator_id = line.split()[1].strip()
                    self.operator_ids.append(operator_id)
                    data = {}
                    # each line should represent an offer, or is the start of 
                    # a new operator 
                    line = in_handler.readline()
                    while not line.startswith("Operator"):
                        prefix = line.split()[0]
                        price = float(line.split()[1])
                        data[prefix] = price
                        line = in_handler.readline()
                    self.operator_data.append(data)
                else:
                   raise my_exception.MyException("Incorrect operator file format") 
            in_handler.close()
        except Exception, e:
            sys.exit(str(e)) 

