"""
This file provides a class that implements a slightly optimized solution than the one 
given in simple_solution. When loading the data, the longest prefix provided by an operator 
is stored. Instead of starting by searching the full phone number in each operator's offer, 
I start by searching only the first K digits of the phone number, where K is the length of 
the largest prefix provided by an operator 
"""
import sys
import numpy
import my_exception


class OptimizedSolution:
    def __init__(self, operator_file):
        self.operator_file = operator_file
        self.operator_data = []
        self.operator_ids = []
        self.longest_prefix = -1

    def load_data(self):
        """ Load the data from the file giving the offers of all the operators ; 
        The variable self.operator_data will include a list of dictionaries
        The variable self.operator_ids will include a list of operator ids in the same order as 
        the dictionaries  """
        try:
            in_handler = open(self.operator_file)
            line = in_handler.readline()
            while line:
                # load the offers of each operator
                if line.startswith("Operator"):
                    operator_id = line.split()[1].strip()
                    self.operator_ids.append(operator_id)
                    data = {}
                    # each line gives a prefix price, or it is the start of a new operator 
                    line = in_handler.readline()
                    while line and not line.startswith("Operator"):
                        prefix = line.split()[0].strip()
                        if len(prefix) > self.longest_prefix:
                            self.longest_prefix = len(prefix)
                        price = float(line.split()[1])
                        data[prefix] = price
                        line = in_handler.readline()
                    self.operator_data.append(data)
                else:
                   # I just raise an exception if the file includes anything else than expected
                   raise my_exception.MyException("Incorrect operator file format") 
            in_handler.close()
        except Exception, e:
            sys.exit(str(e))
            
    def get_solution(self, phone_number):
        """ Get the best solution given a phone number; the phone number should be given as a 
        string including no spaces and no other symbols other than digits 
        """
        # keeps the best solution so far as (operator, prefix, price); 
        # the solution is a list in case more than one operator has the same price
        solution = [(None, None, numpy.inf)]
        # start by searching the longest possible prefix to be found
        number2search = phone_number[0:self.longest_prefix+1]
        # stores the indices of the operators for which the phone number was not found yet
        indices = set(range(0, len(self.operator_ids)))
        while len(number2search)>0 and len(indices)>0:
            # I store the indices of the operators for which the number was found
            indices2delete = [] 
            for idx in indices:
                # search the phone number in the offer of operator with index idx
                if  number2search in self.operator_data[idx]:
                    # check if this solution is better than the ones found before 
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
    S = OptimizedSolution("../examples/ex_operators_2.txt")
    S.load_data()
    numbers = [l.strip() for l in open("../examples/ex_numbers_2.txt").readlines()]
    for n in numbers:
        print n, S.get_solution(n)

if __name__ == '__main__':
    main()
