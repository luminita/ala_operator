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
        


          
def main():
    t = PrefixTree()
    t.add("1", 0.9)
    t.add("268", 5.1)
    t.add("4631", 0.15)
    t.add("46", 0.17)
    t.add("4673", 0.9)
    t.add("46732", 1.1)
    t.add("468", 0.15)
    t.add("4620", 0.0)
    t.visit()
    print "---------"
    price, path =  search(t, "4667453226", None, [])
    print price, path
  
if __name__ == '__main__':
    main()     
