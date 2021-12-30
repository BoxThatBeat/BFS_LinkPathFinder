from DynamicTree import DynamicTree
from bs4 import BeautifulSoup
import requests

class SteamTree(DynamicTree):

    def get_root(self):
        return self.root

    def get_sub_nodes(self, steam_id):

        response = requests.get(f"http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=3E34D2C4349800457EE849596B5133F7&steamid={steam_id}&relationship=friend")

        if response.status_code == 200:
            friends = response.json()["friendslist"]["friends"]
            friend_ids = []
            for friend in friends:
                friend_ids.append(friend["steamid"])

            return friend_ids

        else:
            return []