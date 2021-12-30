from DynamicTree import DynamicTree
from bs4 import BeautifulSoup
import requests

class SteamWebTree(DynamicTree):

    def get_root(self):
        return self.root

    def get_sub_nodes(self, profile_url):

        response = requests.get(f"{profile_url}/friends")
        if (response.status_code == 200):
            soup = BeautifulSoup(response.content, "html.parser")

            links = []
            for link in soup.find_all('a', attrs={"class": ["selectable_overlay"]}):
                links.append(link.get('href'))
            
            return links

        else:
            return []

    def format_output(self, path) -> list:

        formatted_path = []
        for link in path:
            formatted_path.append(link.split("/")[-1]) #only take the steam username

        return formatted_path