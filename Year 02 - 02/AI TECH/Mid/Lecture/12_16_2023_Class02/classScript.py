import numpy

# Class initiation
class Node:
    # Double underscore (__) is defined as predefined special function
    # this one is called contructor, a function that will be called on create
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
        
    def print_name(self):
        print(self.name)
    
    # Use @staticmethod before each function that doesn't need local data
    @staticmethod
    def print_test():
        print('HelloWorld')
        
        
if __name__ == '__main__':
    # Pass class properties to an instance
    node_A = Node('A')
    node_B = Node('B')

    # Access local variables & functions: use dot (.)
    # call
    print(node_A.name)
    node_A.print_name()

    # assign
    node_A.left = node_B
    
    node_A.print_test02()

    