from classScript import Node 

# Local function
def print_tree(node, layer= 0):
        
    for i in range(layer):
        print(' |', end= '')
    print(node.name)
        
    if node.left != None:
        print_tree(node.left, layer+1)
    if node.right != None:
        print_tree(node.right, layer+1)
        

# Main
if __name__ == '__main__':
    print('Start Creating Tree!!!')
    
    nodes = {}
    for i in range(7):
        name = chr(65 + i)
        localNode = Node(name)
        nodes.update({name: localNode})
    
    # Create connection
    nodes['A'].left = nodes['B']
    nodes['A'].right = nodes['C']
    
    nodes['B'].left = nodes['D']
    nodes['C'].right = nodes['G']
    nodes['C'].left = nodes['E']
    
    nodes['E'].left = nodes['F']
    
    
    print_tree(nodes['A'])