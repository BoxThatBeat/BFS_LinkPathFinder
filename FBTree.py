import DynamicTree
from bs4 import BeautifulSoup
import requests

class FBTree(DynamicTree):

    def get_root(self):
        return self.root

    def get_sub_nodes(self, profile_url):

        soup = BeautifulSoup(requests.get(f"{profile_url}/friends").text, "html.parser")
        pass