from DynamicTree import DynamicTree
from bs4 import BeautifulSoup
import requests


class SteamApiTree(DynamicTree):

    def __init__(self, root, api_key):
        self.api_key = api_key
        super().__init__(root)

    def get_root(self):
        return self.root

    def get_sub_nodes(self, steam_id):
        """
        Uses the Steam API to retrieve a list of friends of a given steam_id
        """

        response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key={self.api_key}&steamid={steam_id}&relationship=friend")

        if response.status_code == 200:
            friends = response.json()["friendslist"]["friends"]
            friend_ids = []
            for friend in friends:
                friend_ids.append(friend["steamid"])

            return friend_ids

        else:
            return []

    def format_output(self, path) -> list:
        """
        Uses the Steam API to retrieve the steam username for all the Steam_ids in the path
        Cannot call the API only once for all users since it does not preserve the path order
        """

        formatted_output = []
        for steam_id in path:
            response = requests.get(f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={self.api_key}&steamids={steam_id}")
            
            if response.status_code == 200:
                formatted_output.append(response.json()["response"]["players"][0]["personaname"]) # retrieve username from request

        return formatted_output