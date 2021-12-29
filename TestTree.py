from DynamicTree import DynamicTree

class TestTree(DynamicTree):
 
    def __init__(self, root):
        self.tree = {
            root: ['A1', 'A2', 'A3'],
            'A1' : ['B1','B2'],
            'A2' : ['C1'],
            'A3' : ['D1','D2'],
            'B1' : ['E1','E2','E3','A1'], #Includes cycle
            'B2' : [],
            'C1' : [],
            'D1' : [],
            'D2' : ['F1','F2'],
            'E1' : [],
            'E2' : [],
            'E3' : [],
            'F1' : [],
            'F2' : ['G1'],
            'G1' : []
        }
        super().__init__(root)


    def get_root(self):
        """
        Returns the root node of the tree
        """
        return self.root

 
    def get_sub_nodes(self, node)-> list:
        """
        Returns a list of child nodes
        Returns an empty list if none exist
        """

        return self.tree[node]
     