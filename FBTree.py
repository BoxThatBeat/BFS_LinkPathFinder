import DynamicTree
from bs4 import BeautifulSoup
import requests

class FBTree(DynamicTree):

    def __init__(self, root_profile, goal):
        self.root_profile = root_profile
        self.goal_profile = goal


    def get_root(self):
        return self.root_profile

    def get_sub_nodes(self, profile_url):

        soup = BeautifulSoup(requests.get(f"{profile_url}/friends").text, "html.parser")



