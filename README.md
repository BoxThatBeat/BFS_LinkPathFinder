# BFS Steam Friend Finder

A simple program that implements BFS (Breadth First Search) and uses it to find the minimum number of friend links on a Steam friends list it takes to get to a given steam user. For example, given a Steam user A who has friends B,C,D and Steam user C has friends E,F,G : The path from Steam user A to F is A->C->F. In this project I used abstraction to abstract the idea of a tree so that the BFS implementation would be free of those details and the implementation of retrieving Steam friends lists could be swapped in. I found two different methods for retrieving Steam Friends list of a given Steam user: Using the Steam API which requires an API key and using web scraping on the Steam Community sites.   

## Usage:   

If you have a Steam API key:
```
python PathFinder.py <source-64bit-SteamId> <target-64bit-SteamId> -api_key <api_key>
```

Otherwise:
```
python PathFinder.py <source-Steam-Profile_URL> <target-Steam-Profile_URL>
```
