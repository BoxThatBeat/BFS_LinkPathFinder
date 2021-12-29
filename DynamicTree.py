from abc import ABC, abstractmethod

class DynamicTree(ABC):
 
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def get_root(self):
        """
        Returns the root node of the tree
        """
        pass

    @abstractmethod
    def get_sub_nodes(self, node)-> list:
        """
        Returns a list of child nodes
        Returns an empty list if none exist
        """
        pass