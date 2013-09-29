""" Class that provides a few IO operations """
import sys


def load_lines(filename):
    """ Given a filename, return all the lines in the file wih newline dropped """
    try:
        in_handler = open(filename)
        lines = [l.strip() for l in in_handler.readlines()]
        in_handler.close()
        return lines 
    except Exception, e:
        sys.exit(str(e))

def write_lines(lines, filename): 
    """ Print a list of lines to a file. Note that each line should include
    the newline character """
    try:    
        outf = open(filename, "w")
        for l in lines:
            outf.write(l)
        outf.close()
    except Exception, e:
        sys.exit(str(e))
