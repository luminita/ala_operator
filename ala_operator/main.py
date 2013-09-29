"""
Main body of the software
"""
import os 
import sys
import argparse 
import data_handler
import simple_solution
import optimized_solution


def get_solution_class(method_string):
    """ Return the class that will be used to calculate the solution """
    if method_string == "simple":
        return simple_solution.SimpleSolution
    if method_string == "fast":
        return optimized_solution.OptimizedSolution
    sys.exit("Unknown method: {}".format(method_string))
 
def get_phone_numbers(phone_numbers_data):
    """ Given a phone number or a file including phone numbers, return a list containing
    the valid phone numbers """
    phone_numbers = []
    if os.path.isfile(phone_numbers_data):
        # load only valid phone numbers (they should contain only digits)
        phone_numbers = [pn for pn in data_handler.load_lines(phone_numbers_data) \
            if pn.isdigit()]
    elif phone_numbers_data.isdigit():
        phone_numbers = [phone_numbers_data]
    return phone_numbers

def format_solution(tuple_list):
    """ Given a list of tuples (operator_id, prefix, price) concatenate them to a string """
    string_list = ["{} {} {}".format(*tup) for tup in tuple_list]
    if len(string_list) == 0:
        return "No solution"
    return "\t".join(string_list)     

def main():
    # command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help = "File including the operators' offers", \
        metavar = "operator_file", required = True)
    parser.add_argument('-n', help="Phone number or file including phone numbers, one per line",\
        metavar = "phone_number(s)", required = True)
    parser.add_argument('-m', help = "Method to solve the problem [simple|fast], default = fast", \
        metavar = "solving_method", required = False, default = "fast")     
    parser.add_argument('-o', help = "Output file. By default the result is printed on the screen", \
        metavar = "out_file", required = False, default = None)        
    
    # parse the command line arguments
    args = parser.parse_args()    
    operator_file = args.i
    phone_numbers_data = args.n
    solution_class = get_solution_class(args.m)
    out_file = args.o
    
    # get the list of phone numbers; if no phone number loaded nothing to do
    phone_numbers = get_phone_numbers(phone_numbers_data)
    if len(phone_numbers) == 0:
        sys.exit("Could not load any phone number, nothing to do")

    # load all the operator data
    solution_object = solution_class(operator_file)
    solution_object.load_data()
   
    # find the best operator for each phone numbers
    solutions = ["Phone number\tOperator_id Prefix_used Price\n"]    
    for number in phone_numbers:
        solution = solution_object.get_solution(number)
        str_solution = "{}\t{}\n".format(number, format_solution(solution))
        solutions.append(str_solution)

    # write the result to the output file or to the screen 
    if out_file != None:
        data_handler.write_lines(solutions, out_file)
    else:
        for sol in solutions:
            print sol,     
                
    
if __name__ == '__main__':
    main()

