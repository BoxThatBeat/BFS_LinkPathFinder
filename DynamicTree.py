from abc import ABC, abstractmethod

class DynamicTree(ABC):
 
    def __init__(self, root):
        self.root = root
        super().__init__()
    
    @abstractmethod
    def get_root(self):
        """
        Returns the root node of the tree
        """
        pass

    @abstractmethod
    def get_sub_nodes(self, node) -> list:
        """
        Returns a list of child nodes
        Returns an empty list if none exist
        """
        pass

    @abstractmethod
    def format_output(self, path) -> list:
        """
        Takes the path output list and formats it to make sense given the input for this 'tree'
        """
        pass