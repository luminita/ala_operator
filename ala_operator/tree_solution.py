import my_exception
import sys


class PrefixTree:
    def __init__(self):
        """ children is a dictionary character -> Trie  """
        self.price = None
        self.children = {} 

    def add(self, prefix, price):
        """ Add prefix to dictionary """
        # if we are already at the end of the prefix we just add this 
        st = prefix[0]
        if len(prefix) == 1:
            if st not in self.children:
                self.children[st] = PrefixTree()
            self.children[st].price = price
        else:
            if st not in self.children:
                self.children[st] = PrefixTree()
            node = self.children[st]
            node.add(prefix[1:], price)

    def visit(self):
        """ Print all the nodes in the tree with their price"""
        for k, v in self.children.items():
            print k, v.price
            v.visit()


def search(curr_node, number, price, path):
    """ Search the phone number starting from curr_node """
    st = number[0]
    if (len(number) == 0):
        return price, path
    if st not in curr_node.children:
        if curr_node.price != None:
            price = curr_node.price
        return price, path
    if len(curr_node.children) == 0:
        return curr_node.price, path
    cn = curr_node.children[st]
    if cn.price != None:
        price = cn.price
    path.append(st)
    return search(cn, number[1:], price, path)
        
class TreeSolution:
    def __init__(self):
        self.trees = []
        self.ids = [] 

    def add(self, tree, tree_id):
        self.trees.append(tree)
        self.ids.append(tree_id)

    def get_solution(self, phone_number):
        """ Get the best solution by searching in all trees """
        solution = [(None, None, 1.0e6)]
        for (tree, tree_id) in zip(self.trees, self.ids):
            price, path =  search(tree, phone_number, None, [])
            if price <= solution[0][2]:
                solution[0] = (tree_id, "".join(path), price)

        return solution 

    def load_data(self, operator_file):
        """ Load the data of each operator """
        try:
            in_handler = open(operator_file)
            line = in_handler.readline()
            while line:
                # load the offers of each operator
                if line.startswith("Operator"):
                    tree = PrefixTree()
                    operator_id = line.split()[1].strip()
                    line = in_handler.readline()
                    while line and not line.startswith("Operator"):
                        prefix = line.split()[0].strip()
                        price = float(line.split()[1])
                        tree.add(prefix, price)
                        line = in_handler.readline()
                    self.trees.append(tree)
                    self.ids.append(operator_id)
                else:
                    # I just raise an exception if the file includes anything else than expected
                    raise my_exception.MyException("Incorrect operator file format") 
            in_handler.close()
        except Exception, e:
            sys.exit(str(e))
            
    def print2screen(self):
      for (tree, tree_id) in zip(self.trees, self.ids):
          print tree_id
          tree.visit()
          print "///////////////////"

    
def main():
    t = TreeSolution()
    t.load_data("../examples/ex_operators_1.txt")
    t.print2screen()
    print t.get_solution("4672974752876")


  
if __name__ == '__main__':
    main()     
