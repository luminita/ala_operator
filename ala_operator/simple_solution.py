"""
This file provides a class that implements the simplest solution to 
the problem: the prices of each operators are kept in a hash-table, 
and all the data is loaded in a list of hash tables. When searching 
a number, each hashtable is consulted.  
"""
import sys
import my_exception


class SimpleSolution:
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
                    while line and not line.startswith("Operator"):
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
            
    def get_solution(self, phone_number):
        """ Get the best solurion given a phonenumber; the phone number should be given as a 
        string including no spaces and no other symbols other than digits 
        """
        # keeps the best solution so far as (operator, price); it is a list in case 
        # more than one operator has the same price
        solution = [(None, None, float("inf"))]
        number2search = phone_number
        # stores the indices of the operators for which the phone number was not found yet
        indices = set(range(0, len(self.operator_ids)))
        while len(number2search)>0 and len(indices)>0:
            # this maintains the indices of the operators for which we found this number
            indices2delete = [] 
            for idx in indices:
                # search the phone number in the offer of opperator with index idx
                if  number2search in self.operator_data[idx]:
                    # check if this solution is better than the ones available 
                    price = self.operator_data[idx][number2search]
                    if price < solution[0][2]:
                        solution = [(self.operator_ids[idx], number2search, price)]
                    elif price == solution[0][2]:
                        solution.append((self.operator_ids[idx], number2search, price))
                    # mark this to be removed from the operators that will be considered in the 
                    # next iterations
                    indices2delete.append(idx) 
            # remove the indices of the operators where the phone number was found
            indices = indices.difference(set(indices2delete))
            # drop the last digit of the phone number 
            number2search = number2search[:-1]
        # if no solution was found return an empty list 
        if solution[0][0] == None:
            solution = []
        return solution
                        
def main():
    pass

if __name__ == '__main__':
    main()
