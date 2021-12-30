from DynamicTree import DynamicTree
from bs4 import BeautifulSoup
import requests

class WikiTree(DynamicTree):

    def get_root(self):
        return self.root

    def get_sub_nodes(self, profile_url):

        response = requests.get("https://en.wikipedia.org/wiki/Psychedelia")
        if (response.status_code == 200):
            soup = BeautifulSoup(response.content, "html.parser")

            links = []
            for link in soup.find_all('a'):
                links.append(link.get('href'))

            links = [x for x in links if x is not None]
            print(links)
            filteredLinks = filter(lambda link: link[0:4] == "/wiki", links)

            print(list(filteredLinks))